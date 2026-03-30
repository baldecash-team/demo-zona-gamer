#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restructures baldecash-detalle-pack-gamer.html by replacing the <main> section
(lines 301-549) with new content while preserving base64 images.
"""

import os
import sys

file_path = r"C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-pack-gamer.html"

print(f"Reading file: {file_path}")
print(f"File size: {os.path.getsize(file_path):,} bytes")

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Extract base64 srcs from lines 319 and 320 (index 318 and 319)
line_dark = lines[318]   # line 319 (0-indexed: 318) - packImgDark
line_light = lines[319]  # line 320 (0-indexed: 319) - packImgLight

print(f"Line 319 (dark): {line_dark[:120]}...")
print(f"Line 320 (light): {line_light[:120]}...")

# Extract src="..." from each line
def extract_src(line):
    marker = 'src="'
    start = line.find(marker)
    if start == -1:
        raise ValueError(f"Could not find src= in line: {line[:200]}")
    start += len(marker)
    end = line.find('"', start)
    if end == -1:
        raise ValueError(f"Could not find closing quote for src in line: {line[:200]}")
    return line[start:end]

dark_src = extract_src(line_dark)
light_src = extract_src(line_light)

print(f"dark_src length: {len(dark_src)}")
print(f"light_src length: {len(light_src)}")
print(f"dark_src starts with: {dark_src[:60]}")
print(f"light_src starts with: {light_src[:60]}")

# Split content
# before_main: lines 1-300 (indices 0-299)
# after_main: lines 550-end (indices 549 onwards)
before_main_lines = lines[0:300]
after_main_lines = lines[549:]

before_main = ''.join(before_main_lines)
after_main = ''.join(after_main_lines)

print(f"before_main lines: {len(before_main_lines)}")
print(f"after_main lines: {len(after_main_lines)}")

# ============================================================
# NEW CSS to add before </style> in before_main
# ============================================================
new_css = """
/* ===== GALLERY VIEWER ===== */
.gallery-viewer { background: transparent; }
[data-theme="light"] .gallery-viewer { background: transparent; }
.gallery-thumb { flex: 0 0 80px; width: 80px; height: 60px; border-radius: 8px; overflow: hidden; border: 2px solid #e5e7eb; cursor: pointer; transition: border-color 0.2s; display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 3px; background: var(--bg-card); }
.gallery-thumb.active-thumb { border-color: #4654CD; box-shadow: 0 0 0 2px rgba(70,84,205,0.2); }
.gallery-thumb:hover { border-color: #4654CD; }
.gallery-thumb span { font-size: 9px; font-weight: 600; color: var(--text-secondary); font-family: 'Rajdhani', sans-serif; }
/* ===== SPEC ROWS ===== */
.spec-row { display: flex; align-items: flex-start; justify-content: space-between; padding: 6px 0; gap: 12px; }
.spec-row-label { font-size: 12px; color: var(--text-muted); font-family: 'Rajdhani', sans-serif; flex-shrink: 0; min-width: 80px; }
.spec-row-value { font-size: 13px; font-weight: 600; color: var(--text-primary); font-family: 'Rajdhani', sans-serif; text-align: right; }
.spec-row-value.primary { color: var(--neon-cyan); }
/* ===== CONSIDERACIONES ===== */
.consid-item { transition: transform 0.2s; }
.consid-item:hover { transform: translateX(4px); }
/* ===== SIMILAR PACK CARD ===== */
.similar-pack-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; padding: 20px; cursor: pointer; transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s; flex: 0 0 260px; text-decoration: none; display: block; }
.similar-pack-card:hover { transform: translateY(-4px); border-color: rgba(0,255,213,0.4); box-shadow: 0 0 20px rgba(0,255,213,0.12), 0 8px 24px rgba(0,0,0,0.3); }
/* ===== BOTTOM NAV ===== */
.bottom-nav { display: none; position: fixed; bottom: 0; left: 0; right: 0; z-index: 200; background: var(--bg-card); border-top: 1px solid var(--border); backdrop-filter: blur(12px); }
[data-theme="light"] .bottom-nav { background: #fff; }
.bottom-nav-inner { display: flex; justify-content: space-around; padding: 8px 0 4px; max-width: 480px; margin: 0 auto; }
.bottom-nav a { display: flex; flex-direction: column; align-items: center; gap: 3px; padding: 6px 12px; font-size: 10px; font-family: 'Rajdhani', sans-serif; font-weight: 600; color: var(--text-muted); text-decoration: none; border-radius: 8px; transition: color 0.2s; }
.bottom-nav a.active, .bottom-nav a:hover { color: var(--neon-purple); }
.bottom-nav svg { width: 20px; height: 20px; }
@media (max-width: 1024px) { .bottom-nav { display: block; } .detail-main { padding-bottom: 80px !important; } }
.product-font { font-family: 'Rajdhani', sans-serif; }
[data-theme="dark"] #cronogramaWidget { background: var(--bg-card) !important; border-color: var(--border) !important; }
[data-theme="dark"] #cronogramaWidget .bg-neutral-50 { background: var(--bg-surface) !important; }
[data-theme="dark"] #cronogramaWidget .border-neutral-200 { border-color: var(--border) !important; }
[data-theme="dark"] #cronogramaWidget .text-neutral-500, [data-theme="dark"] #cronogramaWidget .text-neutral-600 { color: var(--text-secondary) !important; }
[data-theme="dark"] #cronogramaWidget .text-neutral-700, [data-theme="dark"] #cronogramaWidget .text-neutral-900 { color: var(--text-primary) !important; }
[data-theme="dark"] #cronogramaWidget .border-t { border-color: var(--border) !important; }
"""

# Add CSS before </style> in before_main
old_style_close = "@media(max-width:768px){.pack-img-wrap{min-height:280px;}}"
if old_style_close not in before_main:
    print("WARNING: Could not find the CSS marker. Falling back to inserting before </style>")
    new_before_main = before_main.replace('</style>', new_css + '\n</style>', 1)
else:
    new_before_main = before_main.replace(
        old_style_close,
        old_style_close + new_css + '\n',
        1
    )

# ============================================================
# NEW MAIN CONTENT
# ============================================================
new_main_raw = """<!-- MAIN CONTENT -->
<main class="detail-main product-font" id="galeria">
  <div class="max-w-[1280px] mx-auto px-4 sm:px-6 lg:px-8">

    <!-- Breadcrumb -->
    <nav class="flex items-center gap-2 text-sm mb-6 flex-wrap" style="font-family:'Rajdhani',sans-serif;">
      <a href="BALDECASH LANDING.html" class="text-neutral-500 hover:text-blue-600 transition" style="text-decoration:none;">Inicio</a>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-neutral-400"><path d="m9 18 6-6-6-6"/></svg>
      <a href="BALDECASH LANDING.html#packs" class="text-neutral-500 hover:text-blue-600 transition" style="text-decoration:none;">Packs</a>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-neutral-400"><path d="m9 18 6-6-6-6"/></svg>
      <span style="color:var(--text-primary);font-weight:600;">Pack Pro Gamer</span>
    </nav>

    <!-- 2-column layout -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start">

      <!-- LEFT: Gallery -->
      <div id="section-gallery" class="order-2 lg:order-1">
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:20px;overflow:hidden;">
          <div class="p-5 pb-0 relative z-10">
            <div class="flex items-center gap-3 mb-2 flex-wrap">
              <span style="display:inline-block;padding:5px 14px;background:var(--neon-cyan);color:#0a0a0a;font-size:13px;font-weight:700;border-radius:8px;font-family:'Rajdhani',sans-serif;">&#127918; Pack Gaming</span>
              <span style="display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:700;color:#f5b070;font-family:'Rajdhani',sans-serif;">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="#f59e0b" stroke="#f59e0b" stroke-width="1"><path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/></svg>
                4.8 <span style="color:var(--text-muted);font-weight:400;">(234)</span>
              </span>
              <span style="display:inline-flex;align-items:center;gap:5px;padding:4px 12px;background:rgba(0,255,127,0.1);border:1px solid rgba(0,255,127,0.25);border-radius:8px;font-size:12px;font-weight:700;color:var(--neon-green);font-family:'Rajdhani',sans-serif;">&#127381; M&aacute;s Vendido</span>
            </div>
            <h1 class="text-2xl md:text-3xl font-bold leading-tight" style="font-family:'Rajdhani',sans-serif;font-weight:700;background:linear-gradient(90deg,var(--neon-purple) 0%,var(--neon-cyan) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:6px;">Pack Pro Gamer &mdash; Laptop + 4 Accesorios</h1>
            <p class="mt-1 text-sm" style="font-family:'Rajdhani',sans-serif;color:var(--text-secondary);">Laptop Legion 5 Pro &middot; Mouse Logitech G203 &middot; Teclado RGB &middot; Aud&iacute;fonos 7.1 &middot; Pad XL</p>
          </div>
          <div class="relative rounded-2xl overflow-hidden gallery-viewer">
            <div class="relative flex items-center justify-center" style="min-height:500px;padding:20px 28px;">
              <div style="display:flex;align-items:center;justify-content:center;width:100%;height:100%;position:relative;">
                <img id="packImgDark" class="dark-img" src="DARK_SRC_PLACEHOLDER" alt="Pack Pro Gamer - modo oscuro" style="max-height:460px;max-width:100%;object-fit:contain;transition:opacity 0.3s ease;">
                <img id="packImgLight" class="light-img" src="LIGHT_SRC_PLACEHOLDER" alt="Pack Pro Gamer - modo claro" style="max-height:460px;max-width:100%;object-fit:contain;transition:opacity 0.3s ease;">
              </div>
              <div class="absolute bottom-4 left-4" style="background:rgba(0,0,0,0.55);backdrop-filter:blur(6px);border-radius:8px;padding:5px 12px;">
                <span style="font-size:10px;text-transform:uppercase;letter-spacing:1.5px;color:rgba(255,255,255,0.7);">Imagen referencial</span>
              </div>
            </div>
            <div class="px-4 py-3 border-t" style="border-color:var(--border);">
              <div class="flex gap-2 justify-center flex-wrap">
                <div class="gallery-thumb active-thumb">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--neon-cyan);"><path d="M18 5a2 2 0 0 1 2 2v8.526a2 2 0 0 0 .212.897l1.068 2.127a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45l1.068-2.127A2 2 0 0 0 4 15.526V7a2 2 0 0 1 2-2z"/><path d="M20.054 15.987H3.946"/></svg>
                  <span>Laptop</span>
                </div>
                <div class="gallery-thumb">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--neon-purple);"><rect x="5" y="2" width="14" height="20" rx="7"/><path d="M12 2v8"/><path d="M5 10h14"/></svg>
                  <span>Mouse</span>
                </div>
                <div class="gallery-thumb">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--neon-orange);"><rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M8 14h8"/></svg>
                  <span>Teclado</span>
                </div>
                <div class="gallery-thumb">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--neon-green);"><path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/></svg>
                  <span>Aud&iacute;fonos</span>
                </div>
                <div class="gallery-thumb">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:#f5b070;"><rect x="2" y="8" width="20" height="10" rx="2"/><path d="M8 8V6a4 4 0 0 1 8 0v2"/></svg>
                  <span>Pad XL</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- RIGHT: Pricing -->
      <div class="order-1 lg:order-2 lg:sticky lg:top-[168px] space-y-6">
        <div id="section-pricing" class="space-y-4">
          <div class="w-full p-6 rounded-2xl" style="background:var(--bg-card);border:1px solid rgba(255,255,255,0.12);box-shadow:0 0 32px rgba(255,255,255,0.04),0 8px 32px rgba(0,0,0,0.3);">
            <h3 class="text-xl mb-1" style="font-family:'Rajdhani',sans-serif;font-size:20px;letter-spacing:0;color:var(--text-primary);font-weight:700;">Calcula tu cuota mensual</h3>
            <p class="mb-6" style="color:var(--text-secondary);font-family:'Rajdhani',sans-serif;font-size:0.85rem;">Selecciona el plazo que mejor se ajuste a tu presupuesto</p>
            <div class="mb-6">
              <label class="block text-xs font-bold mb-3" style="color:var(--text-primary);font-family:'Rajdhani',sans-serif;">Cuota inicial (opcional)</label>
              <div class="flex flex-wrap gap-2">
                <button id="inicialBtn0" onclick="selectInicial(0,this)" class="py-2 px-4 text-sm font-bold rounded-full transition-all cursor-pointer" style="background:var(--neon-cyan);border:1px solid var(--neon-cyan);font-family:'Rajdhani',sans-serif;box-shadow:0 0 10px rgba(0,255,213,0.4);color:#0a0a0a;">Sin inicial</button>
                <button id="inicialBtn1" onclick="selectInicial(299,this)" class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer" style="background:var(--bg-surface);color:var(--text-secondary);border:1px solid rgba(255,255,255,0.12);font-family:'Rajdhani',sans-serif;">S/299</button>
                <button id="inicialBtn2" onclick="selectInicial(599,this)" class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer" style="background:var(--bg-surface);color:var(--text-secondary);border:1px solid rgba(255,255,255,0.12);font-family:'Rajdhani',sans-serif;">S/599</button>
                <button id="inicialBtn3" onclick="selectInicial(899,this)" class="py-2 px-4 text-sm font-medium rounded-full transition-all cursor-pointer" style="background:var(--bg-surface);color:var(--text-secondary);border:1px solid rgba(255,255,255,0.12);font-family:'Rajdhani',sans-serif;">S/899</button>
              </div>
            </div>
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
              <div class="cuota-card relative p-4 rounded-xl cursor-pointer transition-all duration-300" onclick="selectCuotaCard(12,this)" style="background:var(--bg-surface);border:1px solid rgba(255,255,255,0.1);">
                <div class="text-center">
                  <p class="text-xs mb-2" style="color:var(--text-primary);font-family:'Share Tech Mono',monospace;letter-spacing:1px;">12 meses</p>
                  <p class="text-xs line-through mb-1" style="color:rgba(255,255,255,0.5);font-family:'Share Tech Mono',monospace;" id="old12">S/149</p>
                  <p id="val12" style="font-family:'Orbitron',sans-serif;font-size:1.25rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 10px rgba(0,255,213,0.5);">S/129</p>
                  <p class="text-xs mt-1" style="color:rgba(255,255,255,0.7);font-family:'Rajdhani',sans-serif;">al mes</p>
                </div>
              </div>
              <div class="cuota-card relative p-4 rounded-xl cursor-pointer transition-all duration-300" onclick="selectCuotaCard(18,this)" style="background:var(--bg-surface);border:1px solid rgba(255,255,255,0.1);">
                <div class="text-center">
                  <p class="text-xs mb-2" style="color:var(--text-primary);font-family:'Share Tech Mono',monospace;letter-spacing:1px;">18 meses</p>
                  <p class="text-xs line-through mb-1" style="color:rgba(255,255,255,0.5);font-family:'Share Tech Mono',monospace;" id="old18">S/119</p>
                  <p id="val18" style="font-family:'Orbitron',sans-serif;font-size:1.25rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 10px rgba(0,255,213,0.5);">S/109</p>
                  <p class="text-xs mt-1" style="color:rgba(255,255,255,0.7);font-family:'Rajdhani',sans-serif;">al mes</p>
                </div>
              </div>
              <div class="cuota-card relative p-4 rounded-xl cursor-pointer transition-all duration-300" onclick="selectCuotaCard(24,this)" style="background:var(--bg-surface);border:1px solid rgba(255,255,255,0.1);">
                <div class="text-center">
                  <p class="text-xs mb-2" style="color:var(--text-primary);font-family:'Share Tech Mono',monospace;letter-spacing:1px;">24 meses</p>
                  <p class="text-xs line-through mb-1" style="color:rgba(255,255,255,0.5);font-family:'Share Tech Mono',monospace;" id="old24">S/99</p>
                  <p id="val24" style="font-family:'Orbitron',sans-serif;font-size:1.25rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 10px rgba(0,255,213,0.5);">S/89</p>
                  <p class="text-xs mt-1" style="color:rgba(255,255,255,0.7);font-family:'Rajdhani',sans-serif;">al mes</p>
                </div>
              </div>
              <div class="cuota-card-top relative p-4 rounded-xl cursor-pointer transition-all duration-300 scale-105" onclick="selectCuotaCard(36,this)" style="background:linear-gradient(135deg,rgba(0,255,213,0.12),rgba(0,255,213,0.06));border:2px solid var(--neon-cyan);" id="cuotaCard36">
                <div class="text-center">
                  <p class="text-xs mb-2" style="color:var(--text-primary);font-family:'Share Tech Mono',monospace;letter-spacing:1px;">36 meses</p>
                  <p class="text-xs line-through mb-1" style="color:rgba(255,255,255,0.5);font-family:'Share Tech Mono',monospace;" id="old36">S/79</p>
                  <p id="val36" style="font-family:'Orbitron',sans-serif;font-size:1.25rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 14px rgba(0,255,213,0.5);">S/69</p>
                  <p class="text-xs mt-1" style="color:rgba(255,255,255,0.7);font-family:'Rajdhani',sans-serif;">al mes</p>
                </div>
              </div>
              <div class="cuota-card relative p-4 rounded-xl cursor-pointer transition-all duration-300" onclick="selectCuotaCard(48,this)" style="background:var(--bg-surface);border:1px solid rgba(255,255,255,0.1);">
                <div class="text-center">
                  <p class="text-xs mb-2" style="color:var(--text-primary);font-family:'Share Tech Mono',monospace;letter-spacing:1px;">48 meses</p>
                  <p class="text-xs line-through mb-1" style="color:rgba(255,255,255,0.5);font-family:'Share Tech Mono',monospace;" id="old48">S/65</p>
                  <p id="val48" style="font-family:'Orbitron',sans-serif;font-size:1.25rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 10px rgba(0,255,213,0.5);">S/55</p>
                  <p class="text-xs mt-1" style="color:rgba(255,255,255,0.7);font-family:'Rajdhani',sans-serif;">al mes</p>
                </div>
              </div>
            </div>
            <div class="mt-8 p-6 rounded-xl" style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);">
              <div class="text-center">
                <p class="text-xs mb-2" style="color:var(--text-primary);font-family:'Rajdhani',sans-serif;">Pagar&iacute;as</p>
                <p class="line-through text-xl mb-1" id="summaryOld" style="color:rgba(255,255,255,0.5);font-family:'Share Tech Mono',monospace;">S/79/mes</p>
                <p style="font-family:'Orbitron',sans-serif;font-size:2.5rem;font-weight:800;color:var(--neon-cyan);text-shadow:0 0 20px rgba(0,255,213,0.6);line-height:1.1;"><span id="summaryVal">S/69</span><span style="font-size:0.85rem;color:var(--text-primary);">/mes</span></p>
                <p class="text-sm mt-2" id="summaryPlazo" style="color:var(--text-secondary);font-family:'Rajdhani',sans-serif;">durante 36 meses</p>
              </div>
            </div>
            <div class="flex gap-3 mt-6">
              <button class="flex-1 btn-loquiero-detalle py-4 rounded-xl" onclick="window.location.href='baldecash-solicitud.html'">&#128293; Lo quiero &mdash; Solicitar ahora</button>
              <button onclick="agregarAlCarrito()" class="flex items-center justify-center gap-2 px-6 py-4 rounded-xl font-semibold transition-colors cursor-pointer" style="background:rgba(0,255,213,0.1);border:1px solid var(--neon-cyan);color:var(--neon-cyan);">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="8" cy="21" r="1"></circle><circle cx="19" cy="21" r="1"></circle><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"></path></svg>
                <span class="hidden sm:inline">Al carrito</span>
              </button>
            </div>
          </div>
          <div class="w-full">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-8 h-8 rounded-full flex items-center justify-center" style="background:rgba(0,255,127,0.1);">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#00ff7f" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
              </div>
              <div>
                <h3 class="text-sm font-semibold" style="color:var(--text-primary);">Pack certificado BaldeCash</h3>
                <p class="text-xs" style="color:var(--text-muted);">Garant&iacute;as verificadas</p>
              </div>
            </div>
            <div class="flex flex-wrap items-center gap-2">
              <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full" style="background:var(--bg-surface);border:1px solid var(--border);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--neon-cyan)" stroke-width="2"><path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"/><circle cx="12" cy="8" r="6"/></svg><span class="text-xs font-medium" style="color:var(--text-secondary);">Garant&iacute;a 12 meses</span></div>
              <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full" style="background:var(--bg-surface);border:1px solid var(--border);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--neon-cyan)" stroke-width="2"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg><span class="text-xs font-medium" style="color:var(--text-secondary);">Env&iacute;o gratis Lima</span></div>
              <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full" style="background:var(--bg-surface);border:1px solid var(--border);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--neon-cyan)" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg><span class="text-xs font-medium" style="color:var(--text-secondary);">Soporte BaldeCash</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SPECS -->
    <section id="specs" class="mt-16 mb-12">
      <h2 class="mb-6" style="font-family:'Rajdhani',sans-serif;font-size:20px;font-weight:700;color:var(--text-primary);">Lo que incluye el Pack</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="spec-card"><div class="flex items-center gap-3 mb-3"><div class="spec-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 5a2 2 0 0 1 2 2v8.526a2 2 0 0 0 .212.897l1.068 2.127a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45l1.068-2.127A2 2 0 0 0 4 15.526V7a2 2 0 0 1 2-2z"/><path d="M20.054 15.987H3.946"/></svg></div><span class="spec-card-title">Laptop Legion 5 Pro</span></div><div class="spec-card-divider"></div><div class="space-y-1"><div class="spec-row"><span class="spec-row-label">Procesador</span><span class="spec-row-value primary">AMD Ryzen 7 7745HX</span></div><div class="spec-row"><span class="spec-row-label">GPU</span><span class="spec-row-value">NVIDIA RTX 4060 8GB</span></div><div class="spec-row"><span class="spec-row-label">RAM</span><span class="spec-row-value">16GB DDR5-4800</span></div><div class="spec-row"><span class="spec-row-label">Almacenamiento</span><span class="spec-row-value">512GB NVMe SSD</span></div><div class="spec-row"><span class="spec-row-label">Pantalla</span><span class="spec-row-value">16&quot; QHD+ 165Hz IPS</span></div></div></div>
        <div class="spec-card"><div class="flex items-center gap-3 mb-3"><div class="spec-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="7"/><path d="M12 2v8"/><path d="M5 10h14"/></svg></div><span class="spec-card-title">Mouse Logitech G203</span></div><div class="spec-card-divider"></div><div class="space-y-1"><div class="spec-row"><span class="spec-row-label">DPI</span><span class="spec-row-value primary">Hasta 8,000 DPI</span></div><div class="spec-row"><span class="spec-row-label">Botones</span><span class="spec-row-value">6 programables</span></div><div class="spec-row"><span class="spec-row-label">Iluminaci&oacute;n</span><span class="spec-row-value">RGB LIGHTSYNC</span></div><div class="spec-row"><span class="spec-row-label">Cable</span><span class="spec-row-value">1.8m ultra ligero</span></div></div></div>
        <div class="spec-card"><div class="flex items-center gap-3 mb-3"><div class="spec-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M8 14h8"/></svg></div><span class="spec-card-title">Teclado Membrana RGB</span></div><div class="spec-card-divider"></div><div class="space-y-1"><div class="spec-row"><span class="spec-row-label">Tipo</span><span class="spec-row-value primary">Membrana gaming</span></div><div class="spec-row"><span class="spec-row-label">Iluminaci&oacute;n</span><span class="spec-row-value">RGB completo</span></div><div class="spec-row"><span class="spec-row-label">Num&eacute;rico</span><span class="spec-row-value">Incluido</span></div><div class="spec-row"><span class="spec-row-label">Interface</span><span class="spec-row-value">USB</span></div></div></div>
        <div class="spec-card"><div class="flex items-center gap-3 mb-3"><div class="spec-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/></svg></div><span class="spec-card-title">Aud&iacute;fonos Gaming 7.1</span></div><div class="spec-card-divider"></div><div class="space-y-1"><div class="spec-row"><span class="spec-row-label">Driver</span><span class="spec-row-value primary">50mm neodimio</span></div><div class="spec-row"><span class="spec-row-label">Surround</span><span class="spec-row-value">Virtual 7.1</span></div><div class="spec-row"><span class="spec-row-label">Micr&oacute;fono</span><span class="spec-row-value">Boom retractil</span></div><div class="spec-row"><span class="spec-row-label">Interface</span><span class="spec-row-value">USB + 3.5mm</span></div></div></div>
        <div class="spec-card"><div class="flex items-center gap-3 mb-3"><div class="spec-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="8" width="20" height="10" rx="2"/><path d="M8 8V6a4 4 0 0 1 8 0v2"/></svg></div><span class="spec-card-title">Pad Gamer XL</span></div><div class="spec-card-divider"></div><div class="space-y-1"><div class="spec-row"><span class="spec-row-label">Tama&ntilde;o</span><span class="spec-row-value primary">80 &times; 30 cm</span></div><div class="spec-row"><span class="spec-row-label">Superficie</span><span class="spec-row-value">Textura optimizada</span></div><div class="spec-row"><span class="spec-row-label">Base</span><span class="spec-row-value">Antideslizante</span></div><div class="spec-row"><span class="spec-row-label">Bordes</span><span class="spec-row-value">Cosidos duraderos</span></div></div></div>
        <div class="spec-card"><div class="flex items-center gap-3 mb-3"><div class="spec-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><span class="spec-card-title">Garant&iacute;a &amp; Servicio</span></div><div class="spec-card-divider"></div><div class="space-y-1"><div class="spec-row"><span class="spec-row-label">Garant&iacute;a laptop</span><span class="spec-row-value primary">12 meses oficial</span></div><div class="spec-row"><span class="spec-row-label">Garant&iacute;a acc.</span><span class="spec-row-value">6 meses</span></div><div class="spec-row"><span class="spec-row-label">Soporte</span><span class="spec-row-value">BaldeCash 24/7</span></div><div class="spec-row"><span class="spec-row-label">Env&iacute;o</span><span class="spec-row-value">Gratis en Lima</span></div></div></div>
      </div>
    </section>

    <!-- PARA QUIEN ES -->
    <section id="section-ports" class="mb-12">
      <div class="w-full rounded-2xl p-6" style="background:var(--bg-card);border:1px solid var(--border);">
        <div class="flex items-center gap-3 mb-6"><div><h3 style="font-family:'Rajdhani',sans-serif;font-size:20px;font-weight:700;color:var(--text-primary);">&iquest;Para qui&eacute;n es este pack?</h3><p class="text-sm" style="color:var(--text-muted);">Perfil ideal del usuario</p></div></div>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div style="padding:20px;border-radius:12px;border:1px solid rgba(99,102,241,0.3);background:rgba(99,102,241,0.06);"><div style="font-size:2rem;margin-bottom:8px;">&#127891;</div><h4 style="font-family:'Rajdhani',sans-serif;font-weight:700;color:var(--text-primary);margin-bottom:6px;font-size:16px;">Estudiante universitario</h4><p style="font-size:13px;color:var(--text-secondary);line-height:1.5;">Clases, trabajos y gaming en un solo equipo potente. Ideal para tecnolog&iacute;a, dise&ntilde;o y m&aacute;s.</p></div>
          <div style="padding:20px;border-radius:12px;border:1px solid rgba(0,255,213,0.3);background:rgba(0,255,213,0.06);"><div style="font-size:2rem;margin-bottom:8px;">&#127918;</div><h4 style="font-family:'Rajdhani',sans-serif;font-weight:700;color:var(--text-primary);margin-bottom:6px;font-size:16px;">Gamer entusiasta</h4><p style="font-size:13px;color:var(--text-secondary);line-height:1.5;">RTX 4060 para jugar t&iacute;tulos AAA en alta calidad. 165Hz para experiencias fluidas.</p></div>
          <div style="padding:20px;border-radius:12px;border:1px solid rgba(245,176,112,0.3);background:rgba(245,176,112,0.06);"><div style="font-size:2rem;margin-bottom:8px;">&#128187;</div><h4 style="font-family:'Rajdhani',sans-serif;font-weight:700;color:var(--text-primary);margin-bottom:6px;font-size:16px;">Creador de contenido</h4><p style="font-size:13px;color:var(--text-secondary);line-height:1.5;">Potencia para streaming, edici&oacute;n de video y gaming simult&aacute;neo sin lag.</p></div>
        </div>
        <div class="mt-6 pt-4 flex flex-wrap gap-2 justify-center" style="border-top:1px solid var(--border);">
          <span class="px-3 py-1 rounded-full text-xs font-medium" style="background:rgba(0,255,213,0.1);color:var(--neon-cyan);">&#10003; Juegos AAA</span>
          <span class="px-3 py-1 rounded-full text-xs font-medium" style="background:rgba(0,255,213,0.1);color:var(--neon-cyan);">&#10003; Streaming</span>
          <span class="px-3 py-1 rounded-full text-xs font-medium" style="background:rgba(0,255,213,0.1);color:var(--neon-cyan);">&#10003; Trabajo remoto</span>
          <span class="px-3 py-1 rounded-full text-xs font-medium" style="background:rgba(0,255,213,0.1);color:var(--neon-cyan);">&#10003; Dise&ntilde;o gr&aacute;fico</span>
          <span class="px-3 py-1 rounded-full text-xs font-medium" style="background:rgba(0,255,213,0.1);color:var(--neon-cyan);">&#10003; E-sports</span>
        </div>
      </div>
    </section>

    <!-- CRONOGRAMA -->
    <section id="cronograma" class="mb-12">
      <div id="cronogramaWidget" class="w-full bg-white rounded-2xl p-6 shadow-sm border border-neutral-200">
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-6">
          <div class="flex items-center gap-3"><div><h3 style="font-family:'Rajdhani',sans-serif;font-size:20px;font-weight:700;color:var(--text-primary);">Detalle de Cuotas</h3><p class="text-sm text-neutral-500" id="cronSubtitle">36 pagos mensuales</p></div></div>
          <div class="flex gap-1 flex-wrap" id="cronMesesBtns">
            <button onclick="selectCronMeses(12,this)" class="cron-mes-btn px-3 py-1.5 text-xs font-medium rounded-full transition-all cursor-pointer bg-neutral-100 text-neutral-600 hover:bg-neutral-200">12m</button>
            <button onclick="selectCronMeses(18,this)" class="cron-mes-btn px-3 py-1.5 text-xs font-medium rounded-full transition-all cursor-pointer bg-neutral-100 text-neutral-600 hover:bg-neutral-200">18m</button>
            <button onclick="selectCronMeses(24,this)" class="cron-mes-btn px-3 py-1.5 text-xs font-medium rounded-full transition-all cursor-pointer bg-neutral-100 text-neutral-600 hover:bg-neutral-200">24m</button>
            <button onclick="selectCronMeses(36,this)" class="cron-mes-btn px-3 py-1.5 text-xs font-medium rounded-full transition-all cursor-pointer bg-[var(--neon-cyan)] text-white">36m</button>
            <button onclick="selectCronMeses(48,this)" class="cron-mes-btn px-3 py-1.5 text-xs font-medium rounded-full transition-all cursor-pointer bg-neutral-100 text-neutral-600 hover:bg-neutral-200">48m</button>
          </div>
        </div>
        <div class="overflow-x-auto rounded-xl border border-neutral-200">
          <table class="w-full min-w-[600px]"><thead><tr class="bg-neutral-50"><th class="text-left py-3 px-3 text-xs font-semibold text-neutral-500 uppercase">Cuota</th><th class="text-left py-3 px-3 text-xs font-semibold text-neutral-500 uppercase">Fecha</th><th class="text-right py-3 px-3 text-xs font-semibold text-neutral-500 uppercase">Capital</th><th class="text-right py-3 px-3 text-xs font-semibold text-neutral-500 uppercase">Inter&eacute;s</th><th class="text-right py-3 px-3 text-xs font-semibold text-neutral-500 uppercase">Monto</th><th class="text-right py-3 px-3 text-xs font-semibold text-neutral-500 uppercase">Saldo</th></tr></thead><tbody id="cronTableBody"></tbody></table>
        </div>
        <button id="cronToggleBtn" onclick="toggleCronograma()" class="w-full mt-4 py-2 flex items-center justify-center gap-2 text-sm font-medium rounded-lg transition-colors cursor-pointer" style="color:var(--neon-cyan);">
          <svg id="cronToggleIcon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>
          <span id="cronToggleText">Ver todo</span>
        </button>
        <div class="mt-4 pt-4 border-t border-neutral-200 flex items-center justify-between">
          <div class="flex items-center gap-2 text-neutral-600"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-green-500"><path d="M20 6 9 17l-5-5"/></svg><span class="text-sm font-medium">Total a pagar</span></div>
          <p class="text-2xl font-bold text-neutral-900" id="cronTotal">S/2,484</p>
        </div>
        <div class="mt-4 flex gap-3">
          <button class="flex-1 inline-flex items-center justify-center gap-2 px-4 h-10 text-sm font-medium rounded-lg bg-transparent transition-colors cursor-pointer" style="border:2px solid var(--neon-cyan);color:var(--neon-cyan);"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>Ver detalle de pago</button>
          <button class="flex-1 inline-flex items-center justify-center gap-2 px-4 h-10 text-sm font-medium rounded-lg bg-transparent border-2 border-neutral-300 text-neutral-700 hover:bg-neutral-50 transition-colors cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 15V3"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/></svg>Descargar PDF</button>
        </div>
      </div>
    </section>
    <script>
    (function(){
      var tasaMensual=0.0411,precioBase=2400,mesesNombres=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','setiembre','octubre','noviembre','diciembre'],cronMesesSeleccionado=36,cronExpandido=false;
      var cuotasPorPlazo={12:129,18:109,24:89,36:69,48:55};
      function generarCronograma(meses){var cuotaMensual=cuotasPorPlazo[meses],saldo=precioBase,filas=[],totalPagar=0,hoy=new Date(),mesInicio=hoy.getMonth(),anioInicio=hoy.getFullYear();for(var i=1;i<=meses;i++){var interes=saldo*tasaMensual,capital=cuotaMensual-interes;if(i===meses){capital=saldo;interes=cuotaMensual-capital;if(interes<0)interes=0;}saldo=saldo-capital;if(saldo<0)saldo=0;totalPagar+=cuotaMensual;var mesIdx=(mesInicio+i)%12,anio=anioInicio+Math.floor((mesInicio+i)/12);filas.push({num:i,fecha:mesesNombres[mesIdx]+' de '+anio,capital:capital,interes:interes,monto:cuotaMensual,saldo:saldo,esUltima:i===meses});}return{filas:filas,total:totalPagar};}
      function formatS(n){return 'S/'+n.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',');}
      function renderCronograma(){var data=generarCronograma(cronMesesSeleccionado),filas=data.filas,limite=cronExpandido?filas.length:Math.min(6,filas.length),html='';for(var i=0;i<limite;i++){var f=filas[i],bgClass=f.esUltima?'bg-green-100 text-green-600':'bg-[rgba(0,255,213,0.1)] text-[var(--neon-cyan)]';html+='<tr class="border-t border-neutral-100"><td class="py-3 px-3"><div class="w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold '+bgClass+'">'+f.num+'</div></td><td class="py-3 px-3 text-sm text-neutral-600 capitalize">'+f.fecha+'</td><td class="py-3 px-3 text-right text-sm text-neutral-700">'+formatS(f.capital)+'</td><td class="py-3 px-3 text-right text-sm text-neutral-500">'+formatS(f.interes)+'</td><td class="py-3 px-3 text-right"><span class="text-sm font-semibold text-neutral-900">'+formatS(f.monto)+'</span></td><td class="py-3 px-3 text-right text-sm text-neutral-600">'+formatS(f.saldo)+'</td></tr>';}
      document.getElementById('cronTableBody').innerHTML=html;document.getElementById('cronSubtitle').textContent=cronMesesSeleccionado+' pagos mensuales';document.getElementById('cronTotal').textContent='S/'+data.total.toLocaleString('es-PE');var toggleBtn=document.getElementById('cronToggleBtn');if(filas.length<=6){toggleBtn.style.display='none';}else{toggleBtn.style.display='flex';document.getElementById('cronToggleText').textContent=cronExpandido?'Ver menos':'Ver todo';var iconPath=cronExpandido?'m18 15-6-6-6 6':'m6 9 6 6 6-6';document.getElementById('cronToggleIcon').innerHTML='<path d="'+iconPath+'"/>';}}
      window.selectCronMeses=function(meses,btn){cronMesesSeleccionado=meses;cronExpandido=false;var btns=document.querySelectorAll('.cron-mes-btn');btns.forEach(function(b){b.className='cron-mes-btn px-3 py-1.5 text-xs font-medium rounded-full transition-all cursor-pointer bg-neutral-100 text-neutral-600 hover:bg-neutral-200';});btn.className='cron-mes-btn px-3 py-1.5 text-xs font-medium rounded-full transition-all cursor-pointer bg-[var(--neon-cyan)] text-white';renderCronograma();};
      window.toggleCronograma=function(){cronExpandido=!cronExpandido;renderCronograma();};
      renderCronograma();
    })();
    </script>

    <!-- SIMILARES -->
    <section id="similares" class="mb-12">
      <div class="rounded-2xl p-6" style="background:var(--bg-card);border:1px solid var(--border);">
        <div class="flex items-center justify-between mb-6">
          <div><h3 style="font-family:'Rajdhani',sans-serif;font-size:20px;font-weight:700;color:var(--text-primary);" class="mb-1">Tambi&eacute;n te puede interesar</h3><p class="text-sm" style="color:var(--text-muted);">Otros packs disponibles en BaldeCash</p></div>
          <div class="flex items-center gap-2">
            <button onclick="scrollSimilares(-1)" class="w-10 h-10 rounded-full flex items-center justify-center cursor-pointer border-none shadow-lg" style="background:var(--neon-cyan);color:#0a0a0a;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 18-6-6 6-6"/></svg></button>
            <button onclick="scrollSimilares(1)" class="w-10 h-10 rounded-full flex items-center justify-center cursor-pointer border-none shadow-lg" style="background:var(--neon-cyan);color:#0a0a0a;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg></button>
          </div>
        </div>
        <div id="similaresCarousel" style="display:flex;flex-direction:row;flex-wrap:nowrap;overflow-x:auto;overflow-y:hidden;padding-bottom:16px;scrollbar-width:none;gap:16px;">
          <a href="BALDECASH LANDING.html#packs" class="similar-pack-card"><div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;"><span style="font-size:1.8rem;">&#127775;</span><div><p style="font-family:'Share Tech Mono',monospace;font-size:10px;color:var(--neon-cyan);font-weight:700;letter-spacing:1.5px;text-transform:uppercase;">Pack</p><p style="font-family:'Bebas Neue',sans-serif;font-size:1.3rem;letter-spacing:1px;color:var(--text-primary);line-height:1;">STARTER</p></div></div><p style="font-size:12px;color:var(--text-secondary);margin-bottom:14px;line-height:1.5;">Laptop + 2 accesorios para empezar tu aventura gaming.</p><div style="display:flex;flex-direction:column;gap:5px;margin-bottom:14px;"><div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-secondary);font-family:'Rajdhani',sans-serif;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--neon-cyan)" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>Laptop entry-level gaming</div><div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-secondary);font-family:'Rajdhani',sans-serif;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--neon-cyan)" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>Mouse + Pad gaming</div></div><div style="display:flex;align-items:baseline;gap:6px;"><span style="font-family:'Orbitron',sans-serif;font-size:1.4rem;font-weight:800;color:var(--neon-cyan);">S/55</span><span style="font-family:'Rajdhani',sans-serif;font-size:0.85rem;color:var(--text-muted);">/mes</span></div></a>
          <a href="BALDECASH LANDING.html#packs" class="similar-pack-card" style="border-color:rgba(99,102,241,0.4);background:rgba(99,102,241,0.05);"><div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;"><span style="font-size:1.8rem;">&#128081;</span><div><p style="font-family:'Share Tech Mono',monospace;font-size:10px;color:var(--neon-purple);font-weight:700;letter-spacing:1.5px;text-transform:uppercase;">Pack</p><p style="font-family:'Bebas Neue',sans-serif;font-size:1.3rem;letter-spacing:1px;color:var(--text-primary);line-height:1;">ELITE</p></div></div><p style="font-size:12px;color:var(--text-secondary);margin-bottom:14px;line-height:1.5;">Setup completo con laptop top de gama y 6 accesorios premium.</p><div style="display:flex;flex-direction:column;gap:5px;margin-bottom:14px;"><div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-secondary);font-family:'Rajdhani',sans-serif;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--neon-purple)" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>Laptop RTX 4070 flagship</div><div style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text-secondary);font-family:'Rajdhani',sans-serif;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--neon-purple)" stroke-width="2.5"><path d="M20 6 9 17l-5-5"/></svg>6 accesorios premium</div></div><div style="display:flex;align-items:baseline;gap:6px;"><span style="font-family:'Orbitron',sans-serif;font-size:1.4rem;font-weight:800;color:var(--neon-purple);">S/99</span><span style="font-family:'Rajdhani',sans-serif;font-size:0.85rem;color:var(--text-muted);">/mes</span></div></a>
          <a href="BALDECASH LANDING.html#catalogo" class="similar-pack-card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border-style:dashed;"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--neon-cyan)" stroke-width="1.5" style="margin-bottom:12px;opacity:0.7;"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="m9 12 2 2 4-4"/></svg><p style="font-family:'Rajdhani',sans-serif;font-size:14px;font-weight:700;color:var(--text-primary);margin-bottom:4px;">Ver cat&aacute;logo completo</p><p style="font-size:12px;color:var(--text-muted);">Laptops y accesorios individuales</p></a>
        </div>
        <script>window.scrollSimilares=function(dir){var c=document.getElementById('similaresCarousel');if(c)c.scrollBy({left:dir*290,behavior:'smooth'});};</script>
      </div>
    </section>

    <!-- CONSIDERACIONES -->
    <section id="consideraciones" class="mb-12">
      <div class="consideraciones-box" style="background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:24px;">
        <div style="margin-bottom:24px;"><div style="display:flex;align-items:center;gap:12px;margin-bottom:6px;"><h3 style="font-family:'Rajdhani',sans-serif;font-size:20px;font-weight:700;color:var(--text-primary);margin:0;">Consideraciones importantes</h3></div><p style="font-size:13px;color:var(--text-muted);">Informaci&oacute;n que debes tener en cuenta antes de decidir</p></div>
        <div style="display:flex;flex-direction:column;gap:12px;">
          <div class="consid-item" style="padding:20px;border-radius:12px;border:2px solid rgba(255,0,64,0.3);background:rgba(255,0,64,0.06);"><div style="display:flex;align-items:flex-start;gap:16px;"><div style="padding:8px;border-radius:10px;flex-shrink:0;background:rgba(255,0,64,0.15);display:flex;align-items:center;justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ff3366" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div><div style="flex:1;"><h4 style="font-family:'Rajdhani',sans-serif;font-weight:700;color:var(--text-primary);margin:0 0 4px 0;font-size:15px;">Teclado membrana</h4><p style="font-size:13px;color:var(--text-secondary);margin:0;line-height:1.6;">El teclado incluido es de membrana, no mec&aacute;nico. Ideal para empezar, con buena respuesta y durabilidad.</p><div style="margin-top:10px;display:flex;align-items:flex-start;gap:8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ff3366" stroke-width="2" style="flex-shrink:0;margin-top:2px;"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg><p style="font-size:13px;margin:0;"><span style="font-weight:600;color:#ff3366;">Alternativa:</span> <span style="color:var(--text-secondary);">Puedes actualizar a un teclado mec&aacute;nico como accesorio adicional</span></p></div></div></div></div>
          <div class="consid-item" style="padding:20px;border-radius:12px;border:2px solid rgba(240,160,96,0.3);background:rgba(240,160,96,0.06);"><div style="display:flex;align-items:flex-start;gap:16px;"><div style="padding:8px;border-radius:10px;flex-shrink:0;background:rgba(240,160,96,0.15);display:flex;align-items:center;justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#f5b070" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div><div style="flex:1;"><h4 style="font-family:'Rajdhani',sans-serif;font-weight:700;color:var(--text-primary);margin:0 0 4px 0;font-size:15px;">Software del mouse</h4><p style="font-size:13px;color:var(--text-secondary);margin:0;line-height:1.6;">El Logitech G203 es compatible con Logitech G HUB (gratuito) para personalizar RGB y DPI.</p><div style="margin-top:10px;display:flex;align-items:flex-start;gap:8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#f5b070" stroke-width="2" style="flex-shrink:0;margin-top:2px;"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg><p style="font-size:13px;margin:0;"><span style="font-weight:600;color:#f5b070;">Nota:</span> <span style="color:var(--text-secondary);">Descarga gratis desde el sitio oficial de Logitech</span></p></div></div></div></div>
          <div class="consid-item" style="padding:20px;border-radius:12px;border:2px solid rgba(168,85,247,0.3);background:rgba(168,85,247,0.06);"><div style="display:flex;align-items:flex-start;gap:16px;"><div style="padding:8px;border-radius:10px;flex-shrink:0;background:rgba(168,85,247,0.15);display:flex;align-items:center;justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#b87aff" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></div><div style="flex:1;"><h4 style="font-family:'Rajdhani',sans-serif;font-weight:700;color:var(--text-primary);margin:0 0 4px 0;font-size:15px;">Imagen referencial</h4><p style="font-size:13px;color:var(--text-secondary);margin:0;line-height:1.6;">Las im&aacute;genes del pack son referenciales. Los colores y modelos exactos pueden variar seg&uacute;n stock disponible.</p><div style="margin-top:10px;display:flex;align-items:flex-start;gap:8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#b87aff" stroke-width="2" style="flex-shrink:0;margin-top:2px;"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg><p style="font-size:13px;margin:0;"><span style="font-weight:600;color:#b87aff;">Garant&iacute;a:</span> <span style="color:var(--text-secondary);">Los specs son fijos seg&uacute;n el pack seleccionado</span></p></div></div></div></div>
        </div>
      </div>
    </section>

  </div>
</main>
"""

# Replace placeholders with actual base64 srcs
new_main = new_main_raw.replace('DARK_SRC_PLACEHOLDER', dark_src, 1)
new_main = new_main.replace('LIGHT_SRC_PLACEHOLDER', light_src, 1)

# ============================================================
# BOTTOM NAV HTML to add before <!-- FOOTER -->
# ============================================================
bottom_nav_html = """<!-- BOTTOM MOBILE NAV -->
<nav class="bottom-nav">
  <div class="bottom-nav-inner">
    <a href="#galeria" class="active"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>Producto</a>
    <a href="#specs"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>Contenido</a>
    <a href="#cronograma"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>Pagos</a>
    <a href="#similares"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>Similar</a>
  </div>
</nav>

"""

# ============================================================
# CUOTA CALCULATOR JS to add before </body>
# ============================================================
cuota_js = """<script>
(function(){
  var cuotaBase={12:129,18:109,24:89,36:69,48:55};
  var cuotaOld={12:149,18:119,24:99,36:79,48:65};
  var selectedMeses=36;
  var inicialSeleccionada=0;
  function calcCuota(meses,inicial){var base=cuotaBase[meses],reduccion=Math.round(inicial/meses*0.8);return Math.max(base-reduccion,Math.round(base*0.7));}
  function updateSummary(){var cuota=calcCuota(selectedMeses,inicialSeleccionada),old=cuotaOld[selectedMeses];var sv=document.getElementById('summaryVal'),so=document.getElementById('summaryOld'),sp=document.getElementById('summaryPlazo');if(sv)sv.textContent='S/'+cuota;if(so)so.textContent='S/'+old+'/mes';if(sp)sp.textContent='durante '+selectedMeses+' meses';}
  window.selectCuotaCard=function(meses,el){selectedMeses=meses;updateSummary();};
  window.selectInicial=function(monto,btn){inicialSeleccionada=monto;document.querySelectorAll('[id^="inicialBtn"]').forEach(function(b){b.style.background='var(--bg-surface)';b.style.color='var(--text-secondary)';b.style.border='1px solid rgba(255,255,255,0.12)';b.style.boxShadow='none';});btn.style.background='var(--neon-cyan)';btn.style.color='#0a0a0a';btn.style.border='1px solid var(--neon-cyan)';btn.style.boxShadow='0 0 10px rgba(0,255,213,0.4)';updateSummary();};
  window.addEventListener('scroll',function(){var sections=['galeria','specs','section-ports','cronograma','similares','consideraciones'],links=document.querySelectorAll('.bottom-nav a'),current='';sections.forEach(function(id){var el=document.getElementById(id);if(el&&el.getBoundingClientRect().top<=120)current=id;});links.forEach(function(a){a.classList.remove('active');var href=a.getAttribute('href').replace('#','');if(href===current)a.classList.add('active');});});
})();
</script>
"""

# Add bottom nav before <!-- FOOTER -->
footer_marker = '<!-- FOOTER -->'
if footer_marker in after_main:
    new_after_main = after_main.replace(footer_marker, bottom_nav_html + footer_marker, 1)
    print("Added bottom nav before <!-- FOOTER -->")
else:
    print("WARNING: <!-- FOOTER --> not found in after_main!")
    # Try alternative
    new_after_main = after_main

# Add cuota JS before </body>
body_close = '</body>'
if body_close in new_after_main:
    new_after_main = new_after_main.replace(body_close, cuota_js + body_close, 1)
    print("Added cuota JS before </body>")
else:
    print("WARNING: </body> not found in after_main!")

# ============================================================
# Assemble final content
# ============================================================
final_content = new_before_main + new_main + new_after_main

# Write the final file
print(f"\nWriting output to: {file_path}")
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

output_size = os.path.getsize(file_path)
print(f"Output file size: {output_size:,} bytes ({output_size/1024/1024:.2f} MB)")

# Count lines in output
line_count = final_content.count('\n') + 1
print(f"Output line count: {line_count}")

# Quick verification
checks = {
    'id="specs"': 'specs section',
    'id="cronograma"': 'cronograma section',
    'id="similares"': 'similares section',
    'id="consideraciones"': 'consideraciones section',
    'bottom-nav': 'bottom nav',
    'selectCuotaCard': 'cuota calculator JS',
    'packImgDark': 'dark image',
    'packImgLight': 'light image',
    'gallery-viewer': 'gallery viewer CSS',
    'spec-row': 'spec-row CSS',
}

print("\nVerification checks:")
for marker, label in checks.items():
    found = marker in final_content
    status = "OK" if found else "MISSING"
    print(f"  [{status}] {label}: {marker!r}")

print("\nDone!")
