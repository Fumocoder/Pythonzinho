lista = [10, 20, 30, 40, 50]
tempList = []
for i in lista:
    tempList.append(-1)
    lista.pop()
    if len(lista) == 0:
        lista == tempList
        del tempList
        break
print(lista)