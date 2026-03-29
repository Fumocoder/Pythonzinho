#Aqui vamos falar de alguns dos métodos principais de uma string e algumas curiosidades!:
nome = input("Digite seu nome: ")

#1° strings são IMUTÁVEIS(Não podemos alterar os valores contidos em uma string)
##nome[0] = "J"
##print(nome)

#.upper()
print(nome.upper()) #O .upper() deve ser usado no fim da variavel (ou direto no input apos pegar o dado do usuario), ele vai tornar todas as letras maiúsculas.

#.lower() #Igual ao .upper() usado no fim da variavel ou direto no input, torna todas as letras minusculas

print(nome.lower())

#.capitalize() = Torna a 1° letra maiúscula e as outras minusculas.
print(nome.capitalize()) #Somente a 1° letra e tornada maiúscula, mesmo após espaços as outras continuaram minusculas.
##.title() = torna 1 ° letra maiúscula de CADA paralra e as outras minúsculas
print(nome.title()) #CUIDADO: podemos obter algumas letras indesejadas com alguns tipos de caracters especiais que contam da mesma forma que um espaço para o python(Explicarei depois)!!

#.casefold() = torna o texto "o mais equivalente ao padrão unicode possível", deixando todas as strings em minusculas, e padronizando alguns simbolos históricos como "ß" que significa "ss" em alemão:
alemao_letrinha ="ß"
print(alemao_letrinha.casefold()) #Util para padronização de alguns tipos de dados, como nomes e senhas

#center(tamanho, preenchimento) =  Basicamente vai "preencher" sua string para ter o tamanho certo, se ela nao tiver, vai usar o que estiver no campo "preenchimento" como no exemplo:

print(nome.center(15, "-")) # E como o nome diz, sempre vai deixar no centro :D ou tentar

nome_alterado = nome.center(10) #aqui só especificamos o tamanho da string e nao seu espaçador, então o python vai colocar espaços por padrão

print(nome_alterado)
print(len(nome_alterado)) #podemos contar o tamanho da string com len() veremos depois

#count() = como o nome diz, contador(contar)

print(nome.count("Ed")) #conta quantas vezes uma palavra ou letra acontece, voce pode limitar se so quer procurar no começo da string, no fim, no meio, etc... e ele retorna o tanto de vezes que isso aconteceu.

