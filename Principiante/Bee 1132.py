x = int(input())
y = int(input())

n_min = min(x, y)
n_max = max(x, y)

sum = 0
for i in range(n_min, n_max+1):
    if i % 13 != 0:
        sum += i

print(sum)