class Palavra:
    def __init__(self):
        self.palavra = list("Algoritmos")
        self.pilhainversa = []

    def inverte(self):
        objeto = Pilha()
        while self.palavra:
            objeto.push(self.palavra.pop(0))

        while objeto.is_empty() is not True:
            elemento = objeto.pop()
            self.pilhainversa.append(elemento)
        print(''.join(self.pilhainversa))


class Pilha:
    def __init__(self):
        self.pilha = []

    def is_empty(self):
        return len(self.pilha) == 0

    def push(self, elemento):
        self.pilha.append(elemento)
        return elemento

    def pop(self):
        if self.is_empty() is not True:
            return self.pilha.pop()
        return None


objetor = Palavra()
objetor.inverte()
