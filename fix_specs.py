
filepath = r"C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add spec-card CSS after .cuota-card-top:hover rule
OLD_CSS = ".cuota-card:hover { border-color: var(--neon-cyan) !important; box-shadow: 0 0 16px rgba(0,255,213,0.2); }\n.cuota-card-top:hover { border-color: var(--neon-cyan) !important; box-shadow: 0 0 24px rgba(0,255,213,0.35); }"

NEW_CSS = """.cuota-card:hover { border-color: var(--neon-cyan) !important; box-shadow: 0 0 16px rgba(0,255,213,0.2); }
.cuota-card-top:hover { border-color: var(--neon-cyan) !important; box-shadow: 0 0 24px rgba(0,255,213,0.35); }
/* ===== SPEC CARDS ===== */
.spec-card {
  position: relative; background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.08); border-radius: 12px;
  padding: 20px; cursor: pointer;
  transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}
.spec-card::before, .spec-card::after {
  content: ''; position: absolute; width: 14px; height: 14px;
  transition: opacity 0.25s ease; opacity: 0.4;
}
.spec-card::before { top: 9px; left: 9px; border-top: 2px solid var(--neon-cyan); border-left: 2px solid var(--neon-cyan); }
.spec-card::after { bottom: 9px; right: 9px; border-bottom: 2px solid var(--neon-cyan); border-right: 2px solid var(--neon-cyan); }
.spec-card:hover { transform: translateY(-3px); border-color: rgba(0,255,213,0.4); box-shadow: 0 0 20px rgba(0,255,213,0.15), 0 8px 24px rgba(0,0,0,0.4); }
.spec-card:hover::before, .spec-card:hover::after { opacity: 1; }
.spec-card-icon { width: 40px; height: 40px; border-radius: 8px; background: rgba(0,255,213,0.08); border: 1px solid rgba(0,255,213,0.2); display: flex; align-items: center; justify-content: center; color: var(--neon-cyan); flex-shrink: 0; }
.spec-card-title { font-family: 'Rajdhani', sans-serif; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: var(--text-primary); }
.spec-card-divider { height: 1px; background: rgba(255,255,255,0.06); margin: 12px 0; }
.spec-row { display: flex; align-items: center; justify-content: space-between; padding: 3px 0; }
.spec-row-label { font-size: 13px; color: var(--text-muted); font-family: 'Rajdhani', sans-serif; }
.spec-row-value { font-size: 13px; font-weight: 600; color: var(--text-primary); font-family: 'Rajdhani', sans-serif; text-align: right; }
.spec-row-value.primary { color: var(--neon-cyan); }
[data-theme="light"] .spec-card { border-color: rgba(0,0,0,0.08); }
[data-theme="light"] .spec-card:hover { border-color: rgba(0,179,150,0.4); box-shadow: 0 0 20px rgba(0,179,150,0.12), 0 8px 24px rgba(0,0,0,0.1); }
[data-theme="light"] .spec-card-icon { background: rgba(0,179,150,0.08); border-color: rgba(0,179,150,0.2); }
[data-theme="light"] .spec-card-divider { background: rgba(0,0,0,0.08); }"""

if OLD_CSS in content:
    content = content.replace(OLD_CSS, NEW_CSS)
    print("OK: CSS added")
else:
    print("NOT FOUND: CSS insertion point")

# 2. Replace the specs section heading + grid
OLD_HEADING = (
    '<!-- ===== SPECS SECTION ===== -->\n'
    '    <section id="specs" class="mt-16 mb-12">\n'
    '      <h2 class="text-xl font-bold text-neutral-900 mb-6" style="font-family: \'Rajdhani\', sans-serif; font-size:24px;">\n'
    '        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#4654CD" stroke-width="2" style="display:inline; vertical-align:middle; margin-right:8px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>\n'
    '        Especificaciones\n'
    '      </h2>'
)

NEW_HEADING = (
    '<!-- ===== SPECS SECTION ===== -->\n'
    '    <section id="specs" class="mt-16 mb-12">\n'
    '      <h2 class="mb-6" style="font-family:\'Rajdhani\',sans-serif;font-size:22px;font-weight:700;color:var(--text-primary);display:flex;align-items:center;gap:10px;">\n'
    '        <span style="display:inline-block;width:3px;height:22px;background:var(--neon-cyan);border-radius:2px;"></span>\n'
    '        Especificaciones\n'
    '      </h2>'
)

if OLD_HEADING in content:
    content = content.replace(OLD_HEADING, NEW_HEADING)
    print("OK: heading replaced")
else:
    print("NOT FOUND: heading")

# SVG icons (reusable snippets)
CPU_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20v2"/><path d="M12 2v2"/><path d="M17 20v2"/><path d="M17 2v2"/><path d="M2 12h2"/><path d="M2 17h2"/><path d="M2 7h2"/><path d="M20 12h2"/><path d="M20 17h2"/><path d="M20 7h2"/><path d="M7 20v2"/><path d="M7 2v2"/><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="8" y="8" width="8" height="8" rx="1"/></svg>'
MEM_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 19v-3"/><path d="M10 19v-3"/><path d="M14 19v-3"/><path d="M18 19v-3"/><path d="M8 11V9"/><path d="M16 11V9"/><path d="M12 11V9"/><path d="M2 15h20"/><path d="M2 7a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v1.1a2 2 0 0 0 0 3.837V17a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-5.1a2 2 0 0 0 0-3.837Z"/></svg>'
HDD_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" x2="2" y1="12" y2="12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/><line x1="6" x2="6.01" y1="16" y2="16"/><line x1="10" x2="10.01" y1="16" y2="16"/></svg>'
MON_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg>'
BAT_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M 22 14 L 22 10"/><rect x="2" y="6" width="16" height="12" rx="2"/></svg>'
WIFI_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h.01"/><path d="M2 8.82a15 15 0 0 1 20 0"/><path d="M5 12.859a10 10 0 0 1 14 0"/><path d="M8.5 16.429a5 5 0 0 1 7 0"/></svg>'

def card(icon_svg, title, rows):
    rows_html = ""
    for label, value, is_primary in rows:
        cls = ' primary' if is_primary else ''
        rows_html += f'<div class="spec-row"><span class="spec-row-label">{label}</span><span class="spec-row-value{cls}">{value}</span></div>'
    return (
        f'<div class="spec-card">'
        f'<div class="flex items-center gap-3 mb-3">'
        f'<div class="spec-card-icon">{icon_svg}</div>'
        f'<span class="spec-card-title">{title}</span>'
        f'</div>'
        f'<div class="spec-card-divider"></div>'
        f'<div class="space-y-1">{rows_html}</div>'
        f'</div>'
    )

PROCESADOR = card(CPU_SVG, "Procesador", [
    ("Procesador", "AMD Ryzen 5 7520U", True),
    ("Núcleos", "4 núcleos / 8 hilos", False),
    ("Velocidad", "Hasta 4.3 GHz", False),
    ("Cache", "4MB L3", False),
])
MEMORIA = card(MEM_SVG, "Memoria", [
    ("RAM", "8GB DDR5", True),
    ("Tipo", "DDR5-4800", False),
    ("Expandible", "Hasta 16GB", False),
])
ALMACENAMIENTO = card(HDD_SVG, "Almacenamiento", [
    ("SSD", "256GB NVMe", True),
    ("Tipo", "M.2 2242 PCIe 4.0", False),
    ("Expandible", "Sí, slot disponible", False),
])
PANTALLA = card(MON_SVG, "Pantalla", [
    ("Tamaño", "15.6 pulgadas", True),
    ("Resolución", "1920 x 1080 (Full HD)", False),
    ("Panel", "TN Anti-reflejo", False),
    ("Brillo", "220 nits", False),
])
BATERIA = card(BAT_SVG, "Batería", [
    ("Capacidad", "38Wh", True),
    ("Duración", "Hasta 6 horas", False),
    ("Carga rápida", "65W", False),
])
CONECTIVIDAD = card(WIFI_SVG, "Conectividad", [
    ("WiFi", "WiFi 6 (802.11ax)", True),
    ("Bluetooth", "5.1", False),
    ("Cámara", "720p con privacidad", False),
])

NEW_GRID = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-4">{PROCESADOR}{MEMORIA}{ALMACENAMIENTO}{PANTALLA}{BATERIA}{CONECTIVIDAD}</div>'

# Find and replace the old spec grid
import re
# The old grid starts with <div class="grid grid-cols-1 md:grid-cols-2 gap-4"> inside the specs section
# and ends before </section>
specs_start = content.find('<!-- ===== SPECS SECTION ===== -->')
specs_end = content.find('<!-- ===== PUERTOS Y CONECTIVIDAD ===== -->')

if specs_start == -1 or specs_end == -1:
    print("NOT FOUND: specs section boundaries")
else:
    specs_block = content[specs_start:specs_end]
    grid_start = specs_block.find('<div class="grid grid-cols-1 md:grid-cols-2 gap-4">')
    if grid_start == -1:
        print("NOT FOUND: specs grid")
    else:
        # Find the closing </section> tag after the grid
        section_close = specs_block.rfind('</section>')
        if section_close == -1:
            print("NOT FOUND: </section>")
        else:
            old_grid_block = specs_block[grid_start:section_close]
            new_section = (
                specs_block[:grid_start]
                + NEW_GRID
                + '\n    </section>\n\n    '
            )
            content = content[:specs_start] + new_section + content[specs_end:]
            print("OK: specs grid replaced")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Done.")
