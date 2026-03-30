
filepath = r"C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Ruta relativa de las imágenes (URL-encoded para espacios y ñ/í)
IMG = [
    "Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/1.png",
    "Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/2.png",
    "Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/3.png",
    "Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/4.png",
    "Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/5.png",
    "Dise%C3%B1o%20sin%20t%C3%ADtulo%20(2)/6.png",
]

# 1. Imagen principal
OLD_MAIN = 'id="galleryMainImg" alt="Laptop Lenovo frontal" style="max-height:380px;max-width:100%;object-fit:contain;transition:opacity 0.25s ease;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg"'
NEW_MAIN = f'id="galleryMainImg" alt="Laptop Lenovo 1" style="max-height:380px;max-width:100%;object-fit:contain;transition:opacity 0.25s ease;" src="{IMG[0]}"'
if OLD_MAIN in content:
    content = content.replace(OLD_MAIN, NEW_MAIN)
    print("OK: main image")
else:
    print("NOT FOUND: main image")

# 2. Contador
content = content.replace(
    '<span id="galleryCounter" style="font-size:12px;font-weight:600;color:#fff;">1 / 5</span>',
    '<span id="galleryCounter" style="font-size:12px;font-weight:600;color:#fff;">1 / 6</span>'
)
print("OK: counter")

# 3. Tira de miniaturas (reemplazar el bloque completo de 5 thumbs por 6)
def thumb(i, img, active=False):
    border = '#fff' if active else 'rgba(255,255,255,0.25)'
    cls = ' active-thumb' if active else ''
    return (
        f'<div class="gallery-thumb{cls}" onclick="galleryGoto({i},this)" '
        f'style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid {border};cursor:pointer;transition:border-color 0.2s;">'
        f'<img alt="Laptop imagen {i+1}" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="{img}">'
        f'</div>'
    )

NEW_THUMBS = ''.join(thumb(i, IMG[i], i == 0) for i in range(6))

OLD_THUMBS = (
    '<div class="gallery-thumb active-thumb" onclick="galleryGoto(0,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid #fff;cursor:pointer;transition:border-color 0.2s;">'
    '<img alt="Laptop Lenovo frontal" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg"></div>'
    '<div class="gallery-thumb" onclick="galleryGoto(1,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid rgba(255,255,255,0.25);cursor:pointer;transition:border-color 0.2s;">'
    '<img alt="Laptop HP vista lateral" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad8af9ed1fbf48ea397396_hp15.png"></div>'
    '<div class="gallery-thumb" onclick="galleryGoto(2,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid rgba(255,255,255,0.25);cursor:pointer;transition:border-color 0.2s;">'
    '<img alt="Laptop ASUS en escritorio" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad78aca11478d9ed058463_laptop_asus_x515ea.jpg"></div>'
    '<div class="gallery-thumb" onclick="galleryGoto(3,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid rgba(255,255,255,0.25);cursor:pointer;transition:border-color 0.2s;">'
    '<img alt="Laptop Dell para estudios" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7ac27cd445765564b11b_Dell%201505.jpg"></div>'
    '<div class="gallery-thumb" onclick="galleryGoto(4,this)" style="width:72px;height:56px;border-radius:8px;overflow:hidden;border:2px solid rgba(255,255,255,0.25);cursor:pointer;transition:border-color 0.2s;">'
    '<img alt="Laptop Hyundai portatil" style="width:100%;height:100%;object-fit:contain;background:#1a1a1a;padding:4px;" src="https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad79b64b6011e52725b3a7_hyndai_hybook.png"></div>'
)

if OLD_THUMBS in content:
    content = content.replace(OLD_THUMBS, NEW_THUMBS)
    print("OK: thumbnails")
else:
    print("NOT FOUND: thumbnails")

# 4. JS imgs array
OLD_JS = (
    'var imgs=["https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7929bd7b580e6de7247d_Lenovo%20Chromebook%20S330.jpg",'
    '"https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad8af9ed1fbf48ea397396_hp15.png",'
    '"https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad78aca11478d9ed058463_laptop_asus_x515ea.jpg",'
    '"https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad7ac27cd445765564b11b_Dell%201505.jpg",'
    '"https://cdn.prod.website-files.com/62141f21700a64ab3f816206/64ad79b64b6011e52725b3a7_hyndai_hybook.png"];'
)
NEW_JS = 'var imgs=["' + '","'.join(IMG) + '"];'

if OLD_JS in content:
    content = content.replace(OLD_JS, NEW_JS)
    print("OK: JS array")
else:
    print("NOT FOUND: JS array")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Done.")
