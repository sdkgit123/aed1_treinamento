class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Pilha:
    def __init__(self):
        self.cabeca = None

    def is_empty(self):
        return self.cabeca is None

    def push(self, elemento):
        novono = No(elemento)
        novono.proximo = self.cabeca
        self.cabeca = novono

    def pop(self, dado):
        if self.is_empty():
            print("Pilha vazia")
            return None
        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.dado == dado:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return atual.dado
            anterior = atual
            atual = atual.proximo
        print("Elemento não encontrado")
        return None

    def duplicatas(self):
        if self.is_empty():
            print("Pilha vazia")
            return

        elementos = set()
        atual = self.cabeca
        anterior = None

        while atual is not None:
            if atual.dado in elementos:
                if anterior is None:
                    self.pop(self.cabeca.dado)
                else:
                    self.pop(atual.dado)
            else:
                elementos.add(atual.dado)
                anterior = atual
            atual = atual.proximo

    def free(self):
        self.cabeca = None


# Teste da pilha
pilha = Pilha()
pilha.push(3)
pilha.push(2)
pilha.push(3)
pilha.push(1)
pilha.push(8)
pilha.push(2)

print("Pilha antes de remover duplicatas:")
cabeca = pilha.cabeca
while cabeca is not None:
    print(cabeca.dado, end=' ')
    cabeca = cabeca.proximo

pilha.duplicatas()

print("\nPilha depois de remover duplicatas:")
cabeca = pilha.cabeca
while cabeca is not None:
    print(cabeca.dado, end=' ')
    cabeca = cabeca.proximo

pilha.free()
