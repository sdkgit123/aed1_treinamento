class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaDinamica:
    def __init__(self):
        self.cabeca = None

    def is_empty(self):
        return self.cabeca is None

    def push(self, elemento):
        novono = No(elemento)
        if self.is_empty():
            self.cabeca = novono
        else:
            novono.proximo = self.cabeca
            self.cabeca = novono

    def medicao(self):
        if self.is_empty():
            print("A lista está vazia")
            return
        else:
            conta = self.cabeca
            soma = 0
            while conta is not None:
                conta = conta.proximo
                soma += 1
        return soma


objeto = ListaDinamica()
objeto.medicao()
objeto.push(3)
objeto.push(3)
objeto.push(3)
objeto.push(3)
objeto.push(3)
objeto.push(3)
quantos = objeto.medicao()
print(quantos)

