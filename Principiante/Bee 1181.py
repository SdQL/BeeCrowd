l = int(input())
operation = input()

matriz = []
for i in range(12):
    matriz.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

if operation == 'S':
    add = 0
    for k in matriz[l]:
        add = add + k
    print(add)

if operation == 'M':
    average = 0
    add = 0
    for k in matriz[l]:
        add = add + k
    average = add / 12
    print(average)