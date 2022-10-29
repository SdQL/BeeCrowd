inicio, final = map(int, input().split())

if inicio == 0 and final == 0:
    print("O JOGO DUROU 24 HORA(S)")
else:
    contador = 0
    for i in range(inicio + 1, 25):
        contador = contador + 1
        if final > 12:
            final -= 12

    if contador > 12:
        contador = contador - 12

    total = contador + final
    print("O JOGO DUROU {} HORA(S)".format(total))