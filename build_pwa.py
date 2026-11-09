"""Genera dist/ : versión instalable (PWA) y offline de las calculadoras MSC."""
import json, pathlib, hashlib
from PIL import Image, ImageDraw
R=pathlib.Path(__file__).parent; D=R/'docs'; D.mkdir(exist_ok=True); (D/'icons').mkdir(exist_ok=True)
src=(R/'fuente'/'index.html').read_text(encoding='utf-8')
ver=hashlib.sha1(src.encode()).hexdigest()[:8]
head=('<script>window.MSC_PWA=true</script><link rel="manifest" href="manifest.webmanifest">'
 '<meta name="theme-color" content="#14181E"><meta name="apple-mobile-web-app-capable" content="yes">'
 '<meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
 '<meta name="apple-mobile-web-app-title" content="MSC Gestor Legal"><link rel="apple-touch-icon" href="icons/icon-180.png"><link rel="icon" href="icons/icon-192.png">')
reg=('<script>if("serviceWorker" in navigator){window.addEventListener("load",function(){navigator.serviceWorker.register("sw.js").catch(function(){})})}</script>')
out=src.replace('<meta charset="utf-8">','<meta charset="utf-8">'+head,1)
i=out.rindex('</body></html>');out=out[:i]+reg+out[i:]
assert out.count('MSC_PWA=true')==1 and out.endswith('</body></html>\n') or out.endswith('</body></html>')
(D/'index.html').write_text(out,encoding='utf-8')
# íconos: isotipo provisional (cuadro dorado oliva, esquina recortada, M blanca)
def icon(size,maskable=False):
    em=Image.open(R/'assets'/'logo-msc-original.png').convert('RGBA').crop((0,0,876,889))
    im=Image.new('RGBA',(size,size),(20,24,30,255)); s=int(size*(0.62 if maskable else 0.78))
    e=em.resize((s,round(s*889/876)),Image.LANCZOS); im.alpha_composite(e,((size-e.width)//2,(size-e.height)//2)); return im
for n in (180,192,512): icon(n).save(D/'icons'/f'icon-{n}.png')
icon(512,True).save(D/'icons'/'maskable-512.png')
man={"name":"MSC Gestor Legal","short_name":"MSC Gestor Legal","lang":"es-EC","start_url":"./","scope":"./","display":"standalone",
 "background_color":"#F7F5EE","theme_color":"#14181E","description":"Honorarios, consultas, pensiones, plazos y tránsito. Uso interno de Macías Sánchez Consultores.",
 "icons":[{"src":"icons/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icons/icon-512.png","sizes":"512x512","type":"image/png"},
          {"src":"icons/maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]}
(D/'manifest.webmanifest').write_text(json.dumps(man,ensure_ascii=False,indent=1),encoding='utf-8')
sw=f"""const C='msc-{ver}';const CORE=['./','./index.html','./manifest.webmanifest','./icons/icon-192.png','./icons/icon-512.png','./icons/maskable-512.png','./icons/icon-180.png'];
self.addEventListener('install',e=>{{e.waitUntil(caches.open(C).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))}});
self.addEventListener('activate',e=>{{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))}});
self.addEventListener('fetch',e=>{{const r=e.request;if(r.method!=='GET')return;
 if(r.mode==='navigate'){{e.respondWith(fetch(r).then(res=>{{const cp=res.clone();caches.open(C).then(c=>c.put('./index.html',cp));return res}}).catch(()=>caches.match('./index.html')));return}}
 const u=new URL(r.url);if(u.origin!==self.location.origin&&!/fonts\\.(googleapis|gstatic)\\.com$/.test(u.hostname))return;
 e.respondWith(caches.match(r).then(hit=>hit||fetch(r).then(res=>{{if(res.ok||res.type==='opaque'){{const cp=res.clone();caches.open(C).then(c=>c.put(r,cp))}}return res}}).catch(()=>hit)))}});
"""
(D/'sw.js').write_text(sw,encoding='utf-8')
print('dist listo, versión',ver)
