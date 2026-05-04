#Criando a classe de Nó
class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
#Criando a classe de Lista
class Lista:
    #Definindo o construtor
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0
    #Função para inserir no final da lista
    def inserir(self, dado):
        novo = No(dado)
        #Verificando se a lista está vazia
        if self.tamanho == 0:
            self.inicio = novo
            self.final = novo
        else: #Caso não esteja vazia
           self.final.dir = novo
           novo.esq = self.final
           self.final = novo
        self.tamanho += 1
    #Função pra inserir o dado na posição desejada
    def inserirpos(self, dado, pos):
        novo = No(dado)
        #Verificando se a posição está dentro da lista
        if pos <= self.tamanho and self.tamanho != 0:
            if pos == 0:
                print(f"A lista começa na posição 1 (O valor {dado} não foi inserido)")
            else:
                #Verificando se é a primeira posição
                if pos == 1:
                    self.inicio.esq = novo
                    novo.dir = self.inicio
                    self.inicio = novo
                else: #Não é a primeira posição da lista
                    #Inserindo o valor dentro da lista na posição certa
                    arm = self.inicio
                    for i in range(self.tamanho):
                        if i+1 == pos:
                            #Colocando o valor na posição
                            arm.esq.dir = novo
                            novo.esq = arm.esq
                            novo.dir = arm
                            arm.esq = novo
                            #Passando para o próximo elemento
                        arm = arm.dir
        else: #Se o valor for maior que a lista só insere no final
            self.inserir(dado)
    #Função para imprimir a lista
    def imprimir(self):
        arm = self.inicio
        while arm:
            print(arm.dado, end="  ")
            arm = arm.dir
    #Função para remover um valor da lista
    def remover(self, dado):
        #Procurando pelo valor
        arm1 = self.inicio
        arm = None
        while arm1:
            if arm1.dado == dado:
                arm = arm1
            arm1 = arm1.dir
        #Se arm for None, ele pula. Se arm tiver valor, apaga esse valor
        if arm is not None:
            if self.tamanho == 1: #Verificando se só tem um elemento
                self.inicio = None
                self.final = None
            elif arm == self.inicio: #Verificando se é o primeiro elemento
                arm.dir.esq = None
                self.inicio = arm.dir
                arm.dir = None
            elif arm == self.final: #Verificando se é o último elemento
                arm.esq.dir = None
                self.final = arm.esq
                arm.esq = None
            else: #É algum valor dentro da lista, mas não é nenhum dos especificados acima
                arm.esq.dir = arm.dir
                arm.dir.esq = arm.esq
                arm.esq = None
                arm.dir = None
            arm = None
            self.tamanho -= 1

#Teste do código
lista = Lista()
lista.inserir(1)
lista.inserir(2)
lista.inserir(3)
lista.inserir(4)
lista.inserirpos(50, 3)
lista.imprimir()