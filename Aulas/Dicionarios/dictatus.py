#Dicionario são basicamente uma lista com rotulo, para sabermos o que cada valor é.
#Exemplo:

lista_lojas = {
    "São paulo": 6, #Aqui temos a chave São paulo com o valor 6
    "Rio de janeiro" : 3, #Aqui temos a chave Rio de Janeiro com o valor 3
    "Rio grande do Sul" : 3, #Aqui temos a chave Rio grande do Sul com o valor 3
}  #o dict é criado desta forma, (nome do dicionario) = {}
# basicamente o dicionario trabalha com a forma "chave-valor" dict{"nome da chave": valor,}
for i in lista_lojas: #Evitar ficar usando [i] no for, sempre de nomes mais especificos para voce saber o que está manipulando.
    print(i, "Possui:" , lista_lojas[i], "lojas.")

lista_nomes_alunos = {
    "Aluno um" : "Pedro pascal",
    "Aluno dois" : "Sarpamento Cruz",
    "Aluno Três" : "Juninho Palamares",
}

#Também temos o metodo proprio do dicionario chamado .keys() que nos retorna apenas as chaves(rotulos)
print(lista_nomes_alunos.keys())

#o .values() funciona da mesma forma que o .keys(), retornando apenas os valores.
print(lista_nomes_alunos.values())

#o .items() é um metodo mais interessante do dict: ele retorna não só a chave, como seu valor e separa cada chave com seu valor.
print(lista_nomes_alunos.items())

#Ambos os metodos .keys() e .values() e .items() retornam os valores dentro de algo chamado "view".

#Como remover um item de um dict?

#Usamos o metodo .pop(posição), ele remove a chave e o valor, para isso temos que passar a Chave no () do .pop()
lista_nomes_alunos.pop("Aluno um")
print(lista_nomes_alunos.items()) #O aluno um foi removido da lista

#Como verificar se um valor especifico dentro de um dicionario?
 #Basicamente usamos o metodo ""In""

if "Aluno um" in lista_nomes_alunos:
    print("Ele existe")
else:
    print("Tem não man")# Vamos receber o else jaq removes o aluno um acima.