array_list = []
fake_index = 0
for i in range(20):
    array_number = int(input())
    array_list.append(array_number)


for j in array_list[::-1]:
    print('N[{}] = {}'.format(fake_index, j))
    fake_index += 1