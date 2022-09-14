A, B, C = map(float, input().split())

#AREA DEL TRIANGULO DE BASE A Y ALTURA C
areaTriangulo = (A * C) / 2

#AREA DEL CIRCULO DE RADIO C
areaCirculo = 3.14159 * (C ** 2)

#AREA DEL TRAPEZIO DE BASES A Y B Y ALTURA C
areaTrapezio = ((A + B) * C) / 2

#AREA DEL QUADRADO DE LADO B
areaQuadrado = B ** 2

#AREA DO RETANGULO DE LADOS A E B
areaRetangulo = A * B

print("TRIANGULO: {:.3f}".format(areaTriangulo))
print("CIRCULO: {:.3f}".format(areaCirculo))
print("TRAPEZIO: {:.3f}".format(areaTrapezio))
print("QUADRADO: {:.3f}".format(areaQuadrado))
print("RETANGULO: {:.3f}".format(areaRetangulo))

