class Lista:
    def __init__(self):
        #Variáveis
        self.arm = [] #Criando a lista principal
        self.armsec = [] #Criando uma lista secundária (sem repetição)
        self.armfreq = [] #Criando uma lista para o número de repetições (Contagem de repetições)

    
    ###Métodos
    #Preencher a lista
    def fill_list(self):
        #Variáveis
        i = int(1)
        quantItens = int(input('Quantos elementos você deseja inserir na lista? (Precisa ser inteiro e maior que zero): ')) #Solicitando número de itens da lista
        #Verificando os valores inseridos
        if(quantItens > 0): #Verificando se o número inserido é válido
            for i in range(1, quantItens+1): #Passando por cada item da lista
                val = int(0) #Resetando o valor da variável pra cair no while de novo
                while(val <= 0 or val > (4*quantItens)):
                    val = int(input(f'Insira um valor inteiro para o {i}º valor: '))#Inserção do valor, somente inteiros passam
                i+=1 #Contador
                self.arm.append(val) #Armazenando a entrada
        else: print('O valor inserido não é válido') #Preenchimento recusado
    
    #Checador de frequência
    def freq_check(self):
        #Montando as listas auxiliares
        for item in self.arm:
            loc = 0
            #Checando se a lista secundária está vazia
            if(len(self.armsec) == 0): #Está vazia, adicionar o primeiro elemento da tabela principal
                self.armsec.append(item)
                self.armfreq.append(1)
            else: #Não está vazia, iniciar a verificação de repetições
                #Verificando a repetição
                for itemsec in self.armsec: #Batendo as listas
                    if(int(itemsec) == int(item)): #Verificando se o valor já está na lista
                        loc = 1 #Já está na lista
                #Adicionando os valores correspondentes
                if(loc == 0): #Não estava na lista
                    self.armsec.append(item) #Adicionando o item na lista
                    self.armfreq.append(1) #Adicionando o número de repetições
                else: #Já estava na lista
                    self.armfreq[self.armsec.index(item)] += 1 #Adicionando mais uma repetição naquele valor
        #Verificando qual valor é o mais repetido
        freqmax = 0
        listamax = []
        #Pegando a maior frequência
        for itemfreq in self.armfreq: #Passando por cada item verificando qual a maior frequência
            if(itemfreq > freqmax): #Pegando a maior frequência
                freqmax =  itemfreq
        #Passando pela lista vendo quais números tem a maior frequência
        for item in self.armsec:
            if(self.armfreq[self.armsec.index(item)] == freqmax):
                listamax.append(item)
        #Verificando quantos itens tem a maior frequência
        if(len(listamax) == 1):
            print(f'O valor com a maior frequência é {listamax[0]}, com uma frequência de {freqmax}')
        elif(len(listamax) > 1 and len(listamax) < len(self.armsec)):
            print(f'Os valores com a maior frequência são {listamax}, todos com uma frequência de {freqmax}')
        else: print(f'Todos os valores apresentam a mesma frequência, sendo essa {freqmax}')              



#Teste do Código
lista = Lista() #Criando a lista
lista.fill_list() #Preenchendo a lista
lista.freq_check() #Verificando a frequência com que cada item se repete