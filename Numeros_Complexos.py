class Ncomplex:
    def __init__(self):
        self.real = 0
        self.imag = 0


class Operacoes:
    def __init__(self):
        self.ponteir = Ncomplex()

    def cria(self):
        self.ponteir.real = 5
        self.ponteir.imag = 2
        print(f"{self.ponteir.real} + i{self.ponteir.imag}")

    def destroi(self):
        self.ponteir = None

    def soma(self, a, b):
        somareal = self.ponteir.real + a
        somaimag = self.ponteir.imag + b
        print(f"{somareal} + i{somaimag}")

    def subtrai(self, a, b):
        subreal = self.ponteir.real - a
        subimag = self.ponteir.imag - b
        print(f"{subreal} + i{subimag}")


opera = Operacoes()
opera.cria()
opera.soma(3, 4)
opera.subtrai(6, 8)
print(opera.ponteir)  # vai mostrar o endereço, ou seja, existe algo armazenado
opera.destroi()
print(opera.ponteir)  # limpou
