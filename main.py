from classes import BracoMecanico, algoritmos

problema = BracoMecanico("./config/teste.txt")

problema.mover(1)
problema.pegar()
problema.soltar()

algoritmos.a_estrela(problema)
for movimento in problema.movimentos:
    print(movimento)

# print(f"Estado inicial: {problema.bases_caixas}")
# print(f"Custo: {problema.energia_gasta_total}")
# print("")
