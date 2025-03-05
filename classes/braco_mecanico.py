class BracoMecanico:
    def __init__(self, arquivo_configuracao): #Recebe um arquivo txt para configurar os dados iniciais
        with open(arquivo_configuracao, "r") as arquivo: #Utilizamos open para que o arquivo seja fechado automaticamente #"r" significa modo de leitura
            linhas_arquivo = arquivo.read().strip().split("\n") #.strip() é utilizado para remover os espaços em branco e .split() é usado para transformar cada palavra em um elemento de uma lista

        self.numero_linhas = int(linhas_arquivo[0]) #O padrão do arquivo txt estabelece que a primeira linha define o número de posições
        self.num_colunas = int(linhas_arquivo[1]) #O padrão do arquivo txt estabelece que a segunda linha define a altura máxima da pilha(com limite de 3 caixas por pilha)

        self.posicao_bases = [] #Bases/número de posições das caixas
        self.posicao_braco = None

        for i, linhas_arquivo in enumerate(
                linhas_arquivo[2:]): #enumarate é utilizado para conseguir encontrar a posição do braço
            if linhas_arquivo.strip() == "B": #.strip() foi utilizado antes, mas a usei aqui novamente para adicionar uma camada extra de segurança
                self.posicao_braco = i #Caso o braço seja encontrado no arquivo txt, guarda sua localização na variável posicaoBraco
                self.posicao_bases.append([]) #Adiciona um espaço vazio para o braço mecânico
            else:
                caixas = list(map(int, linhas_arquivo.split())) #A partir da lista linhasArquivo, transforma cada elemento em uma lista própria
                self.posicao_bases.append(caixas) #Adiciona cada uma das listas dentro da lista posicaoBases

    def return_essenciais(self):
        return self.numero_linhas, self.num_colunas, self.posicao_bases, self.posicao_braco
    def custo_movimento(self, posicao_desejada): #Somente o custo de movimento do braço(sem incluir caixas)
        distancia = abs(posicao_desejada - self.posicao_braco) #abs é utilizado para garantir que seja retornada uma distância positiva

        if distancia <= 2:
            return distancia
        else:
            return distancia * 0.75 #Se for maior que 2 retorna 75 porcento do custo
        #OBS: a função deve estar funcionando normalmente, mas é melhor testar um pouco mais depois
    def pegar_caixa(self): #Pega a caixa na posição do braço
        if self.posicao_bases[self.posicao_braco]: #Verifica se existe uma base na posição do braço
            self.posicao_bases[self.posicao_braco].pop() #











