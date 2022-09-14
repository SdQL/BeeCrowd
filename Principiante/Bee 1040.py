n1, n2, n3, n4 = map(float, input().split())
prom = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / (2+3+4+1)
print(f'Media: {prom:.1f}')
if prom > 7:
    print("Aluno aprovado.")
elif prom < 5:
    print("Aluno reprovado.")
elif prom <= prom <= 6.9:
    print("Aluno em exame.")
    n5 = float(input())
    print(f'Nota do exame: {n5:.1f}')
    prom2=(prom + n5)/2
    if prom2 >= 5:
        print("Aluno aprovado.")
    elif prom2 <= 4.9:
        print("Aluno reprovado.")

    print(f'Media final: {prom2:.1f}')








