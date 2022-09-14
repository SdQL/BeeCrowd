codigo, nUnidades, precioUnidad = map(float, input().split())
codigo1, nUnidades1, precioUnidad1 = map(float, input().split())


valorTotal = (nUnidades * precioUnidad) + (nUnidades1 * precioUnidad1)
print("VALOR A PAGAR: R$ %.2f"%valorTotal)