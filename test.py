cum = 'poo.poo1.poo2'
new_cum = []
for dot in cum:
    if dot == '.':
        dot = ' '
    new_cum.append(dot)
new_cum = ''.join(new_cum)
print(new_cum)


