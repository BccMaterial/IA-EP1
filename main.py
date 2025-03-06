from classes import BracoMecanico

problema = BracoMecanico("./config/teste.txt")


print(f"Estado inicial: {problema.bases_caixas}")
print(f"Custo: {problema.energia_gasta_total}")
print("")

problema.movimento(1)
problema.pegar()
problema.movimento(0)
problema.soltar()
problema.movimento(3)
problema.pegar()
problema.movimento(0)
problema.soltar()
problema.movimento(3)
problema.pegar()
problema.movimento(1)
problema.soltar()
problema.movimento(4)
problema.pegar()
problema.movimento(3)
problema.soltar()
problema.movimento(4)
problema.pegar()
problema.movimento(3)
problema.soltar()
problema.movimento(4)
problema.pegar()
problema.movimento(1)
problema.soltar()
problema.movimento(3)
problema.pegar()
problema.movimento(1)
problema.soltar()

print(f"Estado final: {problema.bases_caixas}")
print(f"Custo: {problema.energia_gasta_total}")
print("")

if(problema.testar_objetivo()):
    print(f"Chegou em um estado objetivo")
else:
    print(f"Chegou em um estado inválido")
