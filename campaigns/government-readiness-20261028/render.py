from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import json
OUT=Path(__file__).parent
G='#12382b'; I='#f8f5ec'; M='#d6dfce'; A='#bd5a3c'
def font(n,bold=False):
 return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if bold else '')+'.ttf',n)
def wrap(draw,text,f,width):
 lines=[]
 for para in text.split('\n'):
  line=''
  for word in para.split():
   trial=(line+' '+word).strip()
   if draw.textlength(trial,font=f)>width and line: lines.append(line);line=word
   else:line=trial
  lines.append(line)
 return lines
def block(d,text,x,y,size,width,color,bold=False,gap=1.25):
 f=font(size,bold)
 for line in wrap(d,text,f,width):d.text((x,y),line,font=f,fill=color);y+=int(size*gap)
 return y
slides=[
 ('THE PREPAREDNESS HEADLINES','What if the basics\nstop working?','Governments are asking households to prepare for disrupted power, water, food and communications.','Here is what the official guidance actually says.','Current guidance checked 28 OCT 2026 | Sources in caption'),
 ('NETHERLANDS','72 HOURS','Prepare to manage without basic essentials, including electricity and water.','Start with what you already own. The government says your kit should fit your household.','Source: Dutch government / Denk vooruit | 2025–26 booklet'),
 ('NORWAY','1 WEEK','Plan for interruptions to electricity, water, sewage, internet, mobile networks and payments.','This advice increased from three days to one week in May 2024. It is not a newly announced outage.','Source: Norwegian Directorate for Civil Protection | dsb.no'),
 ('SWEDEN','AT LEAST\n1 WEEK','Plan to manage without electricity, water or the ability to buy food.','Water, food, warmth and access to reliable information are core priorities.','Source: Swedish authorities | krisinformation.se/en/get-prepared'),
 ('GERMANY','10 DAYS\nIF POSSIBLE','The federal civil-protection agency advises enough supplies to support yourself for ten days.','Even three days helps. Build your supplies gradually rather than buying everything at once.','Source: Federal Office of Civil Protection / BBK | bbk.bund.de'),
 ('UNITED STATES / WATER','3 DAYS FIRST.\n2 WEEKS IF ABLE.','CDC advises at least one gallon of water per person per day for three days; try for two weeks if possible.','This is water-storage guidance, not a prediction of a two-week nationwide utility outage.','Source: CDC emergency water guidance | Published 27 JUN 2025'),
 ('WHAT THESE WARNINGS MEAN','A plan.\nNot a countdown.','These recommendations cover different emergencies. They do not establish a scheduled worldwide blackout.','We did not verify a new blanket three-week warning. Check your own local alerts for current instructions.','LIVSOLV editorial summary | Official guidance checked 28 OCT 2026'),
 ('YOUR FIRST STEPS / LOW BUDGET','Start where\nyou are.','1  Find your flashlight and charge available power banks.\n2  Write down contacts and agree on a check-in plan.\n3  Count safe water and food you already have.','Save this. Share it with your household.\nFree Emergency Quick Cards at LIVSOLV.com','Never run generators, grills or outdoor fuel-burning stoves indoors.')
]
for i,(tag,title,body,note,source) in enumerate(slides,1):
 dark=i in [1,7,8];bg=G if dark else I;fg=I if dark else G
 im=Image.new('RGB',(1080,1350),bg);d=ImageDraw.Draw(im)
 d.rectangle((72,72,130,82),fill=A)
 d.text((72,106),'LIVSOLV',font=font(30,True),fill=fg)
 d.text((898,110),f'{i:02}/08',font=font(24),fill=fg)
 block(d,tag,72,202,24,936,fg,True)
 y=block(d,title,72,280,80 if i not in [5,6] else 72,936,fg,True,1.13)
 y=block(d,body,72,max(y+50,570),36,936,fg,gap=1.35)
 note_y=max(y+36,860)
 d.line((72,note_y-20,1008,note_y-20),fill=A,width=3)
 end=block(d,note,72,note_y,29,936,M if dark else G,gap=1.35)
 assert end<1195,(i,end)
 block(d,source,72,1214,21,936,M if dark else G,gap=1.3)
 d.text((72,1294),'LIVE IN THE SOLUTION.',font=font(18,True),fill=fg)
 im.save(OUT/f'government-readiness-{i:02}.jpg',quality=93)
# Pinterest companion, deliberately a single useful reference pin.
im=Image.new('RGB',(1000,1500),I);d=ImageDraw.Draw(im)
d.rectangle((0,0,1000,255),fill=G)
d.text((64,45),'LIVSOLV / SAVE THIS GUIDE',font=font(24,True),fill=I)
block(d,'How long should\nyou prepare for?',64,104,56,880,I,True,1.1)
rows=[('NETHERLANDS','72 hours','Without basic essentials such as power and water.'),('NORWAY + SWEDEN','At least 1 week','Household self-preparedness for disrupted services.'),('GERMANY','10 days if possible','Even three days helps. Build supplies gradually.'),('U.S. CDC / WATER','3 days; 2 weeks if able','At least 1 gallon per person, per day.')]
y=300
for tag,title,body in rows:
 d.text((64,y),tag,font=font(22,True),fill=A)
 d.text((64,y+39),title,font=font(45,True),fill=G)
 block(d,body,64,y+103,27,870,G)
 d.line((64,y+180,936,y+180),fill=M,width=2);y+=208
block(d,'Preparedness guidance is not an announcement of a coming blackout.',64,1155,31,870,G,True)
block(d,'Start with what you own. Get free Emergency Quick Cards at LIVSOLV.com',64,1268,29,870,G)
block(d,'Sources: Denk vooruit, DSB, Krisinformation, BBK, CDC\nChecked 28 OCT 2026. Summaries, not verbatim headlines.',64,1410,18,870,G)
im.save(OUT/'pinterest-government-readiness.jpg',quality=93)
thumb=Image.new('RGB',(1080,810),'#e2e2e2')
for i in range(8):
 p=Image.open(OUT/f'government-readiness-{i+1:02}.jpg');p.thumbnail((270,338));thumb.paste(p,((i%4)*270,(i//4)*405))
thumb.save(OUT/'contact-sheet.jpg')
print(json.dumps({'files':[p.name for p in OUT.glob('*.jpg')]}))
