numeros = [10, 5, 78, 2, 34, 190]

def menorMaior(n):
    menor = n[0]
    maior = n[0]
    for i in n:
        if i >= maior:
            maior = i
        if i <= menor:
            menor = i
    return maior, menor

print(menorMaior(numeros))