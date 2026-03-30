
with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', encoding='utf-8') as f:
    content = f.read()

i1 = content.find('Item 1')
i2 = content.find('Item 2')
i3 = content.find('Item 3')
i4 = content.find('<!-- =====', i3)

OLD = 'stroke="var(--neon-cyan)"'

seg1 = content[i1:i2].replace(OLD, 'stroke="#ff3366"')
seg2 = content[i2:i3].replace(OLD, 'stroke="#f5b070"')
seg3 = content[i3:i4].replace(OLD, 'stroke="#b87aff"')

content = content[:i1] + seg1 + seg2 + seg3 + content[i4:]

with open(r'C:\Users\USER\Desktop\Zona gamer\baldecash-detalle-1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.')
