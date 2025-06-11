class livro:
    def __init__(self):
        self.Titulo = "Pequeno Príncipe"
        self.Autor = "Antoine de Saint-Exupéry"
        self.Numero_Paginas =	96

    def Resumo(self):
        print(f"O livro {self.Titulo} foi escrito por {self.Autor} e tem {self.Numero_Paginas} páginas.")

livro = livro()

livro.Resumo()