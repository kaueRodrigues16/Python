class Carro:
    def __init__(self, modelo, ano, marca, TipoDeCombustivel, valor):

        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.TipoDeCombustivel = TipoDeCombustivel
        self.valor = valor

    def apresentar(self):
        print(f" modelo:{self.modelo}, ano:{self.ano}, marca{self.marca}, tipo de combustivel:{ self.TipoDeCombustivel} ,valor:{self.valor}")


carro1 = Carro('fusca',1980,'volks','gasolina',25.000)

print(carro1.modelo)