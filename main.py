from classes import BracoMecanico, algoritmos

problema = BracoMecanico("./config/teste.txt")

print(f"Estado Inicial: {problema.bases_caixas}")
resultado = algoritmos.a_estrela(problema)
if resultado[1] is not None:
    print(f"Solução encontrada: {resultado[1]}")
    print(f"Número de iterações: {resultado[0]}")
else:
    print(f"Não foi encontrada nenhuma solução (Número de iterações: {resultado[0]})")

