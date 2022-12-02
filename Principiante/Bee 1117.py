counter = 0
valid_scores = []

while True:
    score = float(input())
    if 0 <= score <= 10:
        valid_scores.append(score)
        counter += 1
    else:
        print('nota invalida')

    if counter == 2:
        average = sum(valid_scores) / 2
        print('media = {:.2f}'.format(average))
        break
