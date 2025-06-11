class ContaBanco:
    def __init__(self):
        self.titular ="Tiago"
        self.saldo = 0.0
        self.DepositarSaldo = 0.0
        self.SacarSaldo = 0.0


    def Depositar(self):
        print("Digite o valor que queira depositar:  ")
        self.DepositarSaldo = input()

        self.saldo = self.saldo + float(self.DepositarSaldo)
        print(ContaBanco.saldo)

    def Sacar(self):
        print("Digite o valor que queira sacar:  ")
        self.SacarSaldo= input()

        if (float(self.SacarSaldo) > self.saldo):
            print(f"Seu saldo atual é de {self.saldo}, impossivel sacar um valor maior que o saldo meu nobre")
        else:
            self.saldo = self.saldo - float(self.SacarSaldo)
            print(ContaBanco.saldo)

ContaBanco = ContaBanco()
ContaBanco.Depositar()
ContaBanco.Sacar()
