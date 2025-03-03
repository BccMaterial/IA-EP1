def config_inicial(arquivo_configuracao): #Recebe um arquivo txt para configurar os dados iniciais e retorna dados essenciais

    with open(arquivo_configuracao, "r") as arquivo: #Utilizamos open para que o arquivo seja fechado automaticamente #"r" significa modo de leitura
        linhasArquivo = arquivo.read().strip().split("\n") #.strip() é utilizado para remover os espaços em branco e .split() é usado para transformar cada palavra em um elemento de uma lista

    numeroLinhas = int(linhasArquivo[0]) #O padrão do arquivo txt estabelece que a primeira linha define o número de posições
    numColunas = int(linhasArquivo[1]) #O padrão do arquivo txt estabelece que a segunda linha define a altura máxima da pilha(com limite de 3 caixas por pilha)

    posicaoBases = [] #Bases/número de posições das caixas
    posicaoBraco = None

    for i, linhasArquivo in enumerate(linhasArquivo[2:]): #enumarate é utilizado para conseguir encontrar a posição do braço
        if linhasArquivo.strip() == "B": #.strip() foi utilizado antes, mas a usei aqui novamente para adicionar uma camada extra de segurança
            posicaoBraco = i #Caso o braço seja encontrado no arquivo txt, guarda sua localização na variável posicaoBraco
            posicaoBases.append([]) #Adiciona um espaço vazio para o braço mecanico
        else:
            caixas = list(map(int, linhasArquivo.split())) #A partir da lista linhasArquivo, transforma cada elemento em uma lista própria
            posicaoBases.append(caixas) #Adiciona cada uma das listas dentro da lista posicaoBases

    return numeroLinhas, numColunas, posicaoBases, posicaoBraco #Posição bases é a lista inicial

def custo_movimento(posicaoAtual, posicaoDesejada): #Terminar de implementar
    distancia = abs(posicaoDesejada - posicaoAtual) #abs é utilizado para garantir que seja retornada uma distância positiva

    return distancia if distancia <= 2 else round(distancia * 0.75) #VERIFICAR
