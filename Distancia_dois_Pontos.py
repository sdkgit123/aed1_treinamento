import math


class Ponto:
    def __init__(self):
        self.corx = None
        self.cory = None

    def define(self, x, y):
        self.corx = x
        self.cory = y

    def distancia(self, x, y):
        try:
            distx = math.pow(self.corx - x, 2)
            disty = math.pow(self.cory - y, 2)
            resul = math.sqrt(distx + disty)
            print(f"{resul} unidades")
        except:
            print("Nao e possivel fazer a operacao")


objeto = Ponto()
objeto.distancia(2, 4)  # Vai entrar no except pois a primeira coordenada ainda não está definida
objeto.define(-3, -7)
objeto.distancia(2, 4)  # Tcharammm
