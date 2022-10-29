tipoDeTe = int(input())
A, B, C, D, E = map(int, input().split())
lista = [A, B, C, D, E]
contador = 0
for i in lista:
    if i == tipoDeTe:
        contador += 1
    elif i != tipoDeTe:
        contador == 0
print(contador)
