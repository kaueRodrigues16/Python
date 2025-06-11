class Retangulo:

    def __init__(self, largura, altura):

        self.largura = largura
        self.altura = altura

    def caluclarArea(self):
       area =self.altura*self.largura
       print(area)

    def CalcularPerimetro(self):
        perimetro = (self.altura+self.largura)*2
        print(perimetro)

altura = int(input("qual a altura do retangulo: "))
largura = int(input("qual a altura do retangulo: "))

retangulo = Retangulo(altura, largura)

retangulo.caluclarArea()
retangulo.CalcularPerimetro()