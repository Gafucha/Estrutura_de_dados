#Criando o Indexador
class Indexer:
    def __init__(self):
        self.ind = 0
        self.lista = Lista()
    #Função para iniciar o código
    def iniciar(self):
        self.ind = 0
        while self.ind != 1 and self.ind != 2:
            self.ind = int(input('Qual operação você gostaria de realizar?\n1. Inserir processo\n2. Iniciar o programa\nInsira apenas o número da operação: '))
        match self.ind:
            #1. Inserir processo
            case 1:
                #Pedir o nome do processo e o tempo da tarefa
                self.lista.inserir(input('Insira o nome do processo? '), int(input('Quanto tempo o processo tem? ')))
                self.iniciar()
            #2. Iniciar programa
            case 2:
                self.lista.temproc = int(input('Quantas unidades de tempo serão usadas por processamento? '))
                self.lista.executar()
                self.iniciar()
#Criando a classe de Nó
class No:
    def __init__(self, dado, tempo_tarefa):
        self.dado = dado
        self.tempo_retorno = 0
        self.tempo_espera = 0
        self.tempo_tarefa = tempo_tarefa
        self.tempo_restante = tempo_tarefa
        self.esq = None
        self.dir = None
#Criando a classe de Lista
class Lista:
    #Definindo o construtor
    def __init__(self):
        self.inicio = None
        self.final = None
        self.conc_inicio = None
        self.conc_final = None
        self.conc_tamanho = 0
        self.temproc = 0
        self.tempo_total = 0
        self.tamanho = 0
    #Função para inserir no final da lista
    def inserir(self, dado, tempo_tarefa):
        novo = No(dado, tempo_tarefa)
        #Verificando se a lista está vazia
        if self.tamanho == 0:
            self.inicio = novo
            self.final = novo
        else: #Caso não esteja vazia
           self.final.dir = novo
           novo.esq = self.final
           self.final = novo
        self.tamanho += 1
    #Função pra jogar o primeiro elemento pro final
    def ciclar(self):
        #Verificando se tem mais de um elemento na lista
        if self.tamanho > 1: #Se tiver, ciclar o primeiro pro final
            self.inicio.dir.esq = None
            self.final.dir = self.inicio
            self.final = self.inicio
            self.inicio = self.inicio.dir
            self.final.dir = None
        self.executar()
    #Função para imprimir a lista concluida
    def relatorio(self):
        arm = self.conc_inicio
        print(f'A fatia de tempo selecionada foi {self.temproc}')
        while arm:
            print(f'\nProcesso: {arm.dado} | Tempo de execução: {arm.tempo_tarefa} | Tempo de espera: {arm.tempo_retorno - arm.tempo_tarefa} | Tempo de retorno: {arm.tempo_retorno}')
            arm = arm.dir
        self.tempo_med()
    #Função pra calcular o tempo médio
    def tempo_med(self):
        arm = self.conc_inicio
        arm1 = 0
        arm2 = 0
        while arm:
            arm.tempo_espera = arm.tempo_retorno - arm.tempo_tarefa
            arm1 += arm.tempo_espera
            arm2 += arm.tempo_retorno
            arm = arm.dir
        arm1 = arm1 / self.conc_tamanho
        arm2 = arm2 / self.conc_tamanho
        print(f'O tempo médio de espera foi {arm1}u e o tempo médio de retorno foi {arm2}')
    #Função execução
    def executar(self):
        #Verificar se a lista está preenchida
        if self.tamanho <= 0: #A lista está vazia
            print('A lista está vazia')
        else: #No caso da lista não estar vazia
            #Verificando se nessa execução o tempo da tarefa acabará
            if self.inicio.tempo_restante <= self.temproc: #Se o tempo restante for menor que o tempo de execução só executar o tempo restante
                #Registrando o tempo que foi utilizado
                self.tempo_total += self.inicio.tempo_restante
                #Zerando o tempo do processo
                self.inicio.tempo_restante = 0
                #Verificando se existe uma segunda posição
                if self.inicio.dir != None: #Existe uma segunda posição
                    #Verificando se a lista concluida está vazia
                    if self.conc_inicio == None: #Se estiver só colocar no inicio e final
                        self.inicio.tempo_retorno = self.tempo_total
                        self.conc_inicio = self.inicio
                        self.conc_final = self.inicio
                        self.inicio.dir.esq = None
                        self.inicio = self.inicio.dir
                        self.conc_inicio.dir = None
                        self.tamanho -=1
                        self.conc_tamanho += 1
                    else: #A lista concluida não está vazia
                        #Verificar se tem só um elemento na lista concluida
                        if self.conc_tamanho == 1:
                            self.inicio.tempo_retorno = self.tempo_total
                            self.inicio.esq = self.conc_inicio
                            self.conc_inicio.dir = self.inicio
                            self.inicio.dir.esq = None
                            self.conc_final = self.inicio
                            self.inicio = self.inicio.dir
                            self.tamanho -= 1
                            self.conc_tamanho += 1
                        else: #Tem mais de um elemento na lista concluida
                            self.inicio.tempo_retorno = self.tempo_total
                            self.conc_final.dir = self.inicio
                            self.inicio.esq = self.conc_final
                            self.conc_final = self.conc_final.dir
                            self.inicio.dir.esq = None
                            self.inicio = self.inicio.dir
                            self.conc_final.dir = None
                            self.tamanho -= 1
                            self.conc_tamanho += 1
                else: #Não existe uma segunda posição na lista
                    #Verificando se a lista concluida está vazia
                    if self.conc_inicio == None: #Se estiver só colocar no inicio e final
                        self.inicio.tempo_retorno = self.tempo_total
                        self.conc_inicio = self.inicio
                        self.conc_final = self.inicio
                        self.inicio = None
                        self.final = None
                        self.tamanho -=1
                        self.conc_tamanho += 1
                    else: #A lista concluida não está vazia
                        #Verificar se tem só um elemento na lista concluida
                        if self.conc_tamanho == 1:
                            self.inicio.tempo_retorno = self.tempo_total
                            self.inicio.esq = self.conc_inicio
                            self.conc_inicio.dir = self.inicio
                            self.conc_final = self.conc_final.dir
                            self.inicio = None
                            self.final = None
                            self.tamanho -= 1
                            self.conc_tamanho += 1
                        else: #Tem mais de um elemento na lista concluida
                            self.inicio.tempo_retorno = self.tempo_total
                            self.conc_final.dir = self.inicio
                            self.inicio.esq = self.conc_final
                            self.conc_final = self.conc_final.dir
                            self.inicio = None
                            self.final = None
                            self.tamanho -= 1
                            self.conc_tamanho += 1
            else: #O tempo restante é maior que o tempo de execução
                #Subtrair o tempo de execução do processo
                self.inicio.tempo_restante -= self.temproc
                self.tempo_total += self.temproc
            self.relatorio()
            #Ciclar
            self.ciclar()

#Teste código
indexador = Indexer()
indexador.iniciar()