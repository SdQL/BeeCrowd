numbers = []
while True:
    num = int(input())
    if num == 0:
        break

    for i in range(1, num+1):
        numbers.append(i)

    print(*numbers)
    numbers.clear()

