
filepath = r"C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    # Container border/shadow - magenta -> white/subtle
    ("border:1px solid rgba(233,30,140,0.25);box-shadow:0 0 32px rgba(233,30,140,0.08),0 8px 32px rgba(0,0,0,0.3);",
     "border:1px solid rgba(255,255,255,0.12);box-shadow:0 0 32px rgba(255,255,255,0.04),0 8px 32px rgba(0,0,0,0.3);"),

    # Title gradient - magenta -> white solid
    ("background:linear-gradient(90deg,#e91e8c,#ff6ec7);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;",
     "color:#ffffff;"),

    # Subtitle monospace color stays muted, no change needed

    # Label color magenta -> white
    ("color:#e91e8c;font-family:'Share Tech Mono',monospace;letter-spacing:2px;text-transform:uppercase;",
     "color:rgba(255,255,255,0.7);font-family:'Share Tech Mono',monospace;letter-spacing:2px;text-transform:uppercase;"),

    # Active button gradient magenta -> white
    ("background:linear-gradient(90deg,#e91e8c,#c2185b);box-shadow:0 0 12px rgba(233,30,140,0.4);font-family:'Rajdhani',sans-serif;",
     "background:rgba(255,255,255,0.2);border:1px solid rgba(255,255,255,0.5);font-family:'Rajdhani',sans-serif;"),

    # Inactive buttons border magenta -> white
    ("border:1px solid rgba(233,30,140,0.2);font-family:'Rajdhani',sans-serif;",
     "border:1px solid rgba(255,255,255,0.12);font-family:'Rajdhani',sans-serif;"),

    # Plazo card border magenta -> white
    ("border:1px solid rgba(233,30,140,0.2);",
     "border:1px solid rgba(255,255,255,0.1);"),

    # Meses label magenta -> white muted
    ("color:#e91e8c;font-family:'Share Tech Mono',monospace;letter-spacing:1px;",
     "color:rgba(255,255,255,0.6);font-family:'Share Tech Mono',monospace;letter-spacing:1px;"),

    # TOP card gradient background magenta -> white glow
    ("background:linear-gradient(135deg,rgba(233,30,140,0.25),rgba(194,24,91,0.15));border:2px solid #e91e8c;box-shadow:0 0 20px rgba(233,30,140,0.3);",
     "background:linear-gradient(135deg,rgba(255,255,255,0.12),rgba(255,255,255,0.06));border:2px solid rgba(255,255,255,0.5);box-shadow:0 0 20px rgba(255,255,255,0.1);"),

    # TOP badge gradient magenta -> white
    ("background:linear-gradient(90deg,#e91e8c,#c2185b);font-family:'Bebas Neue',sans-serif;letter-spacing:1px;box-shadow:0 0 8px rgba(233,30,140,0.5);",
     "background:rgba(255,255,255,0.2);border:1px solid rgba(255,255,255,0.5);font-family:'Bebas Neue',sans-serif;letter-spacing:1px;"),

    # TOP card 36 meses label color pink -> white
    ("color:#ff6ec7;font-family:'Share Tech Mono',monospace;letter-spacing:1px;",
     "color:rgba(255,255,255,0.8);font-family:'Share Tech Mono',monospace;letter-spacing:1px;"),

    # TOP card strike price pink -> white muted
    ("color:rgba(255,110,199,0.5);font-family:'Share Tech Mono',monospace;",
     "color:rgba(255,255,255,0.35);font-family:'Share Tech Mono',monospace;"),

    # TOP card price text-shadow magenta -> white
    ("color:#fff;text-shadow:0 0 14px rgba(233,30,140,0.8);",
     "color:#fff;text-shadow:0 0 14px rgba(255,255,255,0.4);"),

    # TOP card "al mes" pink -> white
    ("color:rgba(255,110,199,0.8);font-family:'Rajdhani',sans-serif;",
     "color:rgba(255,255,255,0.6);font-family:'Rajdhani',sans-serif;"),

    # Pagarías box background magenta -> white
    ("background:rgba(233,30,140,0.06);border:1px solid rgba(233,30,140,0.2);",
     "background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);"),

    # Pagarías label magenta -> white
    ("color:#e91e8c;font-family:'Share Tech Mono',monospace;letter-spacing:2px;text-transform:uppercase;",
     "color:rgba(255,255,255,0.6);font-family:'Share Tech Mono',monospace;letter-spacing:2px;text-transform:uppercase;"),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
    else:
        print(f"NOT FOUND: {old[:60]}...")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Done. {count}/{len(replacements)} replacements applied.")
