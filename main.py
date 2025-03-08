from classes import BracoMecanico, algoritmos

problema = BracoMecanico("./config/teste.txt")

algoritmos.a_estrela(problema)

print(problema.bases_caixas)
