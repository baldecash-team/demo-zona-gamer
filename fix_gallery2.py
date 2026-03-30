
filepath = r"C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

start = content.find('<div id="section-gallery">')
idx = start
depth = 0
while idx < len(content):
    if content[idx:idx+4] == '<div':
        depth += 1; idx += 4
    elif content[idx:idx+6] == '</div>':
        depth -= 1
        if depth == 0:
            end = idx + 6; break
        idx += 6
    else:
        idx += 1

OLD = content[start:end]

NEW = (
'<div id="section-gallery">'

# ── Product info (no card, no background) ──────────────────────────────
'<div class="px-1 pb-4">'
  '<div class="flex items-center gap-3 mb-2">'
    '<span class="px-3 py-1.5 bg-[#4654CD] text-white text-sm font-bold rounded-lg">Lenovo</span>'
    '<div class="flex items-center gap-1.5">'
      '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-star w-5 h-5 text-amber-400 fill-amber-400" aria-hidden="true"><path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"></path></svg>'
      '<span class="text-base font-bold" style="color:var(--text-primary);">4.5</span>'
      '<span class="text-sm" style="color:var(--text-muted);">(128)</span>'
    '</div>'
  '</div>'
  '<h1 class="text-2xl md:text-3xl font-bold font-[\'Baloo_2\'] leading-tight" style="background:var(--gradient-cyber);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Laptop Lenovo 15.6&quot; para estudios - Ryzen 5</h1>'
'</div>'

# ── Dark image viewer ──────────────────────────────────────────────────
'<div class="relative rounded-2xl overflow-hidden" style="background:#0c0c0c;">'

  # Color dots — top right
  '<div class="absolute top-4 right-4 flex gap-2 z-10">'
    '<button type="button" class="w-8 h-8 rounded-full border-2 transition-all cursor-pointer flex items-center justify-center border-white ring-2 ring-white/30" aria-label="Gris Grafito" style="background-color:rgb(74,74,74);">'
      '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"></path></svg>'
    '</button>'
    '<button type="button" class="w-8 h-8 rounded-full border-2 transition-all cursor-pointer border-neutral-600 hover:border-white" aria-label="Plata" style="background-color:rgb(192,192,192);"></button>'
    '<button type="button" class="w-8 h-8 rounded-full border-2 transition-all cursor-pointer border-neutral-600 hover:border-white" aria-label="Negro" style="background-color:rgb(26,26,26);"></button>'
  '</div>'

  # Main image area
  '<div class="relative flex items-center justify-center" style="min-height:440px;padding:48px 88px;">'

    # Prev arrow
    '<button onclick="galleryPrev()" class="absolute left-4 top-1/2 -translate-y-1/2 z-10 flex items-center justify-center transition-all" style="width:48px;height:48px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);border-radius:50%;color:#fff;font-size:22px;cursor:pointer;" onmouseover="this.style.background=\'rgba(255,255,255,0.18)\'" onmouseout="this.style.background=\'rgba(255,255,255,0.08)\'">'
      '<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>'
    '</button>'

    # Main image
    '<img id="galleryMainImg" alt="Laptop Lenovo frontal" style="max-height:380px;max-width:100%;object-fit:contain;transition:opacity 0.25s ease;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg">'

    # Next arrow
    '<button onclick="galleryNext()" class="absolute right-4 top-1/2 -translate-y-1/2 z-10 flex items-center justify-center transition-all" style="width:48px;height:48px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);border-radius:50%;color:#fff;font-size:22px;cursor:pointer;" onmouseover="this.style.background=\'rgba(255,255,255,0.18)\'" onmouseout="this.style.background=\'rgba(255,255,255,0.08)\'">'
      '<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>'
    '</button>'

    # "Imagen referencial" badge bottom-left
    '<div class="absolute bottom-4 left-4" style="background:rgba(0,0,0,0.55);backdrop-filter:blur(6px);border-radius:8px;padding:5px 12px;">'
      '<span style="font-size:10px;text-transform:uppercase;letter-spacing:1.5px;color:rgba(255,255,255,0.7);">Imagen referencial</span>'
    '</div>'

    # Counter badge bottom-right
    '<div class="absolute bottom-4 right-4" style="background:rgba(0,0,0,0.55);backdrop-filter:blur(6px);border-radius:8px;padding:5px 12px;">'
      '<span id="galleryCounter" style="font-size:12px;font-weight:600;color:#fff;">1 / 5</span>'
    '</div>'

  '</div>'

  # Bottom thumbnail strip
  '<div class="flex justify-center gap-3 pb-5 px-6">'
    '<div class="gallery-thumb active-thumb" onclick="galleryGoto(0,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid #fff;cursor:pointer;transition:border-color 0.2s;">'
      '<img alt="Laptop Lenovo frontal" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg">'
    '</div>'
    '<div class="gallery-thumb" onclick="galleryGoto(1,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid rgba(255,255,255,0.25);cursor:pointer;transition:border-color 0.2s;">'
      '<img alt="Laptop HP vista lateral" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad8af9ed1fbf48ea397396_hp15.png">'
    '</div>'
    '<div class="gallery-thumb" onclick="galleryGoto(2,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid rgba(255,255,255,0.25);cursor:pointer;transition:border-color 0.2s;">'
      '<img alt="Laptop ASUS en escritorio" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad78aca11478d9ed058463_laptop_asus_x515ea.jpg">'
    '</div>'
    '<div class="gallery-thumb" onclick="galleryGoto(3,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid rgba(255,255,255,0.25);cursor:pointer;transition:border-color 0.2s;">'
      '<img alt="Laptop Dell para estudios" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7ac27cd445765564b11b_Dell%201505.jpg">'
    '</div>'
    '<div class="gallery-thumb" onclick="galleryGoto(4,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid rgba(255,255,255,0.25);cursor:pointer;transition:border-color 0.2s;">'
      '<img alt="Laptop Hyundai portatil" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad79b64b6011e52725b3a7_hyndai_hybook.png">'
    '</div>'
  '</div>'

'</div>'  # end dark viewer

# Gallery JS
'<script>'
'(function(){'
'var imgs=["https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg","https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad8af9ed1fbf48ea397396_hp15.png","https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad78aca11478d9ed058463_laptop_asus_x515ea.jpg","https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7ac27cd445765564b11b_Dell%201505.jpg","https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad79b64b6011e52725b3a7_hyndai_hybook.png"];'
'var cur=0;'
'function setActive(n){'
  'cur=(n+imgs.length)%imgs.length;'
  'var el=document.getElementById("galleryMainImg");'
  'el.style.opacity="0";'
  'setTimeout(function(){el.src=imgs[cur];el.style.opacity="1";},200);'
  'document.getElementById("galleryCounter").textContent=(cur+1)+" / "+imgs.length;'
  'document.querySelectorAll(".gallery-thumb").forEach(function(t,i){'
    't.style.borderColor=i===cur?"#fff":"rgba(255,255,255,0.25)";'
  '});'
'}'
'window.galleryPrev=function(){setActive(cur-1);};'
'window.galleryNext=function(){setActive(cur+1);};'
'window.galleryGoto=function(n){setActive(n);};'
'})();'
'</script>'

'</div>'  # end section-gallery
)

content = content[:start] + NEW + content[end:]
with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("SUCCESS")
