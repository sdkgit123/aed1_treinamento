class Expressao:
    def __init__(self):
        self.expressao = list("A*(B+C)/D")

    def transforma(self):
        objeto = Pilha()




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
        else:
            return None

