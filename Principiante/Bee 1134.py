types = {'Alcohol': 1, 'Gasoline': 2, 'Diesel': 3, 'End': 4}

counter_alcohol = 0
counter_gasoline = 0
counter_diesel = 0
while True:
    fuel = int(input())
    if fuel == types['Alcohol']:
        counter_alcohol += 1
    elif fuel == types['Gasoline']:
        counter_gasoline += 1
    elif fuel == types['Diesel']:
        counter_diesel += 1
    elif fuel == types['End']:
        break
    elif fuel not in types:
        continue

print('MUITO OBRIGADO')
print('Alcool: {}'.format(counter_alcohol))
print('Gasolina: {}'.format(counter_gasoline))
print('Diesel: {}'.format(counter_diesel))

