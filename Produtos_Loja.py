class Produto:
    def __init__(self):
        self.nome = "Toalha"
        self.preco = 876438


class MexeProduto:
    def __init__(self):
        self.ponteir = Produto()

    def getproduto(self):
        return self.ponteir.nome, self.ponteir.preco

    def setproduto(self, nome, preco):
        self.ponteir.nome = nome
        self.ponteir.preco = preco
        return


objeto = MexeProduto()
dadosproduto = objeto.getproduto()
print(dadosproduto)
objeto.setproduto("Mesa", 34986394)
dadosproduto = objeto.getproduto()
print(dadosproduto)
