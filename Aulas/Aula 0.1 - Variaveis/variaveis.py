# variavel é algo que usamos para guardar os dados que nosso programa vai usar na Memória RAM.
#Por convenção, temos algumas regras como:
# Começar com letra maiúscula
# separar palavras com _
# Tipagem dinamica: o python adivinha automaticamente o tipo de dado escrito, nao sendo necessario especificar o tipo
# NÃO usar palavras reservadas como: print, if, import,etc... pois isso pode dar problema
#Case sensitive: Nome e nome não são a mesma variavel para o python e não apontam para o mesmo lugar na memória.
# Usar nomes bons e claros, como nome, idade, cartao, etc... evitando coisas do tipo, n, i, cc, etc...
exemplo_boa_variavel = "Eae"

#Atribuição multipla: podemos declarar diversos tipos de variaveis:

nome, idade, cep = "Edson leite da silva",  23, "999999-20"


#ADENDO: em python, não temos "CONSTANTES" literais como em outras linguagens, mas temos uma convenção para que
#caso alguem pegue nosso codigo para modificar, ele não mude o que está na constante
#Declaramos com todas as letras maiúsculas:
ENDERECO_PESSOA = "Rua pipocas 123. av chov" 