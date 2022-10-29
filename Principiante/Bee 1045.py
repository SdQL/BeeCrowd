lados = list(map(float, input().split()))
lados.sort(reverse=True)#Ordena los valores de mayor a menor
a = lados[0]#Asigna el valor de la posicion 0 a la variable a
b = lados[1]#Asigna el valor de la posicion 1 a la variable b
c = lados[2]#Asigna el valor de la posicion 2 a la variable c

if a >= (b+c):
    print("NAO FORMA TRIANGULO")#Si el valor de a es mayor o igual a la suma de b y c, no se forma un triangulo
elif a**2 == (b**2 + c**2):
    print("TRIANGULO RETANGULO")#Si el valor de a al cuadrado es igual a la suma de b al cuadrado y c al cuadrado, se forma un triangulo rectangulo
elif a**2 > (b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")#Si el valor de a al cuadrado es mayor a la suma de b al cuadrado y c al cuadrado, se forma un triangulo obtusangulo
elif a**2 < (b**2 + c**2):
    print("TRIANGULO ACUTANGULO")#Si el valor de a al cuadrado es menor a la suma de b al cuadrado y c al cuadrado, se forma un triangulo acutangulo
if a == b == c:
    print("TRIANGULO EQUILATERO")#Si los valores de a, b y c son iguales, se forma un triangulo equilatero
elif a == b or b == c or c == a:
    print("TRIANGULO ISOSCELES")#Si solo dos valores de a, b y c son iguales, se forma un triangulo isosceles