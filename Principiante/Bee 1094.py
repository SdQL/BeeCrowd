nCasos = int(input())
total_animales = 0
total_conejos = 0
total_sapos = 0
total_ratas = 0
for i in range(nCasos):
    cant, animal = input().split()
    cant = int(cant)
    if animal == 'C':
        total_conejos += cant
    elif animal == 'R':
        total_ratas += cant
    elif animal == 'S':
        total_sapos += cant
    total_animales = total_conejos + total_sapos + total_ratas

porcentaje_conejos = (total_conejos*100) / total_animales
porcentaje_ratones = (total_ratas*100) / total_animales
porcentaje_sapos = (total_sapos*100) / total_animales
print('Total: {} cobaias'.format(total_animales))
print('Total de coelhos: {}'.format(total_conejos))
print('Total de ratos: {}'.format(total_ratas))
print('Total de sapos: {}'.format(total_sapos))
print('Percentual de coelhos: {:.2f} %'.format(porcentaje_conejos))
print('Percentual de ratos: {:.2f} %'.format(porcentaje_ratones))
print('Percentual de sapos: {:.2f} %'.format(porcentaje_sapos))


