import re
lista = []
texto = f'''    ''' #Variavel com espaços dentro

texto_2 = '''   
\fpipas
\ne
\tocas
\v eae
\risso ae
''' #Variavel com alguns valores  de separação  dentro

padrao_vazio =  re.compile(r'\s') #Criamos um padrao os caracteres de separação
padrao_not_vazio = re.compile(r"\S") #Criamos um padrão para procurar coisas que nao sejam o caractere de separação

checador_vazio = padrao_vazio.findall(texto) # criamos o checador  dos caracteres
checador_not_vazio = padrao_not_vazio.findall(texto) #criamos o checados dos NÃO caracteres

print(f"regex: (s) em funcionamento:", checador_vazio) #Exibimos na tela
#Note que vamos receber apenas os espaços, pois eles são considerados caracteres de separação

print(f"regex: (S) em funcionamento: ", checador_not_vazio)
#Perceba que no caso do uso do \S ele vai nos retornar uma lista vazia, pois não há caracteres de separação ou espaços nela

checador_com_letras_vazio = padrao_vazio.findall(texto_2) #checador para o texto 2
checador_com_letras_not_vazio = padrao_not_vazio.findall(texto_2) #Chcador para o texto 2

print("regex: (s) em ação em uma variavel com letras:, ", checador_com_letras_vazio )
#perceba que recebemos os espaços e alguns outro caracteres espciais que são considerados "vazios" em python

print("regex: (S) em ação em uma string com letras: ", checador_com_letras_not_vazio)
#E agora veja aqui, recebemos tudo, menos os espaços ou qualquer caractere vazio.
