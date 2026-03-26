
#and = Ambas as informações precisam ser verdadeiras para que o IF execute, caso contrario, o ELSE será executado
num = 4
somador = 9

if num >3 and somador >= 9:
    print(num + somador)
else:
    print(somador - num, end="\n\n\nseparador")

# or = Uma das informações precisam ser verdadeiras para que o IF execute, se ambas forem falsa o ELSE vai executar.
rg_pessoa = input("Está com seu RG?: ").upper()
cpf= input("Está com seu cpf?:  ").upper()
if rg_pessoa == "SIM" or cpf == "SIM":
    print("Por favor, me mostre para liberar sua passsagem")
else:
    print("Sinto muito, precisa de um dos dois para entrar")

# not = Basicamente inverte a condição, NOT nome, se nao digitarmos nada retorna 0 pois está vazia e cai para o ELSE, se tivermos digitado algo se torna automaticamente 1 pois há um valor nela, independen de string, número, etc...
nome= input("Digite seu nome: ")
if not nome:
    print("Seu nome está vazio >:C")
else:
    print(f"Que nome bonito, {nome} :3")