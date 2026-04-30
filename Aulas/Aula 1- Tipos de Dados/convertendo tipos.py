#Em python (e em outras diversas linguagens) podemos converter um tipo em outro
# Por exemplo, e comum em python pedir dados ao usuarios com números, se não formatarmos a string no começo, por padrão
# o que o usuario digitar será entregue como uma string  mesmo sendo um número:
numero = input("Digite um número: ") #O usuario digita um número
print(type(numero)) #Se digitarmos um número, por padrão caso não sejamos especificos na hora de pegar os dados, ele vira com o tipo str

#Podemos tratar isso convertendo o tipo para o desejado:
numero = int(numero) #convertendo diretamente o número para um tipo int
print(type(numero)) #recebemos o tipo int

#Os principais tipos que poedmos fazer essa conversão são:
#String(str()), inteiro(int()), números com ,(ffloat()), verdadeiro ou falso(bool)