#São os tipos verdadeiros (TRUE, 1) ou falso (FALSE, 0)

vai_comer = "SIM"
if vai_comer == "SIM":
    print("Você disse 'SIM', então seu resposta é verdaidera. ")
else:
    print("Você disse sim, então sua resposta e falsa? não. ")

#O bloco acima foi apenas para explicar a lógica por trás do booleano, falso ou verdadeiro
#pois em python, até mesmo um espaço é considerado suficiente para que algo retorne verdadeiro
#Conseguimos ver melhor o booleano com condições e operadores comparativos:

exemplo = 10 > 11 #a variavel vai guardar se 10 é maior que 11, que nesse caso é falso
print(exemplo)

exemplo_positivo = 11 > 9 #vai guadar se 11 é maior que 9, o que é TRUE
print(exemplo_positivo)