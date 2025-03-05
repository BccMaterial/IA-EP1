class BracoMecanico:
    def __init__(self, posicao_braco): #Recebe um arquivo txt para configurar os dados iniciais
        self.posicao_braco = posicao_braco
        self.energia_gasta_total = 0 #Começa com 0
        self.caixa_carregada_braco = None #Começa carregando nenhuma caixa
        self.movimentos = [] #Lista com todos os movimentos até o momento

    def movimento(self, pos_desejada):
        distancia = abs(pos_desejada - self.posicao_braco) #Utiliza abs para garantir que seja um distancia positiva
        custo = None

        if(distancia <= 2):
            self.energia_gasta_total += distancia
        else:
            self.energia_gasta_total += round(distancia * 0.75)

        if self.caixa_carregada_braco is not None: #Caso esteja carregando uma caixa, adiciona o custo de energia dela
            self.energia_gasta_total += round(self.caixa_carregada_braco / 10) + 1

        self.energia_gasta_total += custo #Adiciona o custo do movimento atual para o objeto
        self.movimentos.append(f"Foi para a posição {pos_desejada} e gastou {custo} de energia")

    def pegar(self, espaco):
        if espaco.bases_caixas[self.posicao_braco] and self.caixa_carregada_braco is None: #Verifica se existe uma caixa na posição do braco
            self.caixa_carregada_braco = espaco.bases_caixas[self.posicao_braco].pop() #Remove a caixa do topo da base com pop() e guarda ela na variavel do objeto
            self.movimentos.append(f"Pegou a caixa na posição {self.caixa_carregada_braco}")

    def soltar(self, espaco): #Verificar depois se "!=" funciona
        if self.caixa_carregada_braco is not None and len(espaco.bases_caixas[self.posicao_braco]) < espaco.tamanho_colunas: #Verifica se o braco está carregando uma caixa e se a altura da pilha é menor que seu valor máximo
            espaco.bases_caixas[self.posicao_braco].append(self.caixa_carregada_braco)
            self.movimentos.append(f"Soltou a caixa {self.caixa_carregada_braco} na pilha {espaco.bases_caixas[self.posicao_braco]}")
            self.caixa_carregada_braco = None #Remove a caixa da variável após colocar ela em outra pilha
