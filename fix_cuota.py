
filepath = r"C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

OLD = (
    '<div class="w-full max-w-4xl mx-auto p-6 bg-white rounded-2xl shadow-lg">'
    '<h3 class="text-xl font-semibold text-neutral-800 mb-2">Calcula tu cuota mensual</h3>'
    '<p class="text-sm text-neutral-500 mb-6">Selecciona el plazo que mejor se ajuste a tu presupuesto</p>'
    '<div class="mb-6"><label class="block text-sm font-medium text-neutral-700 mb-3">Cuota inicial (opcional)</label>'
    '<div class="flex flex-wrap gap-2">'
    '<button class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer bg-[#4654CD] text-white shadow-md">Sin inicial</button>'
    '<button class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer bg-neutral-100 text-neutral-700 hover:bg-neutral-200">S/275</button>'
    '<button class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer bg-neutral-100 text-neutral-700 hover:bg-neutral-200">S/550</button>'
    '<button class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer bg-neutral-100 text-neutral-700 hover:bg-neutral-200">S/824</button>'
    '</div></div>'
    '<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">'
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300 bg-white border-2 border-neutral-200 hover:border-[#4654CD] hover:shadow-lg"><div class="text-center"><p class="text-sm font-medium mb-2 text-neutral-500">12 meses</p><p class="text-xs line-through mb-1 text-neutral-400">S/249</p><p class="text-xl font-bold text-[#4654CD]">S/229</p><p class="text-xs mt-1 text-neutral-500">al mes</p></div></div>'
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300 bg-white border-2 border-neutral-200 hover:border-[#4654CD] hover:shadow-lg"><div class="text-center"><p class="text-sm font-medium mb-2 text-neutral-500">18 meses</p><p class="text-xs line-through mb-1 text-neutral-400">S/175</p><p class="text-xl font-bold text-[#4654CD]">S/159</p><p class="text-xs mt-1 text-neutral-500">al mes</p></div></div>'
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300 bg-white border-2 border-neutral-200 hover:border-[#4654CD] hover:shadow-lg"><div class="text-center"><p class="text-sm font-medium mb-2 text-neutral-500">24 meses</p><p class="text-xs line-through mb-1 text-neutral-400">S/136</p><p class="text-xl font-bold text-[#4654CD]">S/124</p><p class="text-xs mt-1 text-neutral-500">al mes</p></div></div>'
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300 bg-gradient-to-br from-[#4654CD] to-[#3644BD] text-white shadow-xl scale-105"><div class="absolute -top-2 -right-2 bg-green-500 text-white text-xs font-bold px-2 py-1 rounded-full">&#10003;</div><div class="text-center"><p class="text-sm font-medium mb-2 text-white/80">36 meses</p><p class="text-xs line-through mb-1 text-white/60">S/99</p><p class="text-xl font-bold text-white">S/89</p><p class="text-xs mt-1 text-white/80">al mes</p></div></div>'
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300 bg-white border-2 border-neutral-200 hover:border-[#4654CD] hover:shadow-lg"><div class="text-center"><p class="text-sm font-medium mb-2 text-neutral-500">48 meses</p><p class="text-xs line-through mb-1 text-neutral-400">S/79</p><p class="text-xl font-bold text-[#4654CD]">S/71</p><p class="text-xs mt-1 text-neutral-500">al mes</p></div></div>'
    '</div>'
    '<div class="mt-8 p-6 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl"><div class="text-center"><p class="text-sm text-neutral-600 mb-2">Pagar\u00edas</p><p class="line-through text-neutral-400 text-xl mb-1">S/99/mes</p><p class="text-4xl font-bold text-[#4654CD]">S/89/mes</p><p class="text-sm text-neutral-500 mt-2">durante 36 meses</p></div></div>'
    '</div>'
)

NEW = (
    '<div class="w-full max-w-4xl mx-auto p-6 rounded-2xl" style="background:var(--bg-card);border:1px solid rgba(233,30,140,0.25);box-shadow:0 0 32px rgba(233,30,140,0.08),0 8px 32px rgba(0,0,0,0.3);">'
    # Title
    '<h3 class="text-xl font-bold mb-1" style="font-family:\'Bebas Neue\',sans-serif;font-size:1.6rem;letter-spacing:1px;background:linear-gradient(90deg,#e91e8c,#ff6ec7);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Calcula tu Cuota Mensual</h3>'
    '<p class="text-sm mb-6" style="color:var(--text-muted);font-family:\'Share Tech Mono\',monospace;letter-spacing:0.5px;">// selecciona el plazo que mejor se ajuste</p>'
    # Inicial pills
    '<div class="mb-6">'
    '<label class="block text-xs font-bold mb-3" style="color:#e91e8c;font-family:\'Share Tech Mono\',monospace;letter-spacing:2px;text-transform:uppercase;">Cuota inicial (opcional)</label>'
    '<div class="flex flex-wrap gap-2">'
    '<button class="py-2 px-4 text-sm font-bold rounded-full transition-all cursor-pointer text-white" style="background:linear-gradient(90deg,#e91e8c,#c2185b);box-shadow:0 0 12px rgba(233,30,140,0.4);font-family:\'Rajdhani\',sans-serif;">Sin inicial</button>'
    '<button class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer" style="background:var(--bg-surface);color:var(--text-secondary);border:1px solid rgba(233,30,140,0.2);font-family:\'Rajdhani\',sans-serif;">S/275</button>'
    '<button class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer" style="background:var(--bg-surface);color:var(--text-secondary);border:1px solid rgba(233,30,140,0.2);font-family:\'Rajdhani\',sans-serif;">S/550</button>'
    '<button class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer" style="background:var(--bg-surface);color:var(--text-secondary);border:1px solid rgba(233,30,140,0.2);font-family:\'Rajdhani\',sans-serif;">S/824</button>'
    '</div></div>'
    # Plazo cards grid
    '<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">'
    # 12 meses
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300" style="background:var(--bg-surface);border:1px solid rgba(233,30,140,0.2);">'
    '<div class="text-center">'
    '<p class="text-xs font-bold mb-2" style="color:#e91e8c;font-family:\'Share Tech Mono\',monospace;letter-spacing:1px;">12 MESES</p>'
    '<p class="text-xs line-through mb-1" style="color:var(--text-muted);font-family:\'Share Tech Mono\',monospace;">S/249</p>'
    '<p style="font-family:\'Orbitron\',sans-serif;font-size:1.25rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 10px rgba(0,255,213,0.5);">S/229</p>'
    '<p class="text-xs mt-1" style="color:var(--text-muted);font-family:\'Rajdhani\',sans-serif;">al mes</p>'
    '</div></div>'
    # 18 meses
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300" style="background:var(--bg-surface);border:1px solid rgba(233,30,140,0.2);">'
    '<div class="text-center">'
    '<p class="text-xs font-bold mb-2" style="color:#e91e8c;font-family:\'Share Tech Mono\',monospace;letter-spacing:1px;">18 MESES</p>'
    '<p class="text-xs line-through mb-1" style="color:var(--text-muted);font-family:\'Share Tech Mono\',monospace;">S/175</p>'
    '<p style="font-family:\'Orbitron\',sans-serif;font-size:1.25rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 10px rgba(0,255,213,0.5);">S/159</p>'
    '<p class="text-xs mt-1" style="color:var(--text-muted);font-family:\'Rajdhani\',sans-serif;">al mes</p>'
    '</div></div>'
    # 24 meses
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300" style="background:var(--bg-surface);border:1px solid rgba(233,30,140,0.2);">'
    '<div class="text-center">'
    '<p class="text-xs font-bold mb-2" style="color:#e91e8c;font-family:\'Share Tech Mono\',monospace;letter-spacing:1px;">24 MESES</p>'
    '<p class="text-xs line-through mb-1" style="color:var(--text-muted);font-family:\'Share Tech Mono\',monospace;">S/136</p>'
    '<p style="font-family:\'Orbitron\',sans-serif;font-size:1.25rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 10px rgba(0,255,213,0.5);">S/124</p>'
    '<p class="text-xs mt-1" style="color:var(--text-muted);font-family:\'Rajdhani\',sans-serif;">al mes</p>'
    '</div></div>'
    # 36 meses (POPULAR - magenta highlight)
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300 scale-105" style="background:linear-gradient(135deg,rgba(233,30,140,0.25),rgba(194,24,91,0.15));border:2px solid #e91e8c;box-shadow:0 0 20px rgba(233,30,140,0.3);">'
    '<div class="absolute -top-2 -right-2 text-white text-xs font-bold px-2 py-1 rounded-full" style="background:linear-gradient(90deg,#e91e8c,#c2185b);font-family:\'Bebas Neue\',sans-serif;letter-spacing:1px;box-shadow:0 0 8px rgba(233,30,140,0.5);">TOP</div>'
    '<div class="text-center">'
    '<p class="text-xs font-bold mb-2" style="color:#ff6ec7;font-family:\'Share Tech Mono\',monospace;letter-spacing:1px;">36 MESES</p>'
    '<p class="text-xs line-through mb-1" style="color:rgba(255,110,199,0.5);font-family:\'Share Tech Mono\',monospace;">S/99</p>'
    '<p style="font-family:\'Orbitron\',sans-serif;font-size:1.25rem;font-weight:800;color:#fff;text-shadow:0 0 14px rgba(233,30,140,0.8);">S/89</p>'
    '<p class="text-xs mt-1" style="color:rgba(255,110,199,0.8);font-family:\'Rajdhani\',sans-serif;">al mes</p>'
    '</div></div>'
    # 48 meses
    '<div class="relative p-4 rounded-xl cursor-pointer transition-all duration-300" style="background:var(--bg-surface);border:1px solid rgba(233,30,140,0.2);">'
    '<div class="text-center">'
    '<p class="text-xs font-bold mb-2" style="color:#e91e8c;font-family:\'Share Tech Mono\',monospace;letter-spacing:1px;">48 MESES</p>'
    '<p class="text-xs line-through mb-1" style="color:var(--text-muted);font-family:\'Share Tech Mono\',monospace;">S/79</p>'
    '<p style="font-family:\'Orbitron\',sans-serif;font-size:1.25rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 10px rgba(0,255,213,0.5);">S/71</p>'
    '<p class="text-xs mt-1" style="color:var(--text-muted);font-family:\'Rajdhani\',sans-serif;">al mes</p>'
    '</div></div>'
    '</div>'
    # Pagarías box
    '<div class="mt-8 p-6 rounded-xl" style="background:rgba(233,30,140,0.06);border:1px solid rgba(233,30,140,0.2);">'
    '<div class="text-center">'
    '<p class="text-xs mb-2" style="color:#e91e8c;font-family:\'Share Tech Mono\',monospace;letter-spacing:2px;text-transform:uppercase;">// Pagar\u00edas</p>'
    '<p class="line-through text-xl mb-1" style="color:var(--text-muted);font-family:\'Share Tech Mono\',monospace;">S/99/mes</p>'
    '<p style="font-family:\'Orbitron\',sans-serif;font-size:2.5rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 20px rgba(0,255,213,0.6);line-height:1.1;">S/89<span style="font-size:1rem;opacity:0.7;">/mes</span></p>'
    '<p class="text-sm mt-2" style="color:var(--text-muted);font-family:\'Rajdhani\',sans-serif;">durante 36 meses</p>'
    '</div></div>'
    '</div>'
)

if OLD in content:
    content = content.replace(OLD, NEW, 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Cuota widget restyled.")
else:
    # Debug: check what's around the pagarías section
    idx = content.find('Pagar')
    if idx != -1:
        print("Found Pagar at:", idx)
        print(repr(content[idx-20:idx+100]))
    else:
        print("ERROR: OLD string not found")
