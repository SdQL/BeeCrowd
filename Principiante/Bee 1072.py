nCasos = int(input())
rango = range(10, 21)
c1 = 0
c2 = 0
for i in range(nCasos):
    num = float(input())
    if num in rango:
        c1 += 1
    else:
        c2 += 1

print('{} in'.format(c1))
print('{} out'.format(c2))