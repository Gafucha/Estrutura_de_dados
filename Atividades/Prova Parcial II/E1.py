#Classe do indexador
class Indexador:
    #Construtor
    def __init__(self):
        self.ind = 0
        self.lista_pendente = Lista(int(input('Qual o tempo máximo do projeto')))
        self.lista_concluida = Lista(self.lista_pendente.tempo_projeto)
    #Função pra iniciar a interface
    def interf(self):
        self.ind = 0
        #Forçando o usuário a colocar um valor conhecido
        while self.ind != 1 and self.ind != 2 and self.ind != 3 and self.ind != 4 and self.ind != 5 and self.ind != 6:
            self.ind = int(input('~~~~~Interface do projeto~~~~~\n1. Inserir tarefa\n2. Concluir tarefa\n3. Calcular taxa de conclusão\n4. Calcular o tempo restante\n5. Relatório das tarefas\n6. Finalizar projeto'))
        match self.ind:
            #Inserir tarefa
            case 1:
                self.lista_pendente.inserir(input('Insira o nome da tarefa: '), int(input('Insira o tempo da tarefa: ')))
                self.interf()
            #Concluir tarefa / remover
            case 2:
                no = self.lista_pendente.concluir(input('Insira o nome da tarefa a ser removida: '))
                self.lista_concluida.inserir(no.nome, no.tempo_tarefa)
                self.interf()
            #Calcular taxa de conclusão
            case 3:
                arm = self.lista_concluida.inicio
                tempo_conc = int(0)
                tar_conc = int(0)
                #Verificando se a lista já está concluida
                while arm:
                    tempo_conc += arm.tempo_tarefa
                    tar_conc += 1
                    arm = arm.dir
                #Verificando se a lista concluida está cheia
                if tempo_conc == int(self.lista_pendente.tempo_projeto):
                    print('A lista já foi concluida')
                #Verificando se a lista concluida está vazia
                elif tempo_conc == 0:
                    print('A lista está em 0%')
                #Pegando o tempo da lista pendente
                else:
                    arm = self.lista_pendente.inicio
                    tar_pend = int(0)
                    #Juntando o valor pendente
                    while arm:
                        tar_pend += 1
                        arm = arm.dir
                    print(f'A taxa de conclusão do projeto é de: {(int(tar_pend) / (int(tar_pend) + int(tar_conc))) * 100}%')
                self.interf()
            #Calcular o tempo restante
            case 4:
                arm = self.lista_pendente.inicio
                temp_pend = int(0)
                #Juntando o valor pendente
                while arm:
                    temp_pend += arm.tempo_tarefa
                    arm = arm.dir
                print(f'O tempo restante é {self.lista_pendente.tempo_projeto - int(temp_pend)}')
                self.interf()
            #Relatório
            case 5:
                self.lista_pendente.imprimir()
                self.interf()
            #Encerrar
            case 6:
                arm = self.lista_concluida.inicio
                tempo_conc = int(0)
                #Verificando se a lista já está concluida
                while arm:
                    tempo_conc += arm.tempo_tarefa
                    arm = arm.dir
                #Verificando se a lista concluida não está cheia
                if tempo_conc != self.lista_pendente.tempo_projeto:
                    print('Não é possível encerrar, ainda há tarefas pendentes!\n')
                    self.interf()
                else:
                    print('Encerrando!')
#Classe Nó
class No:
    def __init__(self, nome, tempo_tarefa):
        self.nome = nome
        self.tempo_tarefa = tempo_tarefa
        self.esq = None
        self.dir = None
#Classe Lista
class Lista:
    #Construtor
    def __init__(self, tempo_projeto):
        self.inicio = None
        self.final = None
        self.tamanho = 0
        self.tempo_projeto = tempo_projeto
    #Função para inserir no final da lista
    def inserir(self, nome, tempo_tarefa):
        novo = No(nome, tempo_tarefa)
        #Verificando se a lista já está cheia
        arm = self.inicio
        temp_pend = int(0)
        #Juntando o valor pendente
        while arm:
            temp_pend += arm.tempo_tarefa
            arm = arm.dir
        #Verificando se a lista está cheia
        if temp_pend == self.tempo_projeto:
            print('A lista já está cheia!\n')
        #Verificando se o valor cabe
        elif temp_pend + novo.tempo_tarefa > self.tempo_projeto:
            print('O tempo da tarefa é grande demais para o escopo!\n')
        else:
            #Verificando se a lista está vazia
            if self.tamanho == 0:
                self.inicio = novo
                self.final = novo
            else: #Caso não esteja vazia
                self.final.dir = novo
                novo.esq = self.final
                self.final = novo
            self.tamanho += 1
            print('O valor foi inserido com sucesso\n')
    #Função para remover uma tarefa por nome da lista e retornar a tarefa removida
    def concluir(self, nome):
        if self.tamanho == 0: #Verificando se está vazia
            print('Não tem tarefas na lista para remover\n')
        else: #Tem tarefas na lista
            #Procurando pelo nome da tarefa
            arm = self.inicio
            #Chegando no fim da lista ou na tarefa com mesmo nome
            while arm != None and arm.nome != nome:
                arm = arm.dir
            #Se arm for None, ignora | Se arm tiver nome, apaga esse valor
            if arm is not None:
                if self.tamanho == 1: #Verificando se tem uma tarefa
                    self.inicio = None
                    self.final = None
                elif arm == self.inicio: #Verificando se é a primeira tarefa
                    arm.dir.esq = None
                    self.inicio = arm.dir
                    arm.dir = None
                elif arm == self.final: #Verificando se é a última tarefa
                    arm.esq.dir = None
                    self.final = arm.esq
                    arm.esq = None
                else: #É alguma tarefa do meio da lista
                    arm.esq.dir = arm.dir
                    arm.dir.esq = arm.esq
                    arm.esq = None
                    arm.dir = None
                self.tamanho -= 1
                return arm
    #Função pra calcular o tempo restante
    def temp_rest(self):
        arm = self.inicio
        while arm:
            totaltaref += int(arm.tempo_tarefa)
            arm = arm.dir
        res = self.tempo_projeto - totaltaref
        if(res == 0):
            print(f'O projeto já foi terminado e pode ser encerrado!\n')
        else:
            print(f'O tempo restante para terminar o projeto é {res}\n')
    #Função pra imprimir a lista de tarefas
    def imprimir(self):
        arm = self.inicio
        print('~~~~~Começo da lista~~~~~')
        while arm:
            print(arm.nome, end="  ")
            arm = arm.dir
        print('~~~~~Fim da lista~~~~~\n')


#Teste
index = Indexador()
index.interf()