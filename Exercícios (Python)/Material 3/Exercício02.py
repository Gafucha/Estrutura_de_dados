class Carrinho:
    def __init__(self):
        #Variáveis
        self.prod = []
        self.prec = []
        self.quant = []
        
    ###Métodos
    #Adicionando um item
    def additem(self, prod: str, prec: float, quant: int):
        if quant > 0:
            self.prod.append(prod)
            self.prec.append(prec)
            self.quant.append(quant)
        else: print('A quantidade inserida está errada...')


    #Removendo um item da lista
    def delitem(self, val: str):
        self.prec.pop(self.prod.index(val))
        self.quant.pop(self.prod.index(val))
        self.prod.pop(self.prod.index(val))

    
    #Atualizar item
    def upditem(self, prod: str, quant: int):
        self.quant[self.prod.index(prod)] = quant
        print('Quantidade alterada com sucesso')

    #Cálculo total
    def calcttl(self):
        index = -1
        soma = int(0)
        for item in self.quant:
            index+=1
            soma += (self.prec[index] * self.quant[index])
        print('O valor devido é:', soma)
    
    #Listador de itens
    def lister(self):
        index = -1
        for item in self.quant:
            index+=1
            print('Item', index, ' - ', 'Produto:', self.prod[index], '| Preço:', self.prec[index], '| Quantidade:', self.quant[index])



###Execução do código
carro = Carrinho()
carro.additem('Carvão', 5.0, 2)
carro.additem('Espeto de Carne', 7.8, 2)
carro.additem('Espeto de Frango', 5.6, 3)
carro.additem('Espeto de Linguiça', 4.7, 1)
print(carro.prod)
carro.delitem('Espeto de Linguiça')
print(carro.prod)
carro.calcttl()
carro.lister()