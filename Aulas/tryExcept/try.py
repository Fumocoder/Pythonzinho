#Introdução ao TryExcept:

idade = input("sua idade: ") #Criamos uma variavel para pegar a idade 

try: #aqui nós vamos TENTAR fazer algo:
    idade = int(idade) #Vamos transformar a idade em um INTEIRO, jaq por padrão nosso input pega o que foi digitado e transforma em STRING
    idade += 2 # Somamos a Idade digitada e adicionamos 2
    print(idade) #Mostramos a idade no console 
except: #Aqui, Caso nós NÃO TENHAMOS CONSEGUIDO executar o bloco acima, esse bloco será executado no lugar
    print("Digite somente números!")
else:
    print("A soma deu certo!")
finally:
    print("Arruma o código ai man")

#o Try sempre executa caso tudo esteja certo
#O except executa somente se o blloco do try for false(der erro) vai pegar o erro, jogar uma mensagem na tela (como botamos acima) e para a execução do programa
# Podemos adicionar um ELSE que vai executar SE NÃO DER ERRO
#e temos o FINALLY que vai executar se der erro ou não.

