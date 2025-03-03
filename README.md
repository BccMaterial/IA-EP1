# Braço Robótico

Dado um braço robótico que empilha caixas. Deve-se empilhar caixas com limite de 3 caixas por pilha sendo que a ordem das deixas deve ser por peso e colocar nas casas iniciais (à Esquerda)

O braço mecânico pode estica uma localização (+1 casa) ou todas as localizações (+4 casas). Considerar apenas o contexto bidirecional em que o robô usa a esquerda e direita.

Sugestão de configuração inicial:

```bash
                               | ------
                               |      |
                               | 
_10_  _30_  ____  _10_  ____ __|__ _40_  ____  _20_  ____  _30_ 
```

Assim, uma possível configuração final seria:

```bash
                               | ------
 10    10                      |      |
 30    20                      | 
_40_  _30_  ____  ____  ____ __|__ ____  ____  ____  ____  ____ 
```

Porém o software pode receber um arquivo txt que terá as configurações do problema. Ele terá o seguinte formato (desconsiderar o comentário):

```jsx
5 # número de posições ou bases
3 # tamanho máximo das pilhas
# caixas e valores serão cada linha abaixo no valor inicial
30 0 0 # uma caixa de 30kg no chão e nenhuma caixa na pilha na posição 0
20 0 0 # uma caixa de 20kg no chão e nenhuma caixa na pilha na posição 1
B # posição onde ficará o braço mecânico. posição 2
10 5 0 # uma caixa de 10kg e outra de 5kg em cima e nenhuma em cima na posição 3
7 2 1 # uma caixa de 7kg, outra de 2kg e uma de 1kg em cima na posição 4
```

A sua saída deverá ser um arquivo com a seguinte resposta

```jsx
# configuração final das 5 posições
30 20 10
7 5 2
B
1 0 0
0 0 0
# movimentos do braço mecânico até o estado final
E 1 P 20 2 # move para a esquerda, 1 casa e pega o pacote do topo. Gastou 2 de energia
E 1 S 20 5 # move para a esquerda, 1 casa e solta o pacote no topo. Gastou 5 de energia
...
```

Ao mover uma casa, há o custo de 1 de energia. Porém, mover mais de 2 casas, custa 75% do movimento. Por exemplo: 4 casas, custa 3 de energia. A cada 10kg, o custo aumenta em 1 energia, assim uma caixa de 20 kg, custa 2.

Exemplo: Mover 2 casas uma caixa de 40kg: 2*0,75 + 40/10 = 5,5 de energia
