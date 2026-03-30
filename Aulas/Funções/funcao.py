# Funções: são basicamente códigos prontos que podemos rodar para executar determinada tarefa mais rápido, util para quando temos que fazer a mesma coisa varias vezes
# E ao invés de ficar escrevendo o codigo toda vez, chamamaos a função def [Nome da função](parametros) para nos ajudar

#São chamadas de def()


def nome (n): #O nome deve ser intuitivo, usamos o meto de nomeação com underline quando a função tiver mais que uma palavra: nome_completo, por exemplo.
    return  f"{n} Seja bem vindo"

print(nome("Edson")) ### Uma função generica e basica para dar uma mensagem de boas vindas com o nome da pessoa
#Pode não parecer nada, mas quando se tem milhares de nomes, essa função ajuda a economizar tempo ao inves de escrever toda vez uma mnesagem para cada usuario.

#o () da função permite pedir parametros (não sao obrigatorios caso voce apenas queira rodar um codigo sem pedir parametro algum)
#Trarei um projeto completo mais a frente.