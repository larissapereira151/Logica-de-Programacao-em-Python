# A CLASSE: O modelo (a planta)

class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: auau")

    def mostrar_info(self):
        print(f"Nome : {self.nome}, Raça: {self.raca}, Idade: {self.idade} anos")


# Os objetos: Criados a partir da classe (as casas)

cachorro1 = Cachorro("Rex", "Pastor Alemão", 3)
cachorro2 = Cachorro("Nescau", "Vira-lata", 2)

# Acessando atributos
print(cachorro1.nome)

# Também podemos alterar diretamente
cachorro1.idade = 4
print(cachorro1.idade)

# Chamando métodos
cachorro1.latir()
cachorro2.latir()

cachorro1.mostrar_info()
cachorro2.mostrar_info()