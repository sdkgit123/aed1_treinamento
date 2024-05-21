class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class otoNo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class PrimeiraListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def is_empty(self):
        return self.cabeca is None

    def push(self, elemento):
        novono = No(elemento)
        novono.proximo = self.cabeca
        self.cabeca = novono


class SegundaListaEncadeada:
    def __init__(self):
        self.otacabeca = None

    def is_empty(self):
        return self.otacabeca is None

    def push(self, elemento):
        novono = otoNo(elemento)
        novono.proximo = self.otacabeca
        self.otacabeca = novono


class Concatenacao:

    def concatena(self, plista, slista):
        if plista.is_empty():
            plista.cabeca = slista.otacabeca
        else:
            plcabeca = plista.cabeca
            while plcabeca.proximo is not None:
                plcabeca = plcabeca.proximo
            plcabeca.proximo = slista.otacabeca


listaum = PrimeiraListaEncadeada()
listadois = SegundaListaEncadeada()
concatena = Concatenacao()

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
