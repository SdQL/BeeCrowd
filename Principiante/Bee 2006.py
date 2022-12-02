type_tea = int(input())
teas = list(map(int, input().split()))
counter = 0

for i in teas:
    if i == type_tea:
        counter += 1
    elif i != type_tea:
        counter += 0
print(counter)
