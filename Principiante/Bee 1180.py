size = int(input())
array = list(map(int, input().split()))
print('Menor valor: {}'.format(min(array)))
print('Posicao: {}'.format(array.index(min(array))))