
with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', encoding='utf-8') as f:
    content = f.read()

# 1. Fix laptop name (h1)
OLD_H1 = '>Laptop Lenovo 15.6&quot; para estudios - Ryzen 5</h1>'
NEW_H1 = (
    '>Lenovo LOQ 15ARP9</h1>'
    '<p style="font-family:\'Rajdhani\',sans-serif;font-size:15px;color:var(--text-secondary);margin:4px 0 0 0;">'
    'Lenovo LOQ 15ARP9 R7, 16GB, 512GB SSD, 15.6&quot;</p>'
)
if OLD_H1 in content:
    content = content.replace(OLD_H1, NEW_H1)
    print('OK: title updated')
else:
    print('NOT FOUND: h1')

# 2. Fix nav links
OLD_NAV = (
    '<nav class="product-tabs">'
    '<a class="pt-link active" href="#section-gallery">Descripci\u00f3n</a>'
    '<a class="pt-link" href="#specs">Especificaciones</a>'
    '<a class="pt-link" href="#section-pricing">Cuota mensual</a>'
    '<a class="pt-link" href="#section-certifications">Certificaciones</a>'
    '</nav>'
)
NEW_NAV = (
    '<nav class="product-tabs">'
    '<a class="pt-link active" href="#section-gallery">Im\u00e1genes</a>'
    '<a class="pt-link" href="#section-pricing">Cuota mensual</a>'
    '<a class="pt-link" href="#specs">Especificaciones</a>'
    '<a class="pt-link" href="#section-ports">Puertos y conectividad</a>'
    '<a class="pt-link" href="#section-cuotas">Detalle de cuota</a>'
    '<a class="pt-link" href="#section-considerations">Consideraciones importantes</a>'
    '</nav>'
)
if OLD_NAV in content:
    content = content.replace(OLD_NAV, NEW_NAV)
    print('OK: nav updated')
else:
    # Try with encoded characters
    idx = content.find('<nav class="product-tabs">')
    end = content.find('</nav>', idx) + 6
    print('Nav found at:', idx)
    print('Current nav:', repr(content[idx:end]))

with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
