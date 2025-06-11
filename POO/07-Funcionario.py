class Funcionario:
    def __init__(self):
        self.NomeFuncionario = ""
        self.Salario = 0.0

    def calcular_Bonus(self):
        Bonus = ((self.Salario / 100) * 10)
        return Bonus

    def mostrar_informacoes(self):
        print(f"O nome do funcionario é {self.NomeFuncionario}")
        print(f"O salario de {self.NomeFuncionario} é {self.Salario} reais")
        print(f"O valor do bonus é {self.calcular_Bonus()} reais")
        print(f"O salario mais o bonus dele vai ser de {self.Salario + self.calcular_Bonus()} reais")

Funcionario = Funcionario()

print("Digite o nome do funcionario")
Funcionario.NomeFuncionario = input()

print("O salario dele")

Funcionario.Salario = float(input())

Funcionario.mostrar_informacoes()