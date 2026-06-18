#O código não tem verificação de entrada, por favor inserir os valores como pedido
from collections import deque

#Criando o Indexador
class Indexer:
    def __init__(self):
        self.ind = 0
        self.rede = {}
    #Função para iniciar o código
    def iniciar(self):
        self.ind = 0
        while self.ind != 3:
            while self.ind != 1 and self.ind != 2 and self.ind != 3:
                self.ind = int(input('Qual operação você gostaria de realizar?\n1. Inserir processo\n2. Iniciar o programa\n3. Encerrar\nInsira apenas o número da operação: '))
            match self.ind:
                #1. Inserir roteador
                case 1:
                    #Obtendo os valores pra guardar o roteador novo
                    nome = str(input('Insira o nome do novo roteador: '))
                    conex = str(input('Insira as conexões do novo roteador (Separadas por espaço): ')).split()
                    #Adicionando o roteador no dicionário
                    self.rede[nome] = conex
                    self.ind = int(0)
                #2. Imprimir tabela (Roteador)
                case 2:
                    if len(self.rede) == 0:
                        print('A rede está vazia, não é possível iniciar o programa')
                        self.ind = int(0)
                    else:
                        #Obtendo a base para os caminhos
                        rot = input('Insira o nome do roteador base para a tabela: ')
                        #Gerando as variáveis necessárias
                        grafo = bidirec(self.rede)
                        dist, ant, ord = bfs(grafo, rot)
                        #Loop para passar por todos os elementos listando os caminhos mínimos
                        for r in grafo:
                            caminho = reconstruir_caminho(ant, rot, r)
                            #Verificando o caminho
                            if caminho: #Achou um caminho
                                print(f'{rot} -> {r}: {caminho}')
                            else: #Não achou um caminho
                                print(f'{rot} -> {r}: sem rota')
                        print(f'\nTabela de rotas a partir de {rot}\n')
                        self.ind = int(0)
                #3. Encerrar
                case 3:
                    print('Encerrando...')
#Função para executar o percurso em largura no grafo
def bfs(grafo, origem):
    #Definindo as distâncias
    distancia = {v: float('inf') for v in grafo}
    #Definindo o valor anterior
    anterior  = {v: None for v in grafo}
    #Distância da origem
    distancia[origem] = 0
    #Ordem de percurso
    ordem = []
    #Fazendo uma fila
    fila = deque([origem])
    #Percorrendo a fila
    while fila:
        u = fila.popleft()
        ordem.append(u)
        for v in grafo[u]:
            if distancia[v] == float('inf'):   #Ainda não visitado
                distancia[v] = distancia[u] + 1
                anterior[v]  = u
                fila.append(v)
    #Retornando os valores encontrados
    return distancia, anterior, ordem
#Função para reconstruir o caminho da base até o destino
def reconstruir_caminho(anterior, base, destino):
    #Destino não alcançado
    if destino != base and anterior[destino] is None:
        return []
    caminho = []
    atual = destino
    #Guardando o caminho do atual
    while atual is not None:
        caminho.append(atual)
        #Se o atual for o último elemento do caminho, inverter e retornar
        if atual == base:
            caminho.reverse()
            return caminho
        #Passando para o próximo elemento
        atual = anterior[atual]
    return []
#Função pra fazer a tabela ser bidirecional
def bidirec(rede):
    #Criando uma segunda tabela
    grafo2 = {v: list(vizinhos) for v, vizinhos in rede.items()}
    #Loop pra imprimir os caminhos
    for org in rede:
        #Verificando se destinho tem aquela origem
        for destino in rede[org]:
            if destino not in grafo2: #Não tem aquela origem
                grafo2[destino] = []
            if org not in grafo2[destino]: #Tem aquela origem
                grafo2[destino].append(org)
    return grafo2



###Teste de código
index = Indexer()
index.iniciar()