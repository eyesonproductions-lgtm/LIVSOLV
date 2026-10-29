const HEADERS = {'Cache-Control':'private, no-store, max-age=0','Referrer-Policy':'no-referrer','X-Content-Type-Options':'nosniff','X-Robots-Tag':'noindex, nofollow'};
const encoder = new TextEncoder();
function reply(message, status=400) {return new Response(message,{status,headers:HEADERS});}
function json(data,status=200){return new Response(JSON.stringify(data),{status,headers:{...HEADERS,'Content-Type':'application/json'}});}
async function hmac(secret,text){const key=await crypto.subtle.importKey('raw',encoder.encode(secret),{name:'HMAC',hash:'SHA-256'},false,['sign']);return [...new Uint8Array(await crypto.subtle.sign('HMAC',key,encoder.encode(text)))].map(x=>x.toString(16).padStart(2,'0')).join('');}
function equal(a,b){if(typeof a!=='string'||typeof b!=='string'||a.length!==b.length)return false;let diff=0;for(let i=0;i<a.length;i++)diff|=a.charCodeAt(i)^b.charCodeAt(i);return diff===0;}
function validID(id){return typeof id==='string'&&/^cs_live_[A-Za-z0-9]{16,240}$/.test(id);}
export async function stripeSession(id,env,fetcher=fetch){
 const res=await fetcher('https://api.stripe.com/v1/checkout/sessions/'+encodeURIComponent(id),{headers:{Authorization:'Bearer '+env.STRIPE_RESTRICTED_KEY,'Stripe-Version':'2026-09-30.endive'},signal:AbortSignal.timeout(12000)});
 if(!res.ok)throw new Error('Verification unavailable');return res.json();
}
export function eligible(s,env){return s.object==='checkout.session'&&s.livemode===true&&s.mode==='payment'&&s.status==='complete'&&s.payment_status==='paid'&&s.currency==='usd'&&s.amount_total>=1200&&s.payment_link===env.BINDER_PAYMENT_LINK;}
async function entitlement(id,env){return 'orders/'+await hmac(env.DELIVERY_SIGNING_KEY,id)+'.json';}
export async function verifyWebhook(raw,header,secret,now=Date.now()){
 if(!secret||!header)return false;
 const fields=header.split(',').map(x=>x.split('='));const stamp=fields.find(x=>x[0]==='t')?.[1];
 if(!/^\d+$/.test(stamp||'')||Math.abs(Math.floor(now/1000)-Number(stamp))>300)return false;
 const expected=await hmac(secret,stamp+'.'+raw);return fields.filter(x=>x[0]==='v1').some(x=>equal(x[1],expected));
}
export async function handle(request,env,fetcher=fetch){
 const url=new URL(request.url);
 if(url.pathname==='/api/binder/webhook'){
  if(request.method!=='POST')return reply('Method not allowed',405);
  if(!env.STRIPE_WEBHOOK_SECRET||!env.DELIVERY_SIGNING_KEY)return reply('Delivery not configured',503);
  if(Number(request.headers.get('content-length')||0)>1000000)return reply('Request too large',413);
  const raw=await request.text();if(raw.length>1000000)return reply('Request too large',413);
  if(!await verifyWebhook(raw,request.headers.get('stripe-signature'),env.STRIPE_WEBHOOK_SECRET))return reply('Invalid signature',400);
  let event;try{event=JSON.parse(raw);}catch{return reply('Invalid event',400);}
  if(!['checkout.session.completed','checkout.session.async_payment_succeeded','checkout.session.async_payment_failed'].includes(event.type))return json({received:true});
  const id=event.data?.object?.id;if(!validID(id))return reply('Invalid session',400);
  // Re-read Stripe rather than trusting event payment fields, including out-of-order events.
  const s=await stripeSession(id,env,fetcher);if(eligible(s,env)){
   await env.PAID_PRODUCTS.put(await entitlement(id,env),JSON.stringify({version:1,session:id,paid:true}),{httpMetadata:{contentType:'application/json'}});
  }
  return json({received:true});
 }
 if(!['/api/binder/verify','/api/binder/download'].includes(url.pathname))return reply('Not found',404);
 if(env.DELIVERY_ENABLED!=='true'||!env.STRIPE_RESTRICTED_KEY||!env.DELIVERY_SIGNING_KEY||!env.PAID_PRODUCTS)return reply('Secure downloads are being prepared. Keep your purchase receipt.',503);
 if(url.pathname==='/api/binder/verify'){
  if(request.method!=='POST')return reply('Method not allowed',405);
  if(request.headers.get('origin')!==url.origin)return reply('Request not allowed',403);
  if(Number(request.headers.get('content-length')||0)>1024)return reply('Request too large',413);
  let id;try{const body=await request.text();if(body.length>1024)return reply('Request too large',413);id=JSON.parse(body).session_id;}catch{return reply('Invalid request');}
  if(!validID(id))return reply('Use the link from your purchase',403);
  const s=await stripeSession(id,env,fetcher);if(!eligible(s,env))return reply('Payment is not confirmed for this binder.',403);
  // Access requires the signed webhook's durable record, not just a success-page visit.
  if(!await env.PAID_PRODUCTS.head(await entitlement(id,env)))return reply('Payment confirmation is arriving. Please try again shortly.',409);
  if(!await env.PAID_PRODUCTS.head(env.BINDER_OBJECT_KEY))return reply('Your file is being prepared. Keep your receipt.',503);
  const exp=Math.floor(Date.now()/1000)+600;const payload=id+'.'+exp;const token=payload+'.'+await hmac(env.DELIVERY_SIGNING_KEY,payload);
  const res=json({download:'/api/binder/download'});res.headers.set('Set-Cookie','livsolv_delivery='+token+'; Path=/api/binder; Max-Age=600; HttpOnly; Secure; SameSite=Strict');return res;
 }
 if(request.method!=='GET')return reply('Method not allowed',405);
 const token=request.headers.get('cookie')?.split(';').map(x=>x.trim()).find(x=>x.startsWith('livsolv_delivery='))?.slice(17);
 const parts=token?.split('.');if(!parts||parts.length!==3||!validID(parts[0])||!/^\d+$/.test(parts[1]))return reply('Please verify your purchase again.',403);
 const [id,expires,sig]=parts;const now=Math.floor(Date.now()/1000);if(Number(expires)<now||Number(expires)>now+600||!equal(sig,await hmac(env.DELIVERY_SIGNING_KEY,id+'.'+expires)))return reply('Download access expired. Verify your purchase again.',403);
 if(!await env.PAID_PRODUCTS.head(await entitlement(id,env)))return reply('Purchase not confirmed',403);
 const s=await stripeSession(id,env,fetcher);if(!eligible(s,env))return reply('Payment not confirmed',403);
 const file=await env.PAID_PRODUCTS.get(env.BINDER_OBJECT_KEY);if(!file)return reply('File temporarily unavailable',503);
 return new Response(file.body,{headers:{...HEADERS,'Content-Type':'application/zip','Content-Disposition':'attachment; filename="LIVSOLV-Systems-Down-Household-Binder.zip"'}});
}
export default {async fetch(request,env){try{if(new URL(request.url).pathname.startsWith('/api/binder/'))return await handle(request,env);return env.ASSETS.fetch(request);}catch{return reply('Unable to verify your purchase right now. Please try again shortly.',503);}}};
