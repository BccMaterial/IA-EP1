from classes import BracoMecanico, algoritmos, arquivo
from copy import deepcopy

problema = BracoMecanico()
problema_a_estrela = deepcopy(problema)
print("Solução por A*")
print("-----------------------------------------------------------------------")
print(f"Estado Inicial: {problema_a_estrela.to_hashable(problema_a_estrela.bases_caixas)}")
resultado = algoritmos.a_estrela(problema_a_estrela)
if resultado[1] is not None:
    print(f"Solução encontrada: {resultado[1]}")
    print(f"Número de iterações: {resultado[0]}")
else:
    print(f"Não foi encontrada nenhuma solução (Número de iterações: {resultado[0]})")

print()

problema_dijkstra = deepcopy(problema)
print("Solução por Dijkstra")
print("-----------------------------------------------------------------------")
print(f"Estado Inicial: {problema_dijkstra.to_hashable(problema_dijkstra.bases_caixas)}")
resultado = algoritmos.dijkstra(problema_dijkstra)
if resultado[1] is not None:
    print(f"Solução encontrada: {resultado[1]}")
    print(f"Número de iterações: {resultado[0]}")
else:
    print(f"Não foi encontrada nenhuma solução (Número de iterações: {resultado[0]})")

print()

problema_greedy = deepcopy(problema)
print("Solução por Greedy")
print("-----------------------------------------------------------------------")
print(f"Estado Inicial: {problema_greedy.to_hashable(problema_greedy.bases_caixas)}")
resultado = algoritmos.greedy(problema_greedy)
if resultado[1] is not None:
    print(f"Solução encontrada: {resultado[1]}")
    print(f"Número de iterações: {resultado[0]}")
else:
    print(f"Não foi encontrada nenhuma solução (Número de iterações: {resultado[0]})")

no = resultado[1] #Pega o nó na segunda posição da tupla
movimentos = algoritmos.no_caminho_aresta(no)

no_estado = no.estado
no_estado = arquivo.tupla_to_string(no_estado)

print(no_estado)
print(movimentos)

arquivo.escrever("./output", "example3.txt", movimentos, no_estado)




