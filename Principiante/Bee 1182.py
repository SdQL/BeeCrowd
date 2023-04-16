column = int(input())
operation = input().upper()
matrix = []

for i in range(12):
    row = []
    for j in range(12):
        row.append(float(input()))
    matrix.append(row)

green_area = [matrix[i][column] for i in range(12) if i >= 0 and i <= 11]

if operation == 'S':
    result = sum(green_area)
elif operation == 'M':
    result = sum(green_area) / len(green_area)

print('{:.1f}'.format(result))