#Importando o deque
from collections import deque

#Classe do indexador
class Indexador:
    #Construtor
    def __init__(self):
        self.ind = 0
        self.dq = deque([])
        self.dqpago = deque([])
        self.max = input('Insira seu limite de gastos (Valor máximo para compras): ')
    #Função pra iniciar a interface
    def interf(self):
        self.ind = 0
        #Forçando o usuário a colocar um valor conhecido
        while self.ind != 1 and self.ind != 2 and self.ind != 3 and self.ind != 4 and self.ind != 5:
            self.ind = int(input('~~~~~Interface do projeto~~~~~\n1. Adicionar item no carrinho\n2. Pagar pelo item no topo do carrinho\n3. Listar itens no carrinho\n4. Calcular valor pago\n5. Finalizar a compra (Apaga a lista)'))
        match self.ind:
            #Inserir item no carrinho
            case 1:
                self.dq.appendleft()
                self.interf()
            #Pagar item do topo / remover
            case 2:
                item = Item(input('Insira o nome do produto'), input('Insira o preço do produto'))
                for i in range(0, len(self.dq.pago)):
                    total += self.dqpago[i].preco
                #Verificando se já está no limite
                if total == self.max:
                    print('Você já gastou seu valor limite!')
                #Verificando se vai caber
                elif total + item.preco > self.max:
                    print('Esse item estoura sua cota!')
                else:
                    self.dqpago.appendleft(Item(self.dq[0].nome, self.dq[0].preco))
                    self.dq.popleft()
                    print('Comprado com sucesso!')
                self.interf()
            #Listar
            case 3:
                for i in range(0, self.dq):
                    print(self.dq[i].nome,'\n')
                self.interf()
            #Calcular valor pago
            case 4:
                pago = 0
                for i in range(0, self.dqpago):
                    pago += self.dqpago[i].preco
                print(f'O valor pago até agora foi {pago}')
                self.interf()
            #Finalizar a compra
            case 5:
                print('Finalizando...') 
#Classe do item
class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = int(preco)



#Teste
index = Indexador()
index.interf()