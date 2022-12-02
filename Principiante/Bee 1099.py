cases = int(input())

for i in range(cases):
    x, y = map(int, input().split())
    n_min = min(x, y)
    n_max = max(x, y)

    suma = 0
    for j in range(n_min+1, n_max):
        if j % 2 != 0:
            suma += j

    print(suma)