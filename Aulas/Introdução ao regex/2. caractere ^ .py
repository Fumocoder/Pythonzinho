import re #Importamos a biblioteca

texto = 'Pipoca'

padrao_novo = re.compile("^a") #Basicamente estmaos procurando a primeira letra que nesse caso queremos A
check = padrao_novo.findall(texto) #Criamos o nosso localizador
print(check) #Aqui exibimos o resultados da checagem, que vai no retornar uma lista vazia, já que a noss string não começa com A

# O caractere ^ É usado para procurar no inicio da string

padrao_com_chaves = re.compile("[^a]") #Quando usamos o [] nesse caso, estamos buscando por qualquer caractere diferente de "a"
check_novo = padrao_com_chaves.findall(texto) #criamos o localizador
print(check_novo) # Temos a saida de todas as letras do nosso texto, exceto o "a" do final da palavra

