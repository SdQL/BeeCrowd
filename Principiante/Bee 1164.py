cases = int(input())
divisors = []
for i in range(cases):
    num = int(input())
    for j in range(1, num):
        if num % j == 0:
            divisors.append(j)

    if sum(divisors) == num:
        print('{} eh perfeito'.format(num))
    else:
        print('{} nao eh perfeito'.format(num))

    divisors.clear()
