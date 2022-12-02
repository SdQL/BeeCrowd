x = int(input())
y = int(input())

n_min = min(x, y)
n_max = max(x, y)

for i in range(n_min+1, n_max):
    if i % 5 == 2 or i % 5 == 3:
        print(i)