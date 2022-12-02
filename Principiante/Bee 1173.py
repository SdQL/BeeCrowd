element = int(input())
array = [element, ]

for i in array:
    array.insert(len(array), i*2)

    print('N[{}] = {}'.format(array.index(i), i))

    if len(array) == 11:
        break

