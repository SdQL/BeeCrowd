cases = int(input())

for i in range(cases):
    x = int(input())
    count = 0

    for j in range(1, x+1):
        if x % j == 0:
            count += 1

    if count > 2:
        print('{} nao eh primo'.format(x))
    else:
        print('{} eh primo'.format(x))
