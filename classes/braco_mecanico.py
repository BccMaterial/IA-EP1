from . import arquivo
from .no import No

class BracoMecanico:
    # TODO: criar gerar_sucessores()
    # TODO: criar iniciar()
    # TODO: criar testar_objetivo()
    def __init__(self, arquivo_txt): #Recebe um arquivo txt para configurar os dados iniciais
        self.arquivo_txt = arquivo_txt
        self.posicao_braco = None
        self.energia_gasta_total = 0 # Começa com 0
        self.caixa_carregada = 0 # Começa carregando nenhuma caixa
        self.bases_caixas = [] # Slots das pilhas
        self.numero_linhas = 0 # Quantidade de bases
        self.numero_colunas = 0 # Altura máxima das pilhas
        self.movimentos = [] #Lista com todos os movimentos até o momento

        str_arquivo_txt = arquivo.ler(self.arquivo_txt)
        linhas_arquivo = str_arquivo_txt.strip().split("\n")
        self.numero_linhas = int(linhas_arquivo[0])
        self.numero_colunas = int(linhas_arquivo[1])
        
        for i, linha_arquivo in enumerate(linhas_arquivo[2:]): #Começa na posição 3, pois a posição 1 e 2 são usadas para setar valores[
            if linha_arquivo.strip() == "B": #Encontra a posição do braço(strip é utilizado novamente para adicionar uma camada de segurança extra)
                self.posicao_braco = i
                self.bases_caixas.append([]) #Adiciona lista vazia para representar o braço
            else:
                self.bases_caixas.append(list(map(int, linha_arquivo.split())))

    def gerar_sucessores():
        raise NotImplemented("gerar_sucessores não foi criado ainda")

    def iniciar(self):
        return No(self.posicao_braco)

    def testar_objetivo(self):
        """
        Requisitos:
        - Todas as pilhas devem estar em ordem decrescente (Exemplo de ordem do array: [30, 20, 10])
        - Todas as pilhas devem estar à esquerda (O tamanho de cada pilha deve ser descrescente: [3, 3, 2 ,1..])
        """
        todos_decrescentes = False
        todos_a_esquerda = False
        pilhas = self.bases_caixas

        # Valida se a pilha está descrescente
        def eh_decrescente(pilha):
            for i in range(1, len(pilha)):
                if pilha[i] > pilha[i-1]:
                    return False
            return True

        # Validação se a pilha está vazia (Coloquei numa função só por semântica)
        def pilha_vazia(pilha):
            return len(pilha) == 0

        # Itera todas as pilhas, verificando se existe alguma pilha fora de ordem
        for pilha in pilhas:
            if not eh_decrescente(pilha):
                todos_decrescentes = False
                break
            todos_decrescentes = True

        tamanho_pilhas = []
        for pilha in pilhas:
            # Se a pilha for vazia, então é a posição do braço (pulamos ela)
            if pilha_vazia(pilha):
                continue
            # Cria uma nova lista, sem os 0s
            pilha_limpa = [x for x in pilha if x != 0]
            # Insere o tamanho dessa lista em outro lugar
            tamanho_pilhas.append(len(pilha_limpa))
        todos_a_esquerda = eh_decrescente(tamanho_pilhas)

        return todos_decrescentes and todos_a_esquerda

    def custo(self, pos_desejada):
        custo = 0
        distancia = abs(pos_desejada - self.posicao_braco)

        if(distancia <= 2):
            custo += distancia
        else:
            custo += round(distancia * 0.75)
        
        # Caso self.caixa_carregada = 0, ele vai só adicionar 0
        custo += round(self.caixa_carregada / 10)
        return custo

    def movimento(self, pos_desejada):
        custo = self.custo(pos_desejada)
        self.energia_gasta_total += custo
        self.posicao_braco = pos_desejada
        self.movimentos.append(f"Foi para a posição {pos_desejada} e gastou {custo} de energia")

    def pegar(self):
        if self.bases_caixas[self.posicao_braco] and self.caixa_carregada == 0: #Verifica se existe uma caixa na posição do braco
            retiradas = 0
            while self.ver_topo_pilha_atual() == 0:
                self.caixa_carregada = self.bases_caixas[self.posicao_braco].pop() #Remove a caixa do topo da base com pop() e guarda ela na variavel do objeto
                retiradas += 1

            if len(self.bases_caixas[self.posicao_braco]) != 0:
                self.caixa_carregada = self.bases_caixas[self.posicao_braco].pop()

            while retiradas >= 0:
                self.bases_caixas[self.posicao_braco].append(0) 
                retiradas -= 1
            self.movimentos.append(f"Pegou a caixa na posição {self.posicao_braco} com peso {self.caixa_carregada}")

    def soltar(self):
        retiradas = 0
        while self.ver_topo_pilha_atual() == 0:
            self.bases_caixas[self.posicao_braco].pop()
            retiradas += 1

        if self.caixa_carregada != 0 and len(self.bases_caixas[self.posicao_braco]) < self.numero_colunas: #Verifica se o braco está carregando uma caixa e se a altura da pilha é menor que seu valor máximo
            self.bases_caixas[self.posicao_braco].append(self.caixa_carregada)
            self.movimentos.append(f"Soltou a caixa {self.caixa_carregada} na pilha {self.posicao_braco}")
            self.caixa_carregada = 0 #Remove a caixa da variável após colocar ela em outra pilha
            retiradas -= 1

        while retiradas > 0:
            self.bases_caixas[self.posicao_braco].append(0)
            retiradas -= 1


    def ver_topo_pilha_atual(self):
        if self.bases_caixas[self.posicao_braco]:
            return self.bases_caixas[self.posicao_braco][-1]
        else:
            return None

