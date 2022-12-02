ages_list = []
average = 0
while True:
    age = int(input())
    if age < 0:
        break
    else:
        ages_list.append(age)
        average = sum(ages_list) / len(ages_list)

print('{:.2f}'.format(average))

