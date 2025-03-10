from . import arquivo
from .no import No
import random

# Estado -> self.bases_caixas
# Aresta -> self.posicao_braco
# Custo -> no.aresta - no_destino.aresta

class BracoMecanico:
    def __init__(self, arquivo_txt=None, alinhamento="E"): #Recebe um arquivo txt para configurar os dados iniciais
        if alinhamento != "E" and alinhamento != "D":
            raise ValueError("Os possíveis valores para o alinhamento são E ou D.")
        self.alinhamento = alinhamento
        self.arquivo_txt = arquivo_txt
        self.posicao_braco = None
        self.base_braco = None
        self.energia_gasta_total = 0 # Começa com 0
        self.caixa_carregada = 0 # Começa carregando nenhuma caixa
        self.bases_caixas = [] # Slots das pilhas
        self.qtd_bases = 0 # Quantidade de bases
        self.altura_maxima = 0 # Altura máxima das pilhas
        self.total_caixas = 0

        if arquivo_txt is not None:
            str_arquivo_txt = arquivo.ler(self.arquivo_txt)
            linhas_arquivo = str_arquivo_txt.strip().split("\n")
            self.qtd_bases = int(linhas_arquivo[0])
            self.altura_maxima = int(linhas_arquivo[1])
            
            for i, linha_arquivo in enumerate(linhas_arquivo[2:]): #Começa na posição 3, pois a posição 1 e 2 são usadas para setar valores[
                if linha_arquivo.strip() == "B": #Encontra a posição do braço(strip é utilizado novamente para adicionar uma camada de segurança extra)
                    self.posicao_braco = i
                    self.base_braco = i
                    self.bases_caixas.append([]) #Adiciona lista vazia para representar o braço
                else:
                    base = list(map(int, linha_arquivo.split()))
                    self.total_caixas += len([x for x in base if x != 0])
                    self.bases_caixas.append(base)
        else:
            self.qtd_bases = 5
            self.altura_maxima = 3
            self.base_braco = random.choice(range(self.qtd_bases))
            self.posicao_braco = self.base_braco
            
            for i in range(self.qtd_bases):
                if i == self.base_braco:
                    self.bases_caixas.append([])
                    continue
                # Definir quantidade de caixas na pilha
                quantidade_caixas = random.randint(0, self.altura_maxima)
                pilha = []
                for _ in range(quantidade_caixas):
                    self.total_caixas += 1
                    # Definir valores das caixas de forma aleatória
                    pilha.append(random.randint(1, 45))

                # Preencher o que sobrou com 0
                for _ in range(self.altura_maxima - quantidade_caixas):
                    pilha.append(0)

                self.bases_caixas.append(pilha)

    def gerar_sucessores(self, no):
        possiveisBases = self.bases_caixas 
        carregando_caixa = self.caixa_carregada != 0
        sucessores = []
        
        possiveisIndices = [x for x in range(len(possiveisBases)) if len(possiveisBases[x]) != 0]
        random.shuffle(possiveisIndices)
        for i in possiveisIndices:
            no_sucessor = None
            if carregando_caixa:
                # Vai retornar um no
                no_sucessor = self.mover_e_soltar(no, i)
            else:
                # Vai retornar um no
                no_sucessor = self.pegar_e_mover(no, i)

            if no_sucessor is not None:
                sucessores.append(no_sucessor)

        return sucessores


    def iniciar(self):
        return No(self.to_hashable(self.bases_caixas), None, "N 0")

    def testar_objetivo(self, no):
        """
        Requisitos:
        - Todas as pilhas devem estar em ordem decrescente (Exemplo de ordem do array: [30, 20, 10])
        - Todas as pilhas devem estar à esquerda (O tamanho de cada pilha deve ser descrescente: [3, 3, 2 ,1..])
        """
        todos_decrescentes = False
        todos_alinhados = False
        pilhas = self.to_list(no.estado)
        total_caixas = 0

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
            total_caixas += self.pilha_tamanho(pilha)
            if not eh_decrescente(pilha):
                return False
            todos_decrescentes = True

        tamanho_pilhas = []
        for pilha in pilhas:
            # Se a pilha for vazia, então é a posição do braço (pulamos ela)
            if pilha_vazia(pilha):
                continue
            # Insere o tamanho dessa lista em outro lugar
            tamanho_pilhas.append(self.pilha_tamanho(pilha))
        max_pilhas = self.total_caixas // self.altura_maxima
        pilha_sobrando = self.total_caixas % self.altura_maxima
        if self.alinhamento == "E":
            todos_alinhados =   all(x == self.altura_maxima for x in tamanho_pilhas[:max_pilhas]) and\
                                tamanho_pilhas[max_pilhas] == pilha_sobrando
        else:
            todos_alinhados =   all(x == self.altura_maxima for x in tamanho_pilhas[len(tamanho_pilhas) - max_pilhas:]) and\
                                tamanho_pilhas[max_pilhas * (- 1)]
        
        return todos_decrescentes and todos_alinhados and self.total_caixas == total_caixas

    def calcular_custo(self, pos_desejada, pos_inicial=None):
        # TODO: implementar adicionar no & no_sucessor nos parametros
        custo = 0
        distancia = abs(pos_desejada - self.posicao_braco)
    
        if pos_inicial is not None:
            distancia = abs(pos_desejada - pos_inicial)

        if(distancia <= 2):
            custo += distancia
        else:
            custo += round(distancia * 0.75)
        
        # Caso self.caixa_carregada = 0, ele vai só adicionar 0
        custo += round(self.caixa_carregada / 10)
        return custo

    def custo(self, no, no_destino):
        # Aresta = Indice do braço robótico no nó
        return no_destino.custo


    def mover(self, pos_desejada):
        custo = self.calcular_custo(pos_desejada)
        self.energia_gasta_total += custo
        self.posicao_braco = pos_desejada
        # self.movimentos.append(f"Foi para a posição {pos_desejada} e gastou {custo} de energia")

    def pegar(self):
        # Verifica se existe uma caixa na posição do braco e se está tentando pegar uma caixa na base do braço
        if self.bases_caixas[self.posicao_braco] and self.caixa_carregada == 0 and self.posicao_braco != self.base_braco: 
            retiradas = 0

            if self.pilha_vazia(self.bases_caixas[self.posicao_braco]):
                return

            while self.ver_topo_pilha_atual() == 0:
                self.caixa_carregada = self.bases_caixas[self.posicao_braco].pop() #Remove a caixa do topo da base com pop() e guarda ela na variavel do objeto
                retiradas += 1

            if len(self.bases_caixas[self.posicao_braco]) != 0 and self.ver_topo_pilha_atual() != 0:
                self.caixa_carregada = self.bases_caixas[self.posicao_braco].pop()
                # self.movimentos.append(f"Pegou a caixa na posição {self.posicao_braco} com peso {self.caixa_carregada}")

            while retiradas >= 0:
                self.bases_caixas[self.posicao_braco].append(0) 
                retiradas -= 1

    def soltar(self):
        retiradas = 0

        if self.ver_topo_pilha_atual() == 0:
            self.bases_caixas[self.posicao_braco].pop()
            retiradas += 1

        while self.ver_topo_pilha_atual() == 0:
            self.bases_caixas[self.posicao_braco].pop()
            retiradas += 1

        # Verifica se o braco está carregando uma caixa, se a altura da pilha é menor que seu valor máximo e se está tentando soltar uma caixa na base do braço
        if self.caixa_carregada != 0 and len(self.bases_caixas[self.posicao_braco]) < self.altura_maxima and self.posicao_braco != self.base_braco:
            self.bases_caixas[self.posicao_braco].append(self.caixa_carregada)
            # self.movimentos.append(f"Soltou a caixa {self.caixa_carregada} na pilha {self.posicao_braco}")
            self.caixa_carregada = 0 # Remove a caixa da variável após colocar ela em outra pilha
            retiradas -= 1

        while retiradas > 0:
            self.bases_caixas[self.posicao_braco].append(0)
            retiradas -= 1

    def pegar_e_mover(self, no, pos):
        pos_anterior = self.posicao_braco
        self.pegar()
        self.mover(pos)
        custo = self.calcular_custo(pos, pos_anterior)
        estado_sucessor = self.bases_caixas
        casas_movidas = abs(pos_anterior - pos)
        dir_movimento = "E" if pos_anterior - pos > 0 else "D"
        caixa = self.caixa_carregada
        return No(self.to_hashable(estado_sucessor), no, f"{dir_movimento} {casas_movidas} P {caixa} {custo}", custo, self.heuristica(no))

    def mover_e_soltar(self, no, pos):
        pos_anterior = self.posicao_braco
        caixa = self.caixa_carregada
        self.mover(pos)
        self.soltar()
        custo = self.calcular_custo(pos, pos_anterior)
        estado_sucessor = self.bases_caixas
        casas_movidas = abs(pos_anterior - pos)
        dir_movimento = "E" if pos_anterior - pos > 0 else "D"
        return No(self.to_hashable(estado_sucessor), no, f"{dir_movimento} {casas_movidas} S {caixa} {custo}", custo, self.heuristica(no))

    def ver_topo_pilha_atual(self):
        if self.bases_caixas[self.posicao_braco]:
            return self.bases_caixas[self.posicao_braco][-1]
        else:
            return None

    def heuristica(self, no):
        posAtual = self.posicao_braco
        arestaSplitada = no.aresta.split(" ")
        dir_mov = arestaSplitada[0]
        casas_movidas = int(arestaSplitada[1])
        posObj = 0

        if dir_mov == "E":
            posObj = posAtual - casas_movidas
        elif dir_mov == "D":
            posObj = posAtual + casas_movidas

        return abs(posAtual - posObj)
    
    def to_hashable(self, estado):
        return tuple([tuple(x) if len(x) > 0 else tuple() for x in estado])

    def to_list(self, estado):
        return list([list(x) for x in estado]) 

    def pilha_tamanho(self, pilha):
        return len([x for x in pilha if x != 0])

    def pilha_vazia(self, pilha):
        return len([x for x in pilha if x != 0]) == 0

