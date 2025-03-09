def ler(caminho):
    str_arquivo = ""
    with open(caminho, "r") as arquivo:
        str_arquivo = arquivo.read()
    return str_arquivo

def escrever(caminho, string):
    with open(caminho, "w+") as arquivo:
        arquivo.write(string)
