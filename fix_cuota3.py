
filepath = r"C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    # 1. Regular card MESES labels: white -> theme var
    ("color:rgba(255,255,255,0.6);font-family:'Share Tech Mono',monospace;letter-spacing:1px;",
     "color:var(--text-secondary);font-family:'Share Tech Mono',monospace;letter-spacing:1px;"),

    # 2. Cuota inicial label + Pagarías label (same string, replace all)
    ("color:rgba(255,255,255,0.7);font-family:'Share Tech Mono',monospace;letter-spacing:2px;text-transform:uppercase;",
     "color:var(--text-secondary);font-family:'Share Tech Mono',monospace;letter-spacing:2px;text-transform:uppercase;"),

    # 3. TOP card 36 MESES label
    ("color:rgba(255,255,255,0.8);font-family:'Share Tech Mono',monospace;letter-spacing:1px;",
     "color:var(--text-secondary);font-family:'Share Tech Mono',monospace;letter-spacing:1px;"),

    # 4. TOP card strike price
    ("color:rgba(255,255,255,0.35);font-family:'Share Tech Mono',monospace;",
     "color:var(--text-muted);font-family:'Share Tech Mono',monospace;"),

    # 5. TOP card price: white -> neon cyan
    ("color:#fff;text-shadow:0 0 14px rgba(255,255,255,0.4);",
     "color:var(--neon-cyan);text-shadow:0 0 14px rgba(0,255,213,0.5);"),

    # 6. TOP card "al mes"
    ("color:rgba(255,255,255,0.6);font-family:'Rajdhani',sans-serif;",
     "color:var(--text-muted);font-family:'Rajdhani',sans-serif;"),

    # 7. Add cuota-card class to regular plazo cards
    ('class="relative p-4 rounded-xl cursor-pointer transition-all duration-300" style="background:var(--bg-surface);border:1px solid rgba(255,255,255,0.1);"',
     'class="cuota-card relative p-4 rounded-xl cursor-pointer transition-all duration-300" style="background:var(--bg-surface);border:1px solid rgba(255,255,255,0.1);"'),

    # 8. Add cuota-card-top class to TOP card
    ('class="relative p-4 rounded-xl cursor-pointer transition-all duration-300 scale-105" style="background:linear-gradient(135deg,rgba(255,255,255,0.12),rgba(255,255,255,0.06));border:2px solid rgba(255,255,255,0.5);box-shadow:0 0 20px rgba(255,255,255,0.1);"',
     'class="cuota-card-top relative p-4 rounded-xl cursor-pointer transition-all duration-300 scale-105" style="background:linear-gradient(135deg,rgba(255,255,255,0.12),rgba(255,255,255,0.06));border:2px solid rgba(255,255,255,0.5);box-shadow:0 0 20px rgba(255,255,255,0.1);"'),
]

count = 0
for old, new in replacements:
    n = content.count(old)
    if n > 0:
        content = content.replace(old, new)
        count += 1
        print(f"OK ({n}x): {old[:55]}...")
    else:
        print(f"NOT FOUND: {old[:55]}...")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print(f"\nDone: {count}/{len(replacements)} applied")
