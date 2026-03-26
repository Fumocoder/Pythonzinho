lista = [1, 2, -4, 5 ,7 ,29 , 39, 823, -823, -923, 1000, 2000, 7400, 4000]
pares = []
impares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(pares, impares)