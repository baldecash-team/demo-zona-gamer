
filepath = r"C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

OLD_JS = ('var imgs=["Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/1.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/2.png",'
          '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/3.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/4.png",'
          '"Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/5.png","Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/6.png"];'
          'var cur=0;function setActive(n){cur=(n+imgs.length)%imgs.length;var el=document.getElementById("galleryMainImg");'
          'el.style.opacity="0";setTimeout(function(){el.src=imgs[cur];el.style.opacity="1";},200);'
          'document.getElementById("galleryCounter").textContent=(cur+1)+" / "+imgs.length;'
          'document.querySelectorAll(".gallery-thumb").forEach(function(t,i){t.style.borderColor=i===cur?"#fff":"rgba(255,255,255,0.25)";});}'
          'window.galleryPrev=function(){setActive(cur-1);};'
          'window.galleryNext=function(){setActive(cur+1);};'
          'window.galleryGoto=function(n){setActive(n);};')

if OLD_JS not in content:
    print("NOT FOUND: JS block")
else:
    NEW_JS = (
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
    content = content.replace(OLD_JS, NEW_JS)
    print("OK: JS updated")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Done.")
