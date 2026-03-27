# Operadores "Matemáticos"

num = 10
num2= 30
# +(Soma) = Soma dois(minimo requerido) ou mais fatores, também é possivel usar com strings mas de outra forma.
print(num + num2)

# - (Subtração) = subtrai dois(minimo requerido) ou mais valores.

print(num2 - num)

# * (Multiplicação) = multiplica dois(Minimo requerido) ou mais valores, funciona com strings também de outra forma

print(num * num2)

# / (divisão) = divide dois(Minimo requerido) ou mais valores

print(num2 / num)

# // (divisão inteira) divide dois números e retorna sua parte inteira(em cima recebemos um 3.0, na // apenas o 3 será mostrando, como se o python desse um floor() no número

print(num2 // num)

# % (modulo) = resto da divisão, divide o maximo possivel até que sobre 1 ou nada.

print(num2 % num)

# ** (potencia ou exponenciação) potência que aprendemos na escola, exemplo: 2³ = 2x2x2
print(num ** num2)

####################Precedência dos Operadores ###############

# 1° () = tudo que está em parenteses vem em 1°
# 2° depois temos os Expoentes: potenciação
# 3° Ai vem a multiplicação e divisão (Da esquerda para a direita)
# 4° e por fim, soma e subtração (Da esquerda para a direita)