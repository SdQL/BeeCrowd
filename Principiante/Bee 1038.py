X, Y = map(int, input().split())
precios = [4.00, 4.50, 5.00, 2.00, 1.50]
precioTotal = 0
for i in precios:
    precioTotal = Y * precios[X-1]
print("Total: R$ %.2f"%precioTotal)







