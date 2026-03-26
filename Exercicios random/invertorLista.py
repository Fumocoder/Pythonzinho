lista = [10, 20, 30, 40, 50]
tempList = []
for i in lista:
    tempList.insert(0, i)
lista = tempList
del tempList
print(lista)