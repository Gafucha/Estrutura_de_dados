#Criando a classe "Nó"
class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

#Criando a classe da Lista
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    #Função para adicionar no inicio
    def inserir_inicio(self, valor):
        novo = No(valor)
        
        #Verificando se a lista está vazia
        if self.tamanho == 0:            
            self.fim = novo            
        else:
            novo.dir = self.inicio
            self.inicio.esq = novo
            
        self.inicio = novo
        self.tamanho += 1
    #Função pra imprimir os valores da lista
    def printlist(self):
        aux = self.inicio
        while aux:
            print(aux.dado, end="  ")
            aux = aux.dir
    #Função para inserir um valor no final da lista
    def inserir_final(self, valor):
        novo = No(valor)
        #Verificando se a lista está vazia
        if self.tamanho == 0:
            self.inicio = novo
        else:
           self.fim.dir = novo
           novo.esq = self.fim

        self.fim = novo
        self.tamanho += 1
    #Função para pesquisar por um valor dentro da lista
    def pesquisar(self, valor):
        aux = self.inicio
        while aux:
            if aux.dado == valor:
                return aux
            aux = aux.dir
        return None
    #Função para remover um valor da lista
    def remover(self, valor):
        aux = self.pesquisar(valor)
        
        if aux is not None:
            if self.tamanho == 1: #Verifica se a lista tem apenas um valor
                self.inicio = None
                self.fim = None                
            elif aux == self.inicio: #Verifica se o elemento a ser removido é o primeiro elemento
                aux.dir.esq = None
                self.inicio = aux.dir
                aux.dir = None                
            elif aux == self.fim: #Verifica se o elemento a ser removido é o último elemento
                aux.esq.dir = None
                self.fim = aux.esq
                aux.esq = None
            else: #Não é o primeiro nem o último, e a lista está cheia, passar por cada elemento
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dir = None
            aux = None
            self.tamanho -= 1