#Listas em python não são nada mais do que o próprio nome já diz: listas :/
#podemos inicializar uma lista vazia ou  já inserir dados nelas
lista = [] #aqui temos uma lista vazia
lista_nao_vazia = [1,2,3,4,5] #Aqui temos uma lista com valores, sempre os separando por vírgulas


#Também podemos ter diversos tipos de ddos dentro de uma lista, como:
lista_multipla = [1, "Edson", 2+2, "etc..."] #Podemos guadar, contas, outras listas, contas matematicas, funções, etc....

#Funções de uma lista:

#.append() = Usamos para adicionar um valor no final da lista

lista_nao_vazia.append(1) #adicionamos o 1 no final da nossa lista vazia
print(f"número 1 sendo adicionado no final da lista: {lista_nao_vazia}")

#Metodo len()
#Metodo importante que não falei antes, mas ele serve para checar o tamanho da uma lista, mas serve também para variaveis e alguns outros tipos de dados
print(len(lista_nao_vazia) ,"É o tamanho da nossa lista")
#Importante!!! No python sempre começamos a contar do 0 o indice de listas!!!
#E o len() retorna apenas a quantidade de valores em uma lista, nao o número de indices!!!

#.insert(posição, valor) = Podemos inserir valores em uma posição especifica da nossa lista
lista_nao_vazia.insert(5,10) #Aqui, estou adicionando o valor 10 na posição de indice 5 na nossa lista
print(f"Lista com o valor 10 inserido na posição 5 da lista:  {lista_nao_vazia}") #Se houver um número na posição que formos inserir outro, o insert vai empurrar tudo para a direita
#Também e bom deixar claro que: caso tentarmos adicionar o elemento em um indice que não existe, o insert() vai adicionar no fim da lista
#o mesmo vale para indices negativos, ele vai adicionar no começo da lista :d