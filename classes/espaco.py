import braco_mecanico
class espaco:
    def __init__(self, arquivo_txt):
        self.bases_caixas, self.tamanho_colunas, self.braco = self.ler_txt(arquivo_txt)
    def ler_txt(self, arquivo_txt): #Lê o arquivo de texto para setar os dados iniciais
        with open(arquivo_txt, "r") as arquivo:
            linhas_arquivo = arquivo.read().strip().split("\n") #Remove os espaços em branco e retorna uma lista separada por quebras de linhas

        numero_linhas = int(linhas_arquivo[0]) #A linha inicial sempre será o numero de linhas
        tamanho_colunas = int(linhas_arquivo[1]) #A segunda linha sempre será o tamanho das colunas

        bases_caixas = []
        posicao_braco = None

        for i, linha_arquivo in enumerate(linhas_arquivo[2:]): #Começa na posição 3, pois a posição 1 e 2 são usadas para setar valores[
            if linha_arquivo.strip() == "B": #Encontra a posição do braço(strip é utilizado novamente para adicionar uma camada de segurança extra)
                posicao_braco = i
                bases_caixas.append([]) #Adiciona lista vazia para representar o braço
            else:
                bases_caixas.append(list(map(int, linha_arquivo.split())))

        return bases_caixas, tamanho_colunas, braco_mecanico(posicao_braco)