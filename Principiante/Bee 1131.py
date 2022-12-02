count_grenal = 1
wins_inter = 0
wins_gremio = 0
tie_games = 0
while True:
    inter, gremio = map(int, input().split())
    grenal = int(input('Novo grenal (1-sim 2-nao)\n'))

    if inter > gremio:
        wins_inter += 1
    elif gremio > inter:
        wins_gremio += 1
    elif gremio == inter:
        tie_games += 1

    if wins_inter > wins_gremio:
        top_winner = 'Inter venceu mais'
    elif wins_gremio > wins_inter:
        top_winner = 'Gremio venceu mais'
    else:
        top_winner = 'Não houve ncedor'

    if grenal == 2:
        break
    elif grenal == 1:
        count_grenal += 1
        continue

print('{} grenais'.format(count_grenal))
print('Inter:{}'.format(wins_inter))
print('Gremio:{}'.format(wins_gremio))
print('Empates:{}'.format(tie_games))
print(top_winner)