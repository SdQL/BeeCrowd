Dias = int(input())

edadAño = int(Dias/365)
Dias -= edadAño*365
edadMeses = int(Dias/30)
Dias -= edadMeses*30

print(edadAño,"ano(s)")
print(edadMeses,"mes(es)")
print(Dias,"dia(s)")