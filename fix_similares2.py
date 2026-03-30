
import re

with open(r'C:\Users\USER\Desktop\Zona gamer\BALDECASH LANDING.html', encoding='utf-8') as f:
    landing = f.read()

# ── Extraer imágenes base64 de la landing ─────────────────────────────────
def get_imgs(product_name):
    idx = landing.find(product_name)
    start = landing.rfind('{', 0, idx)
    depth = 0; i = start
    while i < len(landing):
        if landing[i] == '{': depth += 1
        elif landing[i] == '}':
            depth -= 1
            if depth == 0: obj = landing[start:i+1]; break
        i += 1
    dark  = re.search(r'imgDark:\s*"(data:image[^"]+)"', obj)
    light = re.search(r'imgLight:\s*"(data:image[^"]+)"', obj)
    return (dark.group(1) if dark else ''), (light.group(1) if light else '')

victus_dark, victus_light   = get_imgs('HP Victus 15-FB3022LA')
fb3013_dark, fb3013_light   = get_imgs('HP 15-fb3013la')
print('Images OK:', bool(victus_dark), bool(victus_light), bool(fb3013_dark), bool(fb3013_light))

# ── SVGs ──────────────────────────────────────────────────────────────────
CPU  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="8" y="8" width="8" height="8" rx="1"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M17 2v2M7 2v2M17 20v2M7 20v2M2 7h2M2 17h2M20 7h2M20 17h2"/></svg>'
RAM  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 19v-3M10 19v-3M14 19v-3M18 19v-3M8 11V9M16 11V9M12 11V9M2 15h20"/><path d="M2 7a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v1.1a2 2 0 0 0 0 3.837V17a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-5.1a2 2 0 0 0 0-3.837Z"/></svg>'
HDD  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" x2="2" y1="12" y2="12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/></svg>'
GPU  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 2v5M8 2v5M12 2v5"/><path d="M6 11h.01M10 11h.01M14 11h.01M18 11h.01M6 15h.01M10 15h.01M14 15h.01M18 15h.01"/></svg>'
MON  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg>'
EYE  = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/></svg>'
ARR  = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg>'
HEART= '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>'

def make_card(img_dark, img_light, brand, name, badges, specs, price, old_price, sub):
    badges_html = ''.join(f'<span class="badge-sim badge-recomendado">{b}</span>' for b in badges)
    specs_html  = ''.join(f'<div class="spec-item-card">{icon}<span>{txt}</span></div>' for icon,txt in specs)
    old_html    = f'<span class="price-old-card">Antes {old_price}</span>' if old_price else ''
    return (
        f'\n          <div style="flex:0 0 300px; min-width:300px; width:300px; font-size:14px;">'
        f'\n            <div class="product-card">'
        f'\n              <div class="card-image-area">'
        f'\n                <div class="card-badges">{badges_html}</div>'
        f'\n                <div class="card-actions"><button class="card-action-btn">{HEART}</button></div>'
        f'\n                <img class="card-main-img dark-img" src="{img_dark}" alt="{name}">'
        f'\n                <img class="card-main-img light-img" src="{img_light}" alt="{name}">'
        f'\n                <div class="imagen-referencial">Imagen referencial</div>'
        f'\n                <div class="card-brand-overlay"><div class="brand-name">{brand}</div><div class="product-name">{name}</div></div>'
        f'\n              </div>'
        f'\n              <div class="card-body">'
        f'\n                <div class="card-specs">{specs_html}</div>'
        f'\n                <div class="card-price-box">'
        f'\n                  <div class="price-top"><span class="price-label-card">Cuota mensual</span></div>'
        f'\n                  {old_html}'
        f'\n                  <div class="price-main"><span class="price-card">S/{price}</span><span class="per-month">/mes</span></div>'
        f'\n                  <div class="price-sub">{sub}</div>'
        f'\n                </div>'
        f'\n              </div>'
        f'\n              <div class="card-footer">'
        f'\n                <button class="btn-detalle">{EYE} Detalle</button>'
        f'\n                <button class="btn-loquiero">Lo quiero {ARR}</button>'
        f'\n              </div>'
        f'\n            </div>'
        f'\n          </div>'
    )

card_victus = make_card(
    victus_dark, victus_light, 'HP', 'HP Victus 15-FB3022LA',
    ['Recomendado', 'Más vendido'],
    [(CPU,'Ryzen 7 7445HS'),(RAM,'16GB DDR5'),(HDD,'512GB SSD'),(GPU,'RTX 4050 6GB'),(MON,'15.6" FHD 144Hz')],
    '375', 'S/449', '24 meses · inicial S/0'
)
card_fb3013 = make_card(
    fb3013_dark, fb3013_light, 'HP', 'HP 15-fb3013la',
    ['Recomendado'],
    [(CPU,'Ryzen 7 8845HS'),(RAM,'16GB DDR5'),(HDD,'1TB SSD'),(GPU,'RTX 4050 6GB'),(MON,'15.6" FHD 144Hz')],
    '383', 'S/459', '24 meses · inicial S/0'
)

# ── Reemplazar cards en detalle ───────────────────────────────────────────
with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', encoding='utf-8') as f:
    detail = f.read()

car_start_idx = detail.find('id="similaresCarousel"')
# Find opening of first card after carousel start
first_card_start = detail.find('\n\n          <!-- Card 1:', car_start_idx)
if first_card_start == -1:
    first_card_start = detail.find('\n\n          <div style="flex:0 0 300px', car_start_idx)

# Find end of last card = closing </div> of carousel minus the last card's wrapper
# We need the content between first card and closing </div>\n        </div> of carousel
carousel_tag_start = detail.rfind('<div', 0, car_start_idx+30)
depth = 0; i = carousel_tag_start
while i < len(detail):
    if detail[i:i+4] == '<div': depth += 1; i += 4
    elif detail[i:i+6] == '</div>':
        depth -= 1
        if depth == 0: carousel_end_idx = i; break
        i += 6
    else: i += 1

OLD_CARDS = detail[first_card_start:carousel_end_idx]
NEW_CARDS = card_victus + card_fb3013 + '\n        '

detail = detail[:first_card_start] + NEW_CARDS + detail[carousel_end_idx:]

with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', 'w', encoding='utf-8') as f:
    f.write(detail)
print('OK: old cards replaced with 2 HP cards in similaresCarousel')
