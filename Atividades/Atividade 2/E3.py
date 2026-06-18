#Criando o Indexador
class Indexer:
    def __init__(self):
        self.ind = 0
        self.lista = Lista()
    #Função para iniciar o código
    def iniciar(self):
        self.ind = 0
        while self.ind != 1 and self.ind != 2 and self.ind != 3 and self.ind != 4 and self.ind != 5:
            self.ind = int(input('Qual operação você gostaria de realizar?\n1. Novo paciente\n2. Realizar atendimento\n3. Ver a fila para atendimento\n4. Buscar por um paciente\n5. Encerrar operações\nInsira apenas o número da operação: '))
        match self.ind:
            #1. Inserir paciente
            case 1:
                #Pedir o nome do paciente e a prioridade
                self.lista.inserir(input('Insira o nome do paciente: '), input('O paciente é prioridade? (sim ou não) '))
                self.iniciar()
            #2. Realizar atendimento
            case 2:
                self.lista.atender()
                self.iniciar()
            #3. Listar
            case 3:
                self.lista.imprimir()
                self.iniciar()
            #4. Buscar
            case 4:
                self.lista.buscar(input('Insira o nome do paciente: '))
                self.iniciar()
            #5. Cancelar
            case 5:
                print('Encerrando...')

#Criando a classe de Nó
class No:
    def __init__(self, dado, prioridade):
        self.dado = dado
        #Verificando prioridade
        if prioridade == 's' or prioridade == 'sim' or prioridade == 'S' or prioridade == 'Sim' or prioridade == 'SIM':
            self.prio = bool(True)
        else:
            self.prio = bool(False)
        self.pos = 0
        self.esq = None
        self.dir = None


#Criando a classe de Lista
class Lista:
    #Definindo o construtor
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0
    #Função para inserir o paciente
    def inserir(self, dado, prioridade):
        novo = No(dado, prioridade)
        arm = self.inicio
        #Verificando se a lista está vazia
        if self.tamanho == 0:
            self.inicio = novo
            self.final = novo
        else: #A lista não está vazia
            #Verificando se é prioridade
            if novo.prio == bool(True): #O paciente é prioridade
                #Verificando se o primeiro elemento é prioridade
                if self.inicio.prio == bool(False): #Não é prioridade
                    self.inicio.esq = novo
                    novo.dir = self.inicio
                    self.inicio = novo
                else: #O primeiro elemento é prioridade
                    #Verificar se o último elemento é prioridade
                    if self.final.prio == bool(False): #Não é prioridade
                        while arm.prio == bool(True): #Chegando no primeiro elemento não-prioridade
                            arm = arm.dir
                        arm.esq.dir = novo
                        novo.esq = arm.esq
                        novo.dir = arm
                        arm.esq = novo
                    else: #O último elemento é prioridade
                        self.final.dir = novo
                        novo.esq = self.final
                        self.final = novo
            else: #O paciente a ser adicionado não é prioridade
                self.final.dir = novo
                novo.esq = self.final
                self.final = novo
        self.tamanho += 1
        #Arrumar as posições
        self.posicionador()
    #Função pra remover o primeiro da fila
    def atender(self):
        #Verificando se tem mais de um elemento na lista
        if self.tamanho <= 1:
            self.inicio = None
            self.fim = None
            self.tamanho = 0
            print('A lista está vazia!')
        else:
            self.inicio = self.inicio.dir
            self.inicio.esq.dir = None
            self.inicio.esq = None
            self.posicionador()
            self.tamanho -= 1
    #Função para imprimir a lista
    def imprimir(self):
        arm = self.inicio
        while arm:
            if arm.prio == bool(True): print(f'O paciente {arm.dado} está na posição {arm.pos} e possui prioridade')
            else: print(f'O paciente {arm.dado} está na posição {arm.pos} e não possui prioridade')
            arm = arm.dir
    #Função para buscar um valor da lista
    def buscar(self, dado):
        #Procurando pelo valor
        arm1 = self.inicio
        arm = None
        while arm1:
            if arm1.dado == dado:
                arm = arm1
            arm1 = arm1.dir
        #Se arm for None, ele avisa que não encontrou
        if arm is not None:
            if arm.prio == bool(True): print(f'O paciente {arm.dado} está na posição {arm.pos} e possui prioridade')
            else: print(f'O paciente {arm.dado} está na posição {arm.pos} e não possui prioridade')
        else: print('Paciente não encontrado')
    #Função para arrumar a posição de todos na fila
    def posicionador(self):
        #Criando as variáveis pra arrumar a posição de todos os pacientes na fila
        arm = self.inicio
        i = 1
        #Passando por todos os elementos arrumando suas posições
        while arm:
            arm.pos = i
            arm = arm.dir
            i+=1


#Código
ind = Indexer()
ind.iniciar()   