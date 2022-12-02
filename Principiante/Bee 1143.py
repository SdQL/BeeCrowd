num = int(input())
counter = 1

for i in range(num):
    print('{} {} {}'.format(counter, counter**2, counter**3))
    counter += 1

