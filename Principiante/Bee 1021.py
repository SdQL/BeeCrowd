n = float(input())
billetes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
monedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for i in billetes:
    x = int(n / i)
    print( x,"nota(s) de R$ %.2f"%i)
    residuo = n % i
    n = residuo

print("MOEDAS:")
for k in monedas:
    x = int(round(n,2)/k)
    print(x,"moeda(s) de R$ %.2f"%k)
    residuo = n % k
    n = residuo
