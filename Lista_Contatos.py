class Contatos:
    def __init__(self):
        self.nome = ["Bia", "Manu", "João", "Italo"]
        self.telefone = [6924, 8539, 6485, 2354]
        self.email = ["b", "e", "j",
                      "i"]


class MexeContatos:
    def __init__(self):
        self.ponteir = Contatos()

    def adiciona(self, n, t, e):
        self.ponteir.nome.append(n)
        self.ponteir.telefone.append(t)
        self.ponteir.email.append(e)

    def remove(self, n):
        verdade = False
        for i in range(len(self.ponteir.nome)):
            if self.ponteir.nome[i] == n:
                self.ponteir.nome.pop(i)
                self.ponteir.telefone.pop(i)
                self.ponteir.email.pop(i)
                verdade = True
                return
        if verdade is False:
            print("Nome nao encontrado.")

    def busca(self, n):
        verdade = False
        for i in range(len(self.ponteir.nome)):
            if self.ponteir.nome[i] == n:
                print(self.ponteir.nome[i])
                print(self.ponteir.telefone[i])
                print(self.ponteir.email[i])
                verdade = True
                return
        if verdade is False:
            print("Nome nao encontrado.")

    def listar(self):
        print(self.ponteir.nome)
        print(self.ponteir.telefone)
        print(self.ponteir.email)


objeto = MexeContatos()
objeto.adiciona("Andrey", 8347, "a")
objeto.listar()
objeto.remove("João")
objeto.busca("Andrey")
objeto.busca("Manu")
objeto.listar()
