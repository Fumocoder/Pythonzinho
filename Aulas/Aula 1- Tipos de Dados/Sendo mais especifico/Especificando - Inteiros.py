#É basicamente o tipo mais conhecido e "inicial" que temos

numero = 5 #o tipo int é o Número inteiro (sem ponto flutuante) negativo ou positivo
#Diferente de linguagens como o C ou Java, o python não tem um limite númerico para o valor inteiro 
#em Java ou C o limite é de −2.147.483.648 a 2.147.483.647
#em python podemos ter valores absurdos para um inteiro, se a nossa Memoria RAM aguentar.
#por exemplo, tecnicamente podemos ter o valor 10**999999999999 mas nosso computador travaria ou teriamos um erro de memoria antes. :D

#Abaixo vamos listar alguns métodos da classe inteira:


#BIT_LENGHT()

print("Quantidade de bits necessarios:", numero.bit_length())#Usamos para descobrir quants bits sao necessarios para representar o número

#BIT_COUNT()

print("número de bits: ",numero.bit_count()) #Conta quantos bits(1) temos

#Temos como converter o valores para octal(base 8) hexadecimal (16) binario (base 2) ou até algum outro valor que precisar-mos
print(f"Octal: {oct(numero)} hexadecimal: {hex(numero)} e binário: {bin(numero)}", sep="\n")