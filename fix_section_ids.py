
with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', encoding='utf-8') as f:
    content = f.read()

# Add id to Puertos section
content = content.replace(
    '<section class="mb-12">\n      <div class="w-full bg-white rounded-2xl p-6 shadow',
    '<section id="section-ports" class="mb-12">\n      <div class="w-full bg-white rounded-2xl p-6 shadow',
    1
)

# Detalle de Cuotas already has id="cronograma", update nav link to match
# Consideraciones already has id="consideraciones", update nav link to match

# Fix nav href for cuotas and consideraciones
content = content.replace(
    'href="#section-cuotas">Detalle de cuota</a>',
    'href="#cronograma">Detalle de cuota</a>'
)
content = content.replace(
    'href="#section-considerations">Consideraciones importantes</a>',
    'href="#consideraciones">Consideraciones importantes</a>'
)

with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
