dupers = [6, 6, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
new_list = []
cont = 0
for i in dupers:
    if i in  new_list:
        pass
    else:
        new_list.append(i)
print(new_list)
