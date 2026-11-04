# VEICULOS

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"{self.marca} {self.modelo} ligado.")

    def mostrar_info(self):
        if self.ligado:
            status = "ligado"
        else:
            status = "desligado"

        print(f"{self.marca} {self.modelo} - {status}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def abrir_porta_malas(self):
        print(f"O porta-malas do {self.modelo} foi aberto.")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def empinar(self):
        if self.ligado:
            print(f"A moto {self.modelo} está empinando!")
        else:
            print("Ligue a moto primeiro!")


print("\n===== HERANÇA =====")

carro = Carro("Toyota", "Corolla", 4)
moto = Moto("Honda", "CB 300", 300)

carro.ligar()
carro.mostrar_info()

moto.mostrar_info()
moto.empinar()

moto.ligar()
moto.mostrar_info()

carro.abrir_porta_malas()
moto.empinar()