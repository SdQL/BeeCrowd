cases = int(input())

for i in range(cases):
    x, y = map(int, input().split())
    if x != 0 and y == 0:
        print('divisao impossivel')
    else:
        print(x/y)