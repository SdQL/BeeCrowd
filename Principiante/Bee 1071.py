n1 = int(input())
n2 = int(input())

n_min = min(n1, n2)
n_max = max(n1, n2)
suma = 0
for i in range(n_min+1, n_max):
    if i % 2 != 0:
        suma += i

print(suma)
