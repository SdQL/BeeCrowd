num = int(input())
array_value = 0
for i in range(1000):
    if array_value < num:
        print('N[{}] = {}'.format(i, array_value))
        array_value += 1

    else:
        array_value = 0
        print('N[{}] = {}'.format(i, array_value))
        array_value += 1
