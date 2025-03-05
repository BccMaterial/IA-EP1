class BracoMecanico:
    def __init__(self, posicao_braco): #Recebe um arquivo txt para configurar os dados iniciais
        self.posicao_braco = posicao_braco
        self.energia_gasta_total = 0 #Começa com 0
        self.caixa_carregada_braco = None #Começa carregando nenhuma caixa
        self.movimentos = [] #Lista com todos os movimentos até o momento

    def movimento(self, pos_desejada):
        distancia = abs(pos_desejada - self.posicao_braco) #Utiliza abs para garantir que seja um distancia positiva

        if(distancia <= 2):
            custo = distancia
        else:
            custo = round(distancia * 0.75)

        if self.caixa_carregada_braco is not None:
            self.energia_gasta_total += round(self.caixa_carregada_braco / 10) + 1

        self.energia_gasta_total += custo #Adiciona o custo do movimento atual para o objeto
        self.movimentos.append(f"Foi para a posição {pos_desejada} e gastou {custo} de energia")

    def pegar(self, espaco):
        if espaco.bases_caixas[self.posicao_braco]: #Verifica se existe uma caixa na posição do braco
            self.caixa_carregada_braco = espaco.bases_caixas[self.posicao_braco].pop() #Remove a caixa do topo da base com pop() e guarda ela na variavel do objeto
            custo = round(self.caixa_carregada_braco / 10) + 1 #A cada 10kg aumenta 1 de energia e utiliza round() para garantir que é um valor inteiro

            self.energia_gasta_total += custo #Adiciona a energia gasta no movimento atual para a variavel do objeto
            self.movimentos.append(f"Pegou a caixa de {self.caixa_carregada_braco} com custo de {custo}")

    def soltar(self, espaco): #Verificar depois se "!=" funciona
        if self.caixa_carregada_braco != None and len(espaco.bases_caixas[self.posicao_braco]) < espaco.tamanho_colunas: #Verifica se o braco está carregando uma caixa e se a altura da pilha é menor que seu valor máximo
            espaco.bases_caixas[self.posicao_braco].append(self.caixa_carregada_braco)
            custo = round((self.caixa_carregada_braco / 10)) + 1 #
