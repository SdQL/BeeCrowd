import math
A, B, C = map(float, input().split())
x = (B**2)-(4*A*C)

if(x < 0 or A==0):
    print("Impossivel calcular")
else:
    x = math.sqrt(x)
    r1 = (-B + x)/(2*A)
    r2 = (-B - x) /(2 * A)
    print("R1 = %.5f"%r1)
    print("R2 = %.5f"%r2)