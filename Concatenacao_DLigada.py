class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class PrimeiraListaDuplamenteLigada:
    def __init__(self):
        self.cabeca = None
        self.rabo = None

    def is_empty(self):
        return self.cabeca is None

    def push(self, elemento):
        novono = No(elemento)
        if self.is_empty():
            self.cabeca = self.rabo = novono
        else:
            novono.proximo = self.cabeca
            self.cabeca.anterior = novono
            self.cabeca = novono

    def remove(self, elemento):
        if self.is_empty():
            print("Lista vazia")
            return

        atual = self.cabeca
        while atual is not None:
            if atual.dado == elemento:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.rabo = atual.anterior

                return

            atual = atual.proximo


class SegundaListaDuplamenteLigada:
    def __init__(self):
        self.cabeca = None
        self.rabo = None

    def is_empty(self):
        return self.cabeca is None

    def push(self, elemento):
        novono = No(elemento)
        if self.is_empty():
            self.cabeca = self.rabo = novono
        else:
            novono.proximo = self.cabeca
            self.cabeca.anterior = novono
            self.cabeca = novono

    def remove(self, elemento):
        if self.is_empty():
            print("Lista vazia")
            return

        atual = self.cabeca
        while atual is not None:
            if atual.dado == elemento:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.rabo = atual.anterior

                return

            atual = atual.proximo

class Contatenacao:
    def concatena(self, listaum, listadois):
        if listaum.is_empty():
            listaum.cabeca = listadois.cabeca
            listaum.rabo = listadois.rabo
        elif listadois.is_empty():
            listadois.cabeca = listaum.cabeca
            listadois.rabo = listaum.rabo
        else:
            listadois.cabeca.anterior = listaum.rabo
            listaum.rabo.proximo = listadois.cabeca
            listaum.rabo = listadois.rabo



listaum = PrimeiraListaDuplamenteLigada()
listadois = SegundaListaDuplamenteLigada()
concatena = Contatenacao()

listaum.push(3)
listaum.push(3)
listaum.push(3)
listaum.push(3)
listaum.push(3)
listaum.push(3)

listadois.push(8)
listadois.push(8)
listadois.push(8)
listadois.push(8)
listadois.push(8)

concatena.concatena(listaum, listadois)

medidor = listaum.cabeca

while medidor is not None:
    print(medidor.dado, end='   ')
    medidor = medidor.proximo
