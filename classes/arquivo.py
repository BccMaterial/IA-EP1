def tupla_to_string(tuplas):
    return "\n".join(" ".join(map(str, sub_tupla)) for sub_tupla in tuplas)


def ler(caminho):
    str_arquivo = ""
    with open(caminho, "r") as arquivo:
        str_arquivo = arquivo.read()
    return str_arquivo

def escrever(caminho, arquivo):
    with open(arquivo, "w+") as arquivo:
        for i, pilhas in enumerate(caminho):
            arquivo.write(f"Passo {i} \n")
            for pilha in pilhas:
                arquivo.write(" ".join(map(str, pilha)) + "\n")
            arquivo.write("\n")
