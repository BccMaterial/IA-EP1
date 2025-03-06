class Visitados:
    def __init__(self):
        # Conjuntos (Sets) em python e {1, 2, 3}
        # necessita ser uma tupla ou string por ser comparável com ==
        self.visitados = set({})

    def adicionar(self, no):
        self.visitados.add(tuple(no.estado))

    def foi_visitado(self, no):
        return tuple(no.estado) in self.visitados

    def tamanho(self):
        return len(self.visitados)
