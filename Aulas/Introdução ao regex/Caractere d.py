import re

texto = "Pipocas extremas de 1992"

padrao= re.compile(r"\d") #criamos o padrão para qualquer caractere que seja um númeo de 0 a 9
localizador = padrao.findall(texto) #cramos o buscador
print(localizador) #retorna os algarismos

#Ao usar caracteres, é sempre uma boa ideia usar o r(raw string) no re.compile para evitar problemas com caracteres especiais como \n

padrao_exclusor = re.compile(r"\D") #o padrão parece igual, mas quando usamos a letrsa Maiusculas estamos pegando tudo que nao seja números
localizador_exclusor = padrao_exclusor.findall(texto)
print(localizador_exclusor)