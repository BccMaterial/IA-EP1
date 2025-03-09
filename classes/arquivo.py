def tupla_to_string(tuplas):
    strings = [] #Linhas

    for tupla in tuplas:
        if not tupla: #Verifica se é a posição vazia do braco mecanico ()
            strings.append("B") #Adiciona B na string caso seja a pos do braço
            continue #Continua para o else quando encontra ()
        else:
            item = [str(item) for item in tupla]
            string = " ".join(item)
            strings.append(string)

    return  "\n".join(strings) #Quebra uma linha para imprimir de modo adequado


def ler(caminho):
    str_arquivo = ""
    with open(caminho, "r") as arquivo:
        str_arquivo = arquivo.read()
    return str_arquivo

def escrever(arquivo, movimentos, estado_final):
    with open(arquivo, "w+", encoding="utf-8") as arquivo:
        arquivo.write("Estado final: \n")
        for pilhas in estado_final:
            arquivo.write(" ".join(map(str, pilhas)))

        arquivo.write("\n")

        arquivo.write("Movimentos do braço até o estado objetivo: \n")
        for movimento in movimentos:
            arquivo.write(movimento + "\n")
