(function(){
var d=document;function po(f){if(d.readyState==='complete')setTimeout(f,150);else addEventListener('load',function(){setTimeout(f,150)})}
// menu mobilne
var b=d.querySelector('.burger'),p=d.getElementById('panel');
if(b&&p){b.addEventListener('click',function(){var o=p.classList.toggle('otw');b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Zamknij menu':'Otwórz menu');d.body.style.overflow=o?'hidden':''});
 p.addEventListener('click',function(e){if(e.target.closest('a')){p.classList.remove('otw');b.setAttribute('aria-expanded','false');d.body.style.overflow=''}})}
// przeciąganie myszą
function ciagnij(el){var x0,s0,ruch=false,wcis=false;
 el.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse')return;wcis=true;ruch=false;x0=e.clientX;s0=el.scrollLeft});
 el.addEventListener('pointermove',function(e){if(!wcis)return;var dx=e.clientX-x0;if(Math.abs(dx)>5){ruch=true;el.classList.add('ciag')}if(ruch){el.scrollLeft=s0-dx;e.preventDefault()}});
 function kon(){if(!wcis)return;wcis=false;if(ruch){el.classList.remove('ciag');var w=el.firstElementChild?el.firstElementChild.getBoundingClientRect().width:el.clientWidth;var g=parseFloat(getComputedStyle(el).columnGap)||0;el.scrollTo({left:Math.round(el.scrollLeft/(w+g))*(w+g),behavior:'smooth'})}}
 el.addEventListener('pointerup',kon);el.addEventListener('pointerleave',kon);
 el.addEventListener('click',function(e){if(ruch){e.preventDefault();e.stopPropagation();ruch=false}},true);
 el.addEventListener('dragstart',function(e){e.preventDefault()})}
// rzędy z strzałkami
d.querySelectorAll('[data-rzad]').forEach(function(r){ciagnij(r);var s=d.querySelector('[data-strz="'+r.dataset.rzad+'"]');if(!s)return;var bt=s.querySelectorAll('button');
 function krok(){var c=r.firstElementChild;return c?c.getBoundingClientRect().width+(parseFloat(getComputedStyle(r).columnGap)||0):r.clientWidth}
 function stan(){bt[0].disabled=r.scrollLeft<4;bt[1].disabled=r.scrollLeft+r.clientWidth>=r.scrollWidth-4}
 bt[0].addEventListener('click',function(){r.scrollBy({left:-krok(),behavior:'smooth'})});bt[1].addEventListener('click',function(){r.scrollBy({left:krok(),behavior:'smooth'})});
 r.addEventListener('scroll',stan,{passive:true});addEventListener('resize',stan);po(stan)});
// karuzele w kartach
d.querySelectorAll('[data-karuzela]').forEach(function(k){var t=k.querySelector('.tor'),l=k.querySelector('.st.l'),r=k.querySelector('.st.r'),c=k.querySelector('.licz'),n=t.children.length;ciagnij(t);
 function i(){return Math.round(t.scrollLeft/t.clientWidth)}
 function stan(){var x=i();if(c)c.textContent=(x+1)+'/'+n;if(l)l.disabled=x<=0;if(r)r.disabled=x>=n-1}
 if(l)l.addEventListener('click',function(){t.scrollBy({left:-t.clientWidth,behavior:'smooth'})});
 if(r)r.addEventListener('click',function(){t.scrollBy({left:t.clientWidth,behavior:'smooth'})});
 t.addEventListener('scroll',stan,{passive:true})});
// lightbox
var lb=d.querySelector('.lb'),li=lb.querySelector('img');
d.addEventListener('click',function(e){var x=e.target.closest('[data-lb]');if(!x)return;var im=x.querySelector('img');li.src=x.dataset.lb;li.alt=im?im.alt:'';lb.classList.add('otw');lb.querySelector('button').focus()});
function zamk(){lb.classList.remove('otw');li.removeAttribute('src')}
lb.addEventListener('click',function(e){if(e.target!==li)zamk()});d.addEventListener('keydown',function(e){if(e.key==='Escape')zamk()});
// temat formularza
d.querySelectorAll('[data-temat]').forEach(function(a){a.addEventListener('click',function(){var s=d.querySelector('select[name=temat]');if(s)s.value=a.dataset.temat})});
// formularz pokazowy
var f=d.querySelector('form.zap');if(f)f.addEventListener('submit',function(e){e.preventDefault();var i=f.querySelector('.info');i.hidden=false});
// mapa przy przewinięciu
var m=d.querySelector('[data-mapa]');
if(m&&'IntersectionObserver' in window){var io=new IntersectionObserver(function(en){if(en[0].isIntersecting){io.disconnect();var fr=d.createElement('iframe');fr.src=m.dataset.mapa;fr.title='Mapa dojazdu do ERMEDIC';fr.loading='lazy';fr.referrerPolicy='no-referrer-when-downgrade';m.appendChild(fr)}},{rootMargin:'300px'});io.observe(m)}
})();
