from classes import BracoMecanico, algoritmos, arquivo
from copy import deepcopy
import os

print("Obs.: Caso o arquivo não exista, ou não seja passado nenhum, as pilhas serão sorteadas")
caminho = input("Insira o caminho do arquivo de configuração: ")

if caminho is None or caminho == "":
    print("Caminho não foi enviado. Sorteando pilhas...")
    caminho = None
elif os.path.isfile(caminho):
    print("Caminho não encontrado. Sorteando pilhas...")

problema = BracoMecanico(caminho)
problema_a_estrela = deepcopy(problema)
print("Solução por A*")
print("-----------------------------------------------------------------------")
print(f"Estado Inicial: {problema_a_estrela.to_hashable(problema_a_estrela.bases_caixas)}")
print()

resultado_a_estrela = algoritmos.a_estrela(problema_a_estrela)
if resultado_a_estrela[1] is not None:
    print(f"Solução encontrada: {resultado_a_estrela[1]}")
    print(f"Número de iterações: {resultado_a_estrela[0]}")
else:
    print(f"Não foi encontrada nenhuma solução (Número de iterações: {resultado_a_estrela[0]})")

print()

#Gera o arquivo txt do resultado com a_estrela:
no_a_estrela = resultado_a_estrela[1]
movimentos_a_estrela = algoritmos.no_caminho_aresta(no_a_estrela)
no_estado_a_estrela = arquivo.tupla_to_string(no_a_estrela.estado)
arquivo.escrever("./output/a_estrela_sol.txt", movimentos_a_estrela, no_estado_a_estrela)

#Solução com dijkstra:
problema_dijkstra = deepcopy(problema)
print("Solução por Dijkstra")
print("-----------------------------------------------------------------------")
print(f"Estado Inicial: {problema_dijkstra.to_hashable(problema_dijkstra.bases_caixas)}")
resultado_dijkstra = algoritmos.dijkstra(problema_dijkstra)
if resultado_dijkstra[1] is not None:
    print(f"Solução encontrada: {resultado_dijkstra[1]}")
    print(f"Número de iterações: {resultado_dijkstra[0]}")
else:
    print(f"Não foi encontrada nenhuma solução (Número de iterações: {resultado_dijkstra[0]})")

print()

#Gera o arquivo txt do resultado com dijkstra:
no_dijkstra = resultado_dijkstra[1]
movimentos_dijkstra = algoritmos.no_caminho_aresta(no_dijkstra)
no_estado_dijkstra = arquivo.tupla_to_string(no_dijkstra.estado)
arquivo.escrever("./output/dijkstra_sol.txt", movimentos_dijkstra, no_estado_dijkstra)

#Solução com greedy:
problema_greedy = deepcopy(problema)
print("Solução por Greedy")
print("-----------------------------------------------------------------------")
print(f"Estado Inicial: {problema_greedy.to_hashable(problema_greedy.bases_caixas)}")
resultado_greedy = algoritmos.greedy(problema_greedy)
if resultado_greedy[1] is not None:
    print(f"Solução encontrada: {resultado_greedy[1]}")
    print(f"Número de iterações: {resultado_greedy[0]}")
else:
    print(f"Não foi encontrada nenhuma solução (Número de iterações: {resultado_greedy[0]})")

no_greedy = resultado_greedy[1]
movimentos_greedy = algoritmos.no_caminho_aresta(no_greedy)
no_estado_greedy = arquivo.tupla_to_string(no_greedy.estado)
arquivo.escrever("./output/greedy_sol.txt", movimentos_greedy, no_estado_greedy)


