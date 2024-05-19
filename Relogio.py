class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.__hora = hora  # Transformando os atributos em atributos privados, não podem ser acessados.
        self.__minuto = minuto
        self.__segundo = segundo

    def set_time(self, hora, minuto, segundo):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
        return f"{self.__hora :02d}:{self.__minuto :02d}:{self.__segundo :02d}"

    def get_time(self):
        return f"{self.__hora :02d}:{self.__minuto :02d}:{self.__segundo :02d}"

    def avancaseg(self):
        if self.__segundo == 59 and self.__minuto == 59 and self.__hora == 23:
            self.__hora = 00
            self.__minuto = 00
            self.__segundo = 00
        elif self.__segundo == 59 and self.__minuto == 59:
            self.__hora = self.__hora + 1
            self.__minuto = 00
            self.__segundo = 00
        elif self.__segundo == 59:
            self.__minuto = self.__minuto + 1
            self.__segundo = 00
        else:
            self.__segundo = self.__segundo + 1
        return f"{self.__hora :02d}:{self.__minuto :02d}:{self.__segundo :02d}"


# Exemplo de uso
relogio = Relogio(14, 30, 25)

print(relogio.get_time())  # 14:30:25
relogio.set_time(22, 59, 59)

print(relogio.get_time())

relogio.avancaseg()

print(relogio.get_time())  # 16:45:30

print(relogio.__hora)  # Não conseguirá acessar o atributo
