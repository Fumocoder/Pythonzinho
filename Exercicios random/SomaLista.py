import sys
numeros = input("Digite 5 números para serem somados separados por espaço: ")
def somadorLista(numeros):
    try:
        numeros = numeros.split()
        tempList = []
        for i in numeros:
            tempList.append(float(i))
        return sum(tempList)
        
    except:
        print("Erro inesperado, tente novamente: ")
print(somadorLista(numeros))

