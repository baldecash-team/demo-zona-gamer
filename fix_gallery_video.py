
with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', encoding='utf-8') as f:
    content = f.read()

YOUTUBE = "https://www.youtube.com/embed/L9ntME3bffs?start=380&end=392"
PLAY_ICON = '<svg viewBox="0 0 24 24" width="28" height="28"><circle cx="12" cy="12" r="12" fill="rgba(255,0,0,0.85)"/><polygon points="10,8 10,16 17,12" fill="white"/></svg>'

# ── 1. Add iframe next to galleryMainImg ──────────────────────────────────────
OLD_IMG = '<div class="gallery-img-wrap" id="galleryImgWrap"><img id="galleryMainImg" alt="Laptop Lenovo 1" style="max-height:380px;max-width:100%;object-fit:contain;" src="Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/1.png"></div>'
NEW_IMG = (
    '<div class="gallery-img-wrap" id="galleryImgWrap">'
    '<iframe id="galleryVideo" src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen '
    'style="display:none;width:100%;height:380px;border-radius:8px;border:none;"></iframe>'
    '<img id="galleryMainImg" alt="Laptop Lenovo 1" style="max-height:380px;max-width:100%;object-fit:contain;" src="Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/1.png">'
    '</div>'
)
if OLD_IMG in content:
    content = content.replace(OLD_IMG, NEW_IMG)
    print('OK: iframe added')
else:
    print('NOT FOUND: galleryImgWrap')

# ── 2. Shift existing thumb indices (5→6, 4→5, ... 0→1) ─────────────────────
for old_i in range(5, -1, -1):
    content = content.replace(
        'onclick="galleryGoto(%d,this)"' % old_i,
        'onclick="galleryGoto(%d,this)"' % (old_i + 1)
    )
print('OK: thumb indices shifted')

# ── 3. Insert video thumb before the first (now index-1) thumb ───────────────
VIDEO_THUMB = (
    '<div class="gallery-thumb active-thumb" onclick="galleryGoto(0,this)" '
    'style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid #fff;cursor:pointer;transition:border-color 0.2s;'
    'background:#1a1a1a;display:flex;align-items:center;justify-content:center;">'
    + PLAY_ICON +
    '</div>'
)
OLD_FIRST_THUMB = '<div class="gallery-thumb active-thumb" onclick="galleryGoto(1,this)"'
NEW_FIRST_THUMB = VIDEO_THUMB + '<div class="gallery-thumb" onclick="galleryGoto(1,this)"'
if OLD_FIRST_THUMB in content:
    content = content.replace(OLD_FIRST_THUMB, NEW_FIRST_THUMB, 1)
    print('OK: video thumb inserted')
else:
    print('NOT FOUND: first thumb after shift')

# ── 4. Counter 1/6 → 1/7 ─────────────────────────────────────────────────────
content = content.replace(
    '<span id="galleryCounter" style="font-size:12px;font-weight:600;color:#fff;">1 / 6</span>',
    '<span id="galleryCounter" style="font-size:12px;font-weight:600;color:#fff;">1 / 7</span>'
)
print('OK: counter updated')

# ── 5. Update JS ──────────────────────────────────────────────────────────────
OLD_JS = (
    'var imgsDark=["Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/1.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/2.png",'
    '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/3.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/4.png",'
    '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/5.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/6.png"];'
    'var imgsLight=["Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/1.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/2.png",'
    '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/3.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/4.png",'
    '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/5.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/6.png"];'
    'function getImgs(){return document.documentElement.getAttribute("data-theme")==="light"?imgsLight:imgsDark;}'
    'var cur=0;'
    'function setActive(n){var imgs=getImgs();cur=(n+imgs.length)%imgs.length;var el=document.getElementById("galleryMainImg");'
    'el.style.opacity="0";setTimeout(function(){el.src=imgs[cur];el.style.opacity="1";},200);'
    'document.getElementById("galleryCounter").textContent=(cur+1)+" / "+imgs.length;'
    'document.querySelectorAll(".gallery-thumb").forEach(function(t,i){t.style.borderColor=i===cur?"#fff":"rgba(255,255,255,0.25)";});}'
    'function refreshGalleryTheme(){var imgs=getImgs();cur=0;'
    'document.querySelectorAll(".gallery-thumb img").forEach(function(t,i){t.src=imgs[i];});'
    'var el=document.getElementById("galleryMainImg");el.src=imgs[0];'
    'document.getElementById("galleryCounter").textContent="1 / "+imgs.length;'
    'document.querySelectorAll(".gallery-thumb").forEach(function(t,i){t.style.borderColor=i===0?"#fff":"rgba(255,255,255,0.25)";});}'
    'window.galleryPrev=function(){setActive(cur-1);};'
    'window.galleryNext=function(){setActive(cur+1);};'
    'window.galleryGoto=function(n){setActive(n);};'
    'window.galleryRefreshTheme=refreshGalleryTheme;'
)

yt_embed_autoplay = YOUTUBE + '&autoplay=1'

NEW_JS = (
    'var YOUTUBE_EMBED="' + yt_embed_autoplay + '";'
    'var imgsDark=["Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/1.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/2.png",'
    '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/3.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/4.png",'
    '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/5.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/6.png"];'
    'var imgsLight=["Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/1.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/2.png",'
    '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/3.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/4.png",'
    '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/5.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(3)/6.png"];'
    'function getImgs(){return document.documentElement.getAttribute("data-theme")==="light"?imgsLight:imgsDark;}'
    'var cur=0;var TOTAL=7;'
    'function setActive(n){cur=((n%TOTAL)+TOTAL)%TOTAL;'
    'var iframe=document.getElementById("galleryVideo");'
    'var img=document.getElementById("galleryMainImg");'
    'if(cur===0){'
    'iframe.src=YOUTUBE_EMBED;iframe.style.display="block";'
    'img.style.display="none";'
    '}else{'
    'iframe.src="";iframe.style.display="none";'
    'var imgs=getImgs();img.style.opacity="0";img.style.display="block";'
    'setTimeout(function(){img.src=imgs[cur-1];img.style.opacity="1";},200);'
    '}'
    'document.getElementById("galleryCounter").textContent=(cur+1)+" / "+TOTAL;'
    'document.querySelectorAll(".gallery-thumb").forEach(function(t,i){t.style.borderColor=i===cur?"#fff":"rgba(255,255,255,0.25)";});}'
    'function refreshGalleryTheme(){var imgs=getImgs();'
    'document.querySelectorAll(".gallery-thumb img").forEach(function(t,i){t.src=imgs[i];});'
    'var iframe=document.getElementById("galleryVideo");var img=document.getElementById("galleryMainImg");'
    'if(cur===0){iframe.src=YOUTUBE_EMBED;iframe.style.display="block";img.style.display="none";}'
    'else{var rimgs=getImgs();img.src=rimgs[cur-1];iframe.src="";iframe.style.display="none";img.style.display="block";}'
    'document.getElementById("galleryCounter").textContent=(cur+1)+" / "+TOTAL;'
    'document.querySelectorAll(".gallery-thumb").forEach(function(t,i){t.style.borderColor=i===cur?"#fff":"rgba(255,255,255,0.25)";});}'
    'window.galleryPrev=function(){setActive(cur-1);};'
    'window.galleryNext=function(){setActive(cur+1);};'
    'window.galleryGoto=function(n){setActive(n);};'
    'window.galleryRefreshTheme=refreshGalleryTheme;'
)

if OLD_JS in content:
    content = content.replace(OLD_JS, NEW_JS)
    print('OK: JS updated')
else:
    print('NOT FOUND: JS block')

with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
