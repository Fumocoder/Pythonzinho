# Usamos ela em sistemas grande ou projeto maiores, quando estamos criando um programa ou aplicativo mais "grandinho"

#POO = programação orientada a objeto, podemos dizer que classes == objetos (De certa forma)

#Exemplo: um celular Iphone 16, ele tem camera, tela touch, controle por voz, botão pra ligar, botão para aumentar ou diminuir volume.
# Podemos dizemos que o celular tem diversos ATRIBUTOS
# Ele também tem "FUNÇÕES" como por exemplo, se eu apertar os botoes de volume ele vai abaixar ou aumentar, se eu clicar na tela touch ela vai ligar, posso tirar fotos coma  camera, etc...
# "FUNÇÕES" sao o que nosso celular pode fazer;
# Ou seja: Class CELULAR tem ATRIBUTOS(SELF, MODELO, CAMERA, RAM, BOTOES, ETC...)
#DEF  AUMENTARVLUME()

#É mais fácil entender isso mexerndo na classe diretamente.

#Vamos começar criando a Classe Celular:

class Celular:
    def __init__(self, modelo, cor, camera, memoria, botao_ligar, botao_volume,): #__init__ = Ela inicia  nossa classe, ela diz o que precisamos para que nosso objeto exista.
        self.modelo = modelo #Definimos o modelo
        self.cor = cor #Definimos a cor
        self.camera = camera # dizemos o modelo da camera
        self.memoria = memoria # Quanto de memoria ele tem
        self.botao_ligar = botao_ligar #O botão de ligar
        self.botao_volume = botao_volume #O botão de volume
        #Nesta parte, criamos o "modelo" de como nosso celular deve seguir para ser um "celular" ou seja, existir.

        def tirarFoto():
            return f"Foto tirada pela camera de {self.camera}"
        
iphone = Celular(16, "Azul", "100MP", "12GB",  )