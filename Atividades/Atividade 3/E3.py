import random
class No:
    #Definindo o construtor
    def __init__(self, tick, nome, setor, cota, qtd, tipo):
        self.cod = int(random.randint(1, 9999))
        self.tick = str(tick)
        self.nome = str(nome)
        self.setor = str(setor)
        self.cota = float(cota)
        self.qtd = int(qtd)
        self.tipo = str(tipo)
        self.esq = None
        self.dir = None
class Lista:
    #Definindo o construtor
    def __init__(self):
        self.raiz = None
    #Método para inserir
    def inserir(self, novo):
        #Verificando se o valor está na lista
        while(self.buscar(novo.cod) != False):
            #Se o valor já estiver na lista, gera outro número, até a chave ser única
            novo.cod = int(random.randint(1000, 9999))
        #No caso do elemento não estar na lista, inserir ele
        #Verificando se a lista está vazia
        if(self.raiz is None):
            #Se estiver vazia adicionar o nó como raiz
            self.raiz = novo
        else: #No caso de não estar vazia, usar o inserir recursivo
            self._inserir(self.raiz, novo)
        print(f'\nO ativo "{novo.tick}" foi adicionado com sucesso! (Código do ativo: {novo.cod})')
    #Método da inserção recursivo
    def _inserir(self, no_atual, novo):
        #Se o novo for menor que o nó atual, ir para a esquerda
        if(novo.cod < no_atual.cod):
            #Se a esquerda estiver vazia, inserir ali
            if(no_atual.esq is None):
                no_atual.esq = novo
            else: #Se a esquerda tiver elemento, chamar a recursividade para esquerda
                self._inserir(no_atual.esq, novo)
        else: #No caso do novo ser maior que o valor atual, ir para a direita
            #Se a direita estiver vazia, inserir a ali mesmo
            if(no_atual.dir is None):
                no_atual.dir = novo
            else: #Se a direita tiver um elemento, chamar a recursividade para direita
                self._inserir(no_atual.dir, novo)
    #Método para buscar dentro da lista (Basicamente passa a raiz adiante)
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)
    #Método recursivo de busca
    def _buscar(self, no_atual, valor):
        #Se o nó atual estiver vazio, retornar falso
        if(no_atual is None):
            return False
        #Se o nó atual for o que procuramos, retornar verdadeiro
        if(no_atual.cod == valor):
            return no_atual
        #No caso de não ser nenhum dos dois, continuar procurando pra esquerda
        if(valor < no_atual.cod):
            return self._buscar(no_atual.esq, valor)
        #No caso de não estar para a esquerda, procurar para a direita
        return self._buscar(no_atual.dir, valor)
    #Método para remover elementos (Filtragem)
    def remover(self, valor):
        #Verificando se o valor procurado está na lista
        if(self.buscar(valor) == False):
            #Se não achar, printar erro
            print(f"O código {valor} não existe na árvore.")
            #Encerrar o código se não achar
            return
        #No caso de achar o valor na lista, passar a lista para o _remover()
        self.raiz = self._remover(self.raiz, valor)
        #Notificação pro usuário que foi removido
        print(f"Valor {valor} removido com sucesso.")
    #Método para remover recursivo (Remoção)
    def _remover(self, no_atual, valor):
        #Verifica se acabaram os elementos do ramo
        if(no_atual is None):
            return no_atual
        #Procura o valor pra esquerda
        if(valor < no_atual.cod):
            no_atual.esq = self._remover(no_atual.esq, valor)
        #Procura o valor pra direita
        elif(valor > no_atual.cod):
            no_atual.dir = self._remover(no_atual.dir, valor)
        #O valor foi encontrado
        else: #Descobrindo qual caso o valor se encontra
            #Verificando se o nó não tem filhos
            if(no_atual.esq is None and no_atual.dir is None): 
                return None
            #Verificando se o nó tem apenas um filho
            #O filho está na direita
            elif no_atual.esq is None:
                return no_atual.dir
            #O filho está na esquerda
            elif no_atual.dir is None:
                return no_atual.esq
            #Nesse caso, o nó possui dois filhos
            else:
                #Acha o menor valor da árvore da direita
                sucessor = self.menor(no_atual.dir)
                #Troca o nó atual pelo sucessor de valor mais próximo
                no_atual.cod = sucessor.cod
                #Remove o sucessor da subárvore direita
                no_atual.dir = self._remover(no_atual.dir, sucessor.cod)
        #Retorna o elemento atual para terminar a troca de lugares
        return no_atual
    #Método para achar o menor valor
    def menor(self, no):
        #Indo pra esquerda até não poder mais
        while(no.esq is not None):
            no = no.esq
            #Retorna o nó de valor mais baixo
        return no
    #Método pra calcular o valor patrimonial total de uma subárvore
    def patrimoniosub(self, valor):
        #Verificando se a árvore está vazia
        if(self.raiz == None):
            print('\nA árvore está vazia!')
        #Buscando o nó correspondente ao código informado
        else:
            no = self._buscar(self.raiz, valor)
            #Caso o código não exista na árvore
            if(no == False):
                print('\nAtivo não encontrado!')
            #Caso o ativo exista
            else:
                arm = []
                armcarteira = []
                subsoma = float(0)
                totsoma = float(0)
                #Reunindo todos os elementos da subárvore
                self._patrimoniosub(no, arm)
                #Reunindo todos os elementos da árvore
                self._patrimoniosub(self.raiz, armcarteira)
                #Calculando o valor patrimonial da subárvore (subsoma)
                #Passando por todos os elementos da lista
                for i in range(len(arm)):
                    subsoma += float(arm[i].cota * arm[i].qtd)
                #Calculando o valor patrimonial da árvore (totsoma)
                for i in range(len(armcarteira)):
                    totsoma += float(armcarteira[i].cota * armcarteira[i].qtd)
                #Calculando a participação percentual da subárvore
                part = (subsoma / totsoma) * 100
                #Exibindo os resultados
                print(f'\n~~~~~~~~~~Cálculo da subárvore~~~~~~~~~~')
                print(f'Ativo: {no.tick} (Código: {no.cod})\nValor próprio: R${no.cota * no.qtd}\nNúmero de ativos da subárvore: {len(arm)}\nValor patrimonial do nó: R${subsoma}\nParticipação no patrimônio total da carteira: {part:.2f}%')
    #Método recursivo pra calcular o valor patrimonial total e as outras informações
    def _patrimoniosub(self, no_atual, arm):
        #Verificando se o nó atual tem valor
        if(no_atual is not None): #Se tiver valor, percorrer
            #Percorrer o lado esquerdo
            self._patrimoniosub(no_atual.esq, arm)
            #Guardando o valor atual
            arm.append(no_atual)
            #Percorrer o lado direito
            self._patrimoniosub(no_atual.dir, arm)
        else:
            return
#####Menu de opções
arv = Lista()
ind = int(0)
#Travando o menu até o usuário inserir o número 6
while(ind != 6):
    #Escolha da função
    while(ind != 1 and ind != 2 and ind != 3 and ind != 4 and ind != 5 and ind != 6):
        try:
            #Solicitando input
            ind = int(input('Qual operação você deseja realizar?\n1. Cadastrar ativo\n2. Buscar ativo por código\n3. Atualizar cotação\n4. Retirar ativo da carteira\n5. Calcular valor patrimonial da subárvore\n6. Encerrar o código\nInsira apenas o número da operação desejada: '))
            if(ind > 6 or ind < 1): print('O número precisa ser entre 1 e 6...')
        except:
            print('Erro: O valor inserido precisa ser um número\n')
    #Execução da função escolhida
    match ind:
        #1. Cadastrar ativo
        case 1:
            #Criar um nó, repassar esse nó na inserção
            tick = str(input('\nInsira o ticker do ativo: '))
            nome = str(input('\nInsira o nome da empresa: '))
            setor = str(input('\nInsira o setor do ativo: '))
            try: #Verificação da cotação
                cota = float(input('\nInsira a cotação do ativo: '))
                try: #Verificação da quantidade
                    qtd = int(input('\nInsira a quantidade de cotas do ativo: '))
                    tipo = str(input('\nInsira o tipo do ativo: '))
                    #Adicionando os valores no novo nó
                    novo = No(tick, nome, setor, cota, qtd, tipo)
                    #Inserindo o novo nó na lista
                    arv.inserir(novo)
                except: #No caso da quantidade de cotas estar em formato errado, avisar e não adicionar o elemento
                    print('\nO valor inserido para a quantidade de cotas precisa ser um inteiro (O ativo não foi inserido)\n')
            except: #No caso da cotação estar errada, avisar e não adicionar o elemento
                print('\nO valor inserido para a cotação ser um float (O ativo não foi inserido)\n')
            ind = int(0)
        #2. Buscar ativo por código
        case 2:
            #Fazendo o usuário inserir um código válido
            try:
                busc = int(input('\nInsira o código de um ativo para buscar: '))
                arm = arv.buscar(busc)
                if(arm == False):
                    print('\nO ativo inserido não foi encontrado\n')
                else:
                    print(f'\nCódigo do ativo: {arm.cod}\nTicker: {arm.tick}\nNome da empresa: {arm.nome}\nSetor: {arm.setor}\nCotação: R${arm.cota}\nQuantidade de cotas: {arm.qtd}\nTipo do ativo: {arm.tipo}\nValor total em custódia: R${arm.cota * arm.qtd}\n')
            except:
                print('\nO código precisa ser numérico\n')
            ind = int(0)
        #3. Atualizar cotação
        case 3:
            try:
                busc = int(input('\nInsira o código de um ativo para buscar: '))
                arm = arv.buscar(busc)
                if(arm == False):
                    print('\nO ativo inserido não foi encontrado\n')
                else:
                    try:
                        arm.cota = float(input('insira a nova cota: '))
                    except:
                        print('\nA cota precisa ser numérica, o valor não foi atualizado\n')
            except:
                print('\nO código precisa ser numérico\n')
            ind = int(0)
        #4. Retirar ativo da carteira
        case 4:
            try:
                busc = int(input('\nInsira o código de um ativo para buscar: '))
                arm = arv.remover(busc)
            except:
                print('\nO código precisa ser numérico\n')
            ind = int(0)
        #5. Calcular valor patrimonial da subárvore
        case 5:
            try:
                busc = int(input('\nInsira o código de um ativo para buscar: '))
                arm = arv.patrimoniosub(busc)
            except:
                print('\nO Código inserido precisa ser numérico (Operação cancelada)\n')
            ind = int(0)
        #6. Encerrar
        case 6:
            print('Encerrando...')