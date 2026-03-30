
with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', encoding='utf-8') as f:
    content = f.read()

# 1. Especificaciones: remove cyan bar span
OLD1 = '<span style="display:inline-block;width:3px;height:22px;background:var(--neon-cyan);border-radius:2px;"></span>\n        Especificaciones'
NEW1 = 'Especificaciones'
if OLD1 in content:
    content = content.replace(OLD1, NEW1)
    print('OK: Especificaciones span removed')
else:
    print('NOT FOUND: Especificaciones span')

# 2. Puertos y Conectividad: remove USB icon wrapper div
OLD2 = '<div class="w-10 h-10 rounded-xl bg-[rgba(0,255,213,0.1)] flex items-center justify-center">\n      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-usb w-5 h-5 text-[var(--neon-cyan)]" aria-hidden="true"><circle cx="10" cy="7" r="1"></circle><circle cx="4" cy="20" r="1"></circle><path d="M4.7 19.3 19 5"></path><path d="m21 3-3 1 2 2Z"></path><path d="M9.26 7.68 5 12l2 5"></path><path d="m10 14 5 2 3.5-3.5"></path><path d="m18 12 1-1 1 1-1 1Z"></path></svg>\n    </div>'
if OLD2 in content:
    content = content.replace(OLD2, '')
    print('OK: Puertos icon removed')
else:
    # Try finding it more loosely
    idx = content.find('lucide-usb w-5 h-5')
    if idx != -1:
        # Find the wrapping div start
        div_start = content.rfind('<div class="w-10 h-10', 0, idx)
        div_end = content.find('</div>', idx) + 6
        content = content[:div_start] + content[div_end:]
        print('OK: Puertos icon removed (loose)')
    else:
        print('NOT FOUND: Puertos icon')

# 3. Detalle de Cuotas: remove calendar icon wrapper div
idx = content.find('lucide-calendar w-5 h-5')
if idx != -1:
    div_start = content.rfind('<div class="w-10 h-10', 0, idx)
    div_end = content.find('</div>', idx) + 6
    content = content[:div_start] + content[div_end:]
    print('OK: Detalle cuotas icon removed')
else:
    print('NOT FOUND: Detalle cuotas icon')

# 4. Consideraciones importantes: remove cyan info icon wrapper
OLD4 = '<div style="padding:8px; background:var(--neon-cyan); border-radius:10px; display:flex; align-items:center; justify-content:center;">\n    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/></svg>\n  </div>'
if OLD4 in content:
    content = content.replace(OLD4, '')
    print('OK: Consideraciones icon removed')
else:
    idx = content.find('background:var(--neon-cyan); border-radius:10px; display:flex')
    if idx != -1:
        div_start = content.rfind('<div', 0, idx)
        div_end = content.find('</div>', idx) + 6
        content = content[:div_start] + content[div_end:]
        print('OK: Consideraciones icon removed (loose)')
    else:
        print('NOT FOUND: Consideraciones icon')

with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
