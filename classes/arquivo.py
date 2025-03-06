def ler(caminho):
    str_arquivo = ""
    with open(caminho, "r") as arquivo:
        str_arquivo = arquivo.read()
    return str_arquivo
