#Temos uma converção no python para digitar em multiplas linhas, usamos 3 aspas: '''

print('''coe
isso é
um texto de
multiplas linhas
      ''')

#Também podemos usar para fazer comentarios de multiplas linhas no código, mas não é uma boa ideia, sempre á uma boa ideia
#Usar o # para uma nova linha de comentário toda vez.

#ID() = descobrir se uma variavel aponta para o mesmo local que outra na memória

val1= 1
val2 = 1
print(id(val1), id(val2)) #Ambas apontam para o mesmo lugar na memoria, para melhor gerenciamento voce pode excluir ou refatorar seu código para economia de memória