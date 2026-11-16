from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
out=Path(__file__).parent
slides=[
('THE 60-SECOND HOUSEHOLD CHECK','The power is out.\nWhere is your\nflashlight?','If you have to hunt for the basics in the dark, your next step is simpler than buying more gear.','Swipe for five things to sort out before you need them.'),
('01 / LIGHT','Give the light\na home.','Pick one easy-to-reach place for a working flashlight. Tell everyone where it lives. Test it today.','Solar lights still need charging time. Keep another charged light or spare batteries ready.'),
('02 / BACKUP POWER','Choose what\nstays on.','Write down your essentials: phone, light, router, and any equipment your household depends on. Then check what your backup can actually run.','A battery’s stored energy and its maximum power output are different limits. Check both before relying on it.'),
('03 / CHECK-IN PLAN','No cell signal?\nCheck the Wi-Fi.','If internet service still works, Wi-Fi messaging or previously enabled Wi-Fi calling may help. Your router also needs power.','Write down one out-of-town contact and agree on a meeting place in case every network fails.'),
('04 / SAFE WATER','Count people.\nThen count water.','CDC’s starting point: at least 1 gallon per person per day for 3 days. For four people, that is 12 gallons.','Plan extra for pets and additional needs. Build toward two weeks if possible. Source: CDC emergency water guidance.'),
('05 / PUT IT ON PAPER','Your plan should\nwork offline.','Write down item locations, contacts and household jobs. Keep a paper copy somewhere everyone can find it.','Get the free Emergency Quick Cards at LIVSOLV.com. Save this carousel and share it with your household.')
]
green='#12382b'; ivory='#f8f5ec'; accent='#c27b51';muted='#d8dfd2'
def font(n,b=False):return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if b else '')+'.ttf',n)
def lines(d,t,f,w):
 r=[]
 for p in t.split('\n'):
  s=''
  for word in p.split():
   q=(s+' '+word).strip()
   if s and d.textlength(q,font=f)>w:r.append(s);s=word
   else:s=q
  r.append(s)
 return r
def block(d,t,y,n,c,b=False):
 f=font(n,b)
 for line in lines(d,t,f,744):d.text((60,y),line,font=f,fill=c);y+=int(n*1.32)
 return y
for i,(tag,title,body,note) in enumerate(slides,1):
 dark=i in (1,6);bg=green if dark else ivory;fg=ivory if dark else green
 im=Image.new('RGB',(864,1080),bg);d=ImageDraw.Draw(im)
 d.rectangle((60,58,112,65),fill=accent)
 d.text((60,89),'LIVSOLV',font=font(25,True),fill=fg)
 d.text((730,90),f'{i}/6',font=font(22),fill=fg)
 block(d,tag,178,19,fg,True)
 y=block(d,title,244,55,fg,True)
 y=block(d,body,max(475,y+30),29,fg)
 y=max(777,y+30)
 d.line((60,y-19,804,y-19),fill=accent,width=3)
 end=block(d,note,y,24,muted if dark else green)
 assert end<1010,(i,end)
 d.text((60,1031),'PRACTICAL PREP. START WITH WHAT YOU OWN.',font=font(16,True),fill=fg)
 im.save(out/f'outage-check-{i:02}.jpg',quality=92,optimize=True)
sheet=Image.new('RGB',(864,720),'#ddd')
for i in range(6):
 im=Image.open(out/f'outage-check-{i+1:02}.jpg');im.thumbnail((288,360));sheet.paste(im,((i%3)*288,(i//3)*360))
sheet.save(out/'contact-sheet.jpg')
print('Rendered six 864x1080 JPEG slides.')
