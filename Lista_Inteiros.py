class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def is_empty(self):
        return self.cabeca is None

    def push(self, elemento):
        novono = No(elemento)
        novono.proximo = self.cabeca
        self.cabeca = novono


listainteiros = [5, 7, 2, 6, 2, 8, 9]
objeto = ListaEncadeada()
for i in range(len(listainteiros)):
    objeto.push(listainteiros.pop())

medidor = objeto.cabeca
while medidor is not None:
    print(medidor.dado)
    medidor = medidor.proximo
