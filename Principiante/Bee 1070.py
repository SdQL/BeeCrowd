numero = int(input())

iteracion = 0
while True:
    if numero % 2 != 0:
        print(numero)
        iteracion += 1
    else:
        iteracion = iteracion
    numero += 1
    if iteracion == 6:
        break
