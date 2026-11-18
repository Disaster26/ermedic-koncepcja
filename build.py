from PIL import Image
# produkty: klucz, liczba zdjec, typ, nazwa, cena, dopisek
P=[('ermedic',4,'Łóżko pielęgnacyjne','ERMEDIC 90x200','1 880 zł','Rata 0% od 376 zł','Lite drewno · ★★★★★ 6 opinii'),
   ('classic2',2,'Łóżko rehabilitacyjne','CLASSIC 2 90x200','2 479 zł','','Tapicerowane, do 200x200 cm'),
   ('comfort',4,'Łóżko rehabilitacyjne','COMFORT 90x200','2 479 zł','Rata 0% od 495,80 zł','Tapicerowane, do 200x200 cm'),
   ('comfortplus',3,'Łóżko rehabilitacyjne','COMFORT PLUS 90x200','2 679 zł','','Pikowany zagłówek, do 200x200 cm'),
   ('ergold',4,'Łóżko rehabilitacyjne','ERGOLD 2 90x200','2 659 zł','',''),
   ('classic',2,'Łóżko rehabilitacyjne','CLASSIC 90x200','2 479 zł','','★★★★★ 2 opinie'),
   ('erlux',1,'Łóżko rehabilitacyjne','ERLUX 90x200','2 489 zł','','Z pojemnikiem pod stelażem')]
out=[]
for k,n,typ,naz,cena,rata,gw in P:
    sl=[]
    for i in range(1,n+1):
        w,h=Image.open(f'img/{k}{i}-560.webp').size
        sl.append(f'<button data-lb="img/{k}{i}-800.webp" aria-label="Powiększ zdjęcie {i}"><img src="img/{k}{i}-560.webp" srcset="img/{k}{i}-360.webp 360w, img/{k}{i}-560.webp 560w, img/{k}{i}-800.webp 800w" sizes="(max-width:760px) 46vw, (max-width:1100px) 30vw, 23vw" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{typ} {naz} - zdjęcie {i}"></button>')
    nav=(f'<button class="st l" aria-label="Poprzednie zdjęcie" disabled><svg aria-hidden="true"><use href="#i-lew"/></svg></button><button class="st r" aria-label="Następne zdjęcie"><svg aria-hidden="true"><use href="#i-str"/></svg></button><span class="licz">1/{n}</span>' if n>1 else '')
    out.append(f'''   <article class="prod">
    <div class="fot" data-karuzela><div class="tor">{''.join(sl)}</div>{nav}</div>
    <div class="opis"><span class="typ">{typ}</span><h3>{naz}</h3><p class="cena">{cena}</p>{f'<p class="rata">{rata}</p>' if rata else ''}{f'<p class="gw">{gw}</p>' if gw else ''}<div class="dol"><a class="btn" href="#rehab">Do koszyka</a></div></div>
   </article>''')
K=[('k-rehab','Łóżka rehabilitacyjne','65 modeli i rozmiarów'),('k-tapic','Łóżka tapicerowane','Do sypialni'),('k-kont','Łóżka kontynentalne','Wielowarstwowa konstrukcja'),
   ('k-mat','Materace prozdrowotne','Do łóżek rehabilitacyjnych'),('k-mat2','Materace standardowe','Do sypialni'),('k-naroz','Narożniki i sofy','Do salonu'),('k-dzieci','Łóżka dla dzieci','Z barierką')]
kat=[]
for k,n,o in K:
    w,h=Image.open(f'img/{k}-480.webp').size
    kat.append(f'   <a href="#kategorie"><img src="img/{k}-480.webp" srcset="img/{k}-240.webp 240w, img/{k}-480.webp 480w" sizes="(max-width:560px) 56vw, (max-width:900px) 38vw, (max-width:1500px) 19vw, 13vw" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{n}"><h3>{n}</h3><span>{o}</span></a>')
S=[('s-classic','Łóżko kontynentalne CLASSIC','Pionowo przeszywany zagłówek','2 330 zł'),('s-europa','Łóżko kontynentalne EUROPA','Zaokrąglone, pionowe przeszycia','2 370 zł'),
   ('s-elara','Łóżko kontynentalne ELARA','Gęsto pikowany zagłówek','2 320 zł'),('s-ocean','Łóżko kontynentalne OCEAN','Wysoki zagłówek z bocznymi pasami','2 350 zł'),
   ('s-deco','Łóżko kontynentalne DECO','Zagłówek z kwadratowych paneli','2 280 zł'),('s-aura','Łóżko AURA','Zagłówek z poziomych paneli','1 950 zł')]
syp=[]
for k,n,o,c in S:
    w,h=Image.open(f'img/{k}-640.webp').size
    syp.append(f'   <article><div class="fot"><img src="img/{k}-640.webp" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{n} 160x200"></div><h3>{n}</h3><p>{o}</p><p class="cena">{c}</p></article>')
s=open('src.html',encoding='utf-8').read()
s=s.replace('{{PRODUKTY}}','\n'.join(out)).replace('{{KATEGORIE}}','\n'.join(kat)).replace('{{SYPIALNIA}}','\n'.join(syp))
s=s.replace('{{BADGE_STYLE}}',open('badge_style.part',encoding='utf-8').read().replace('<style>','').replace('</style>','').strip())
s=s.replace('{{BADGE_LINK}}',open('badge_link.part',encoding='utf-8').read().strip())
assert '{{' not in s
open('index.html','w',encoding='utf-8').write(s)
print('ok',len(s))
