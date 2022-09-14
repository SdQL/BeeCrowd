a, b, c = map(int, input().split())

MAYOR = (a + b + abs(a - b)) / 2
X = (MAYOR + c + abs(MAYOR - c)) / 2
X = int(X)

print(X , "eh o maior")


