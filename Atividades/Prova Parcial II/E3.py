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
            self.ind = int(input('~~~~~Interface do projeto~~~~~\n1.Inserir pessoa\n2. Colocar pessoas no trem\n3. Verificar fila\n4.Verificar lotação do trem\n5. Encerrar'))
        match self.ind:
            #Inserir pessoa
            case 1:
                self.dq.append('pessoa')
            case 2:
                self.trem.append(self.dq[0])
                self.dq.append

