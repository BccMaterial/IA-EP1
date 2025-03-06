from classes import BracoMecanico, algoritmos

problema = BracoMecanico("./config/teste.txt")


print(f"Estado inicial: {problema.bases_caixas}")
print(f"Custo: {problema.energia_gasta_total}")
print("")
