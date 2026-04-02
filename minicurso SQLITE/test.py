#SQlite = Banco relacional ()
import sqlite3 #Importamos a biblioteca SQLITE3

ligacao = sqlite3.connect("./minicurso SQLITE/jogadores.db") #Criamos uma ligção(conexão) com um banco de dados existe.
#Se o banco de dados nao existir, ao executar o codigo execute abaixo, ela será criada automaticamente

cursor =  ligacao.cursor()#objeto mensageiro (Ele é quem faz executar os querry's no SQLite)

cursor.execute("CREATE TABLE  IF NOT EXISTS jogadores(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL, servidor TEXT NOT NULL, tmp_jogo INTEGER NOT NULL, poder INTEGER NOT NULL, UNIQUE(nome, servidor))") #Criamos uma tabela com 4 colunas
#o trecho IF NOT EXISTS serve para criar a tabela SOMENTE se ela nao existir, se ela existir ele nao vai criar isso evita um erro posterior de tentar criar uma tabela que ja existe
#id INTEGER NOT NULL PRIMAR KEY AUTOINCREMENT = Basicamente diz que nosso id é um INTEIRO(INTEGER) o PRIMARY KEY é o identificardor, só pode existir 1 por tabela e nao pode repetir
    # NOT NULL = não pode ser vazio
    #AUTOINCREMENT = a cada vez que um valor for adicionado, o id vai aumentar em 1 automaticamente seria algo como id+=1
    

ligacao.commit()
#fetchone = Vai sempre retornar o proximo item da tabela


#fetchmany
#fetchall