#Complexidade do algoritmo O(n^3)
class Lista:
    def __init__(self):
        #Variáveis
        self.arm = [] #Criando a lista


    ###Métodos
    #Preencher a lista
    def fill_list(self):
        #Variáveis
        i = int(1)
        val = int(0)
        quantItens = int(input('Quantos elementos você deseja inserir na lista? (Precisa ser inteiro e maior que zero): ')) #Solicitando número de itens da lista
        #Verificando os valores
        if(quantItens > 0): #Verificando se o número inserido é válido
            for item in range(quantItens): #Passando por cada item da lista
                val = int(input(f'Insira um valor inteiro para o {i}º valor: '))#Inserção do valor, somente inteiros passam
                i+=1 #Contador
                self.arm.append(val) #Armazenando a entrada
        else: print('O valor inserido não é válido') #Preenchimento recusado

    #Checador de soma
    def sumcheck(self):
        if(len(self.arm) >= 3): #Verificando existem elementos o suficiente 
            #Definindo variáveis
            exyn = 'n'
            #Passando pelos valores e verificando
            for i in range(2, len(self.arm)):
                for j in range(0, i-1):
                    for k in range(j+1, i):
                        if(self.arm[k] + self.arm[j] == self.arm[i]): #Verificando se a soma de dois elementos é igual ao terceiro
                            exyn = 'achou' #Variável de confirmação
                            print(f'itemk = {self.arm[k]}\nitemj = {self.arm[j]}\nitemi = {self.arm[i]}') #Imprimindo os valores que se enquadraram
            if(exyn == 'achou'): #Verificando se foi encontrado algum valor
                print('Existe um elemento que é soma de dois anteriores')
            else: #Não foi encontrado nenhum valor
                print('Nenhum elemento é a soma de dois anteriores')
        else:
            print('Não há valores o suficiente na lista pra realizar o cálculo')



#Teste do código
lista = Lista() #Criando a lista
lista.fill_list() #Preenchendo a lista
lista.sumcheck() #Verificando a soma