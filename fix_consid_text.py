
with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', encoding='utf-8') as f:
    content = f.read()

i1 = content.find('Item 1')
i4 = content.find('<!-- =====', content.find('Item 3'))

# Replace all text-secondary inside consideration items with white
old = 'color:var(--text-secondary);'
new = 'color:#ffffff;'

seg = content[i1:i4].replace(old, new)
content = content[:i1] + seg + content[i4:]

with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
