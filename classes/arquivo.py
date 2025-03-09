def tupla_to_string(tuplas):
    return "\n".join(" ".join(str(i) if i else "B" for i in tupla_interior) for tupla_interior in tuplas)


def ler(caminho):
    str_arquivo = ""
    with open(caminho, "r") as arquivo:
        str_arquivo = arquivo.read()
    return str_arquivo

def escrever(caminho, arquivo, movimentos, estado_final):
    with open(arquivo, "w+", encoding="utf-8") as arquivo:
        arquivo.write("Estado final: \n")
        for pilhas in estado_final:
            arquivo.write(" ".join(map(str, pilhas)) + "\n")
            arquivo.write("\n")

        arquivo.write("Movimentos do braço até o estado objetivo: \n")
        for movimento in movimentos:
            arquivo.write(movimento + "\n")
