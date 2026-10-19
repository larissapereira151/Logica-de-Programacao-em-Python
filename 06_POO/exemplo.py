#A CLASSE: O modelo (a planta)
from types import coroutine

class celular:
    def __init__(self, marca, modelo, cor, bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria!! Coloque o aparelho para carregar.")
        else:
            self.ligado = True
            print (f"{self.modelo} Ligado!")

#Os objetos: Criados a partir da classe (as casas)

celular1 = celular( "Samsung", "Galaxy s23", "Preto")
celular2 = celular("Motorola", "Moto6", "Azul")

#Acessando e alterando atrivutos
print (celular2.marca)

#Támbem podmos alterar diretamente
celular1.cor = "branco"
print(celular1.cor)

#Chamando métodos
celular2.ligar()