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

    def pop(self, elemento):
        if self.is_empty():
            print("Nao ha elementos na lista")
            return 0
        else:
            atual = self.cabeca
            anterior = None
            soma = 0
            while atual is not None:
                if atual.dado == elemento:
                    if anterior is None:
                        self.cabeca = atual.proximo
                    else:
                        anterior.proximo = atual.proximo
                    atual = atual.proximo
                    soma += 1
                else:
                    anterior = atual
                    atual = atual.proximo
            if soma != 0:
                return 1
            else:
                print("O elemento nao estava na lista")
                return 0


objeto = ListaDinamica()
objeto.pop(6)
objeto.push(3)
objeto.push(9)
objeto.push(9)
objeto.push(1)
objeto.push(8)
objeto.push(2)
comeco = objeto.cabeca
while comeco is not None:
    print(comeco.dado, end='      ')
    comeco = comeco.proximo
objeto.pop(56)
comeco = objeto.cabeca
while comeco is not None:
    print(comeco.dado, end=' ')
    comeco = comeco.proximo
