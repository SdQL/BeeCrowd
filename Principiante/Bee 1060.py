lista = []
for i in range(6):
    nums = float(input())
    lista.append(nums)

contador = 0
for j in lista:
    if j > 0:
        contador += 1
print("{} valores positivos".format(contador))