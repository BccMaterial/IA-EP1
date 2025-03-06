from queue import PriorityQueue

class FilaPrioridade:
    def __init__(self):
        self.fila = PriorityQueue()

    def push(self, valor, item):
        self.fila.put((valor, item))

    def pop(self):
        if (self.esta_vazio()):
            return None
        else:
            (_, no) = self.fila.get()
            return no

    def esta_vazio(self):
        return self.fila.empty()
