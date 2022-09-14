n = int(input())
print(n)
billetes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]

for i in billetes:
    x = int(n / i)
    print( x,"nota(s) de R$ %.2f"%x)
    residuo = n % i
    n = residuo