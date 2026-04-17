from math import sqrt

#A principal função do python, ela é usada para exibir algo no console
#ela é usada da seguinte forma: print(argumento)


variavel = 98

print("Edson") #Podemos colocar  Strings

print(1,2,3,4,5) #Números

print(variavel) #Variaveis

print(sqrt(12))# funções


### Por padrão, no fim do print há uma quebra de linha
print("Que isso meu filho, calma", end='##\n') #Por padrão, o windows usa o padrão: CRLF( uma quebra de linha padrão) podemos alterar o comportamento do final do print com o comando end=''

###podemos alterar o "separar" como no exemplo abaixo:
print(10, 20, 30, 40, sep='_*_') #Agora, ao invés de ter um espaço (colocado por padrão) após a vírgula temos o simbolo de _*_