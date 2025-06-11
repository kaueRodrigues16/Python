class Produto:
    def __init__(self):
        self.NomeProduto = ""
        self.PrecoProduto = 0.0
        self.DescontoProduto = 0.0

    def Mostra_Preco_Com_Desconto(self):
        PrecoComDesconto = self.PrecoProduto - ((self.PrecoProduto / 100) * self.DescontoProduto)
        print(f"O preço original do produto {self.NomeProduto} é { self.PrecoProduto} reais")
        print(f"Com o desconto de {self.DescontoProduto}%, o valor ira ser de {PrecoComDesconto} reais")

Produto = Produto()

print("Digite o nome do produto")
Produto.NomeProduto = input()

print("Agora o preço deste produto")
Produto.PrecoProduto = float(input())

print("Agora o desconto em porcentagem")
Produto.DescontoProduto = float(input())

Produto.Mostra_Preco_Com_Desconto()
