class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        novono = Node(data)
        if self.head is None or self.head.data >= data:  # Caso para lista vazia ou inserção no início
            novono.next = self.head
            self.head = novono
            return

        # Encontrar a posição correta para inserção
        indicador = self.head
        while indicador.next is not None and indicador.next.data < data:
            indicador = indicador.next

        # Inserir o novo nó
        novono.next = indicador.next
        indicador.next = novono


objeto = LinkedList()
objeto.insert_sorted(6)
objeto.insert_sorted(3)
objeto.insert_sorted(9)
objeto.insert_sorted(9)
objeto.insert_sorted(1)
objeto.insert_sorted(8)
objeto.insert_sorted(2)
comeco = objeto.head
while comeco is not None:
    print(comeco.data, end='      ')
    comeco = comeco.next




