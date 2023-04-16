
cases = int(input())


for i in range(cases):
    x, y = map(int, input().split())
    c = 0
    odd_array = []

    while c < y:
        if x % 2 != 0:
            odd_array.append(x)
            c += 1
        x += 1

    print(sum(odd_array))



