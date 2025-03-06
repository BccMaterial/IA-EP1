from classes import BracoMecanico

problema = BracoMecanico("./config/teste.txt")

problema.movimento(0)
problema.pegar()
problema.movimento(3)
problema.soltar()

print(problema.caixa_carregada_braco)
print(problema.bases_caixas)
print(problema.movimentos)
