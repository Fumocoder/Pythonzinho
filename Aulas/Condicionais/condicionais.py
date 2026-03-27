#IF,ELSE,ELIEF

#If = Pode ser usado sozinho, ele acontece se uma dada condição for verdadeira

numero = 5

if numero == 6:
    print("KK eae") #Nada vai ocorrer pois a condição não é verdadeira


#Else = Contrario do If, ocorre se a condição não for verdadeira( condição contraria ao if)
if numero == 7:
    print("KK eae men")
else:
    print("Coe man") # O else será executado pois o numero não corresponde a condição do if :D

#Elif = condição alternativa ao IF(assim por dizer), podemos adicionar mais condições para que sejam executadas, podemos ter a quantidade de elif's que quiseremos, mas não é bom encher seu código deles, lembre-se disso xD
if numero == 3:
    print("KK eae men")
elif numero == 4:
    print("Aiinda não")
elif numero == 5:
    print("Agora o elif foi executado :D") # o Elif vai ser executado, pois agora temos a condição verdadeira
else:
    print("É isso ai man")