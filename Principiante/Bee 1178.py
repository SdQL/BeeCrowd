x = float(input())
for i in range(100):
    print('N[{}] = {:.4f}'.format(i, x))
    x /= 2

"""
x = float(input())
array_list = [x, ]


for i in range(0, 101):
    array_list.append(array_list[i]/2)
    indice = array_list.index(array_list[i])
    print('N[{}] = {:.4f}'.format(indice, array_list[i]))

"""