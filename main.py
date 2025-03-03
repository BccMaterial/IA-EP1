def config_inicial(arquivo_configuracao): #Recebe um arquivo txt para configurar os dados iniciais
    # O arquivo txt deve seguir o seguinte padrão:
    # 5: Número de posições
    # 3: Altura máxima das pilhas(sempre será 3)
    # 30 0 0: Posição 0: caixa de 30kg no chão
    # 20 0 0: Posição 1: caixa de 20kg no chão
    # B: Posição 2 braço mecânico
    # 10 5 0: Posição 3: caixas de 10kg e 5kg empilhadas
    # 7 2 1: Posição 4: caixas de 7kg, 2kg e 1kg empilhadas

    with open(arquivo_configuracao, "r") as arquivo: #Utilizamos open para que o arquivo seja fechado automaticamente #"r" significa modo de leitura
        linhasArquivo = arquivo.read().strip().split("\n") #.strip() é utilizado para remover os espaços em branco e .split() é usado para transformar cada palavra em um elemento de uma lista

    numeroLinhas = int(linhasArquivo[0]) #O padrão do arquivo txt estabelece que a primeira linha define o número de posições
    numColunas = int(linhasArquivo[1]) #O padrão do arquivo txt estabelece que a segunda linha define a altura máxima da pilha

    basesPos = [] #Bases/número de posições das caixas
    posicaoBraco = None

    for i, linhasArquivo in enumerate(linhasArquivo[2:]): #enumarate é utilizado para conseguir encontrar a posição do braço
        if linhasArquivo.strip() == "B": #.strip() foi utilizado antes, mas a usei aqui novamente para adicionar uma camada extra de segurança
            posicaoBraco = i #Caso o braço seja encontrado no arquivo txt, guarda sua localização na variável posicaoBraco
            basesPos.append([]) #Adiciona um espaço vazio para o braço mecanico
        # Implementar :else:
