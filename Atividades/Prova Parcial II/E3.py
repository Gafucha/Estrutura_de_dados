#Importando o deque
from collections import deque

#Classe do indexador
class Indexador:
    #Construtor
    def __init__(self):
        self.ind = 0
        self.dq = deque([])
        self.trem = deque([])
        self.ocup = 0
        vag = int(input('Insira o número de vagões do trem: '))
        ass = int(input('Insira o número de assentos do trem: '))
        self.max = vag * ass
    #Função pra iniciar a interface
    def interf(self):
        self.ind = 0
        #Forçando o usuário a colocar um valor conhecido
        while self.ind != 1 and self.ind != 2 and self.ind != 3 and self.ind != 4 and self.ind != 5:
            self.ind = int(input('~~~~~Interface do projeto~~~~~\n1. Inserir pessoa\n2. Colocar a primeira pessoa da fila no trem\n3. Verificar fila\n4. Verificar lotação do trem\n5. Encerrar\n'))
        match self.ind:
            #Inserir pessoa na fila
            case 1:
                self.dq.append(Pes(input('Insira o nome da pessoa: ')))
                print('Pessoa inserida com sucesso!\n')
                self.interf()
            #Colocando pessoa no trem
            case 2:
                if len(self.dq) == 0:
                    print('Não tem ninguém na fila do trem!\n')
                elif len(self.trem) < self.max:
                    self.trem.append(self.dq[0])
                    self.dq.popleft()
                    self.ocup += 1
                    print(f'{self.trem[len(self.trem)-1].nome} foi adicionada no trem\n')
                else:
                    print('O trem já está lotado!')
                self.interf()
            #Listar
            case 3:
                if self.ocup == 0:
                    print('A fila está vazia!')
                else:
                    for i in range(0, len(self.dq)):
                        print(f'{i+1}º Pessoa: {self.dq[i].nome}\n')
                self.interf()
            #Listar o trem e lotação
            case 4:
                if self.ocup == 0:
                    print('O trem está vazio!')
                else:
                    for i in range(0, len(self.trem)):
                        print(f'{i+1}º Pessoa: {self.trem[i].nome}\n')
                    print(f'\n A ocupação do trem atual é de {(self.ocup/self.max)*100}% de {self.max}, ou seja, {self.ocup} lugares estão ocupados')
                self.interf()
            #Encerramento
            case 5:
                print(f'Enviando o trem atual com: {self.ocup} pessoas...')
#Classe pra pessoa
class Pes:
    def __init__(self, nome):
        self.nome = nome


#Teste
index = Indexador()
index.interf()