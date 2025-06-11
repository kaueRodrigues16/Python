class Aluno:
    def __init__(self):
        self.Nome = ""
        self.Nota1 = 0.0
        self.Nota2 = 0.0
        self.Media = 0.0

    def CalcularMedia(self):
        Media = (self.Nota1 + self.Nota2) / 2
        print(f"A media do aluno {self.Nome} é: {Media}")

    def Resultado(self):
        if ( ((self.Nota1 + self.Nota2) / 2)) >= 6 :
            print("Aprovado")
        else:
            print("Não aprovado")

Aluno = Aluno()

print("Digite o nome do aluno")
Aluno.Nome = input()

print("Agora digite a primeira nota deste aluno")
Aluno.Nota1 = float(input())

print("Agora digite a segunda nota deste aluno")
Aluno.Nota2 = float(input())

Aluno.CalcularMedia()
Aluno.Resultado()

