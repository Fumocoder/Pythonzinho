import re #importamos a bibliotecas REGEX(Regular expressions)

#Muito utilizado para validação e extração de dados especifimos.
texto1=  '''
Sites diversos:
https://google.com/
https://gov.br/
https://youtube.com/
'''
#(.) = lê qualquer caracter menos uma nova linha:
#/. = para podermos incluir o caractere . na busca
texto_padrao = "pipocando"
padrao = re.compile("pi.o.a")  #estamos buscando o padrão: "PI" (. = qualquer coisa menos uma nova linha) "O" (.) "a"
#Nesta parte apenas criamos o padrão, não estamos fazendo uma busca, tanto que, se dermos um print no padrão vai nos retornar o re.compile("pi.o.a")

#Criando uma forma de procurar o nosso "Padrão"
localiza_padrao = padrao.findall(texto_padrao) # aqui criamos uma variavel para ser nosso localizador, dentro dele colocamos o padrã que criamos com o re.compile acma
#usamos o findall() para achar TODAS as ocorrencias do padrão na palavra e dentro do findall() colocamos onde queremos buscar, nesse caso, no texto_padrao
print(localiza_padrao) #Perceba que quando rodamos o código ele vai nos retornar "Pipoca" pois esse é o padrão que estamos procurando, ele vai exlucir o "ndo" do fim


