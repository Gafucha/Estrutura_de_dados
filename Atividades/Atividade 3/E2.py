import random
class No:
    def __init__(self, conti, nome, nomeci, qtd):
        self.cod = int(random.randint(1, 9999))
        self.conti  = str(conti)
        self.nome = str(nome)
        self.nomeci = str(nomeci)
        self.qtd = int(qtd)
        self.esq = None   
        self.dir = None   
        self.altura = 1
    def __repr__(self):
        return f"No({self.cod})"
#Classe para representar a árvore AVL e suas operações
class AVL:
    def __init__(self):
        self.raiz = None
    #Conjunto de métodos auxiliares
    def _altura(self, no):        
        if no is None:
            return 0
        return no.altura
    def _atualizar_altura(self, no):        
        no.altura = 1 + max(self._altura(no.esq), self._altura(no.dir))
    def _fator(self, no):
        if no is None:
            return 0
        return self._altura(no.esq) - self._altura(no.dir)
    #Método das rotações a direita
    def _rotacao_direita(self, z):
        y  = z.esq
        T3 = y.dir
        #Rotação
        y.dir = z
        z.esq = T3
        #Atualiza alturas (z primeiro, pois agora é filho de y)
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y   #Nova raiz da subárvore
    #Método das rotações a esquerda
    def _rotacao_esquerda(self, z):
        y  = z.dir
        T2 = y.esq
        #Rotação
        y.esq = z
        z.dir = T2
        #Atualização das alturas
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y   #Nova raiz da subárvore
    #Método de rebalanceamento das árvores
    def _rebalancear(self, no):
        self._atualizar_altura(no)
        fb = self._fator(no)
        #Caso 1: Esquerda-Esquerda
        if fb > 1 and self._fator(no.esq) >= 0:
            return self._rotacao_direita(no)
        #Caso 2: Esquerda-Direita
        if fb > 1 and self._fator(no.esq) < 0:
            no.esq = self._rotacao_esquerda(no.esq)
            return self._rotacao_direita(no)
        #Caso 3: Direita-Direita
        if fb < -1 and self._fator(no.dir) <= 0:
            return self._rotacao_esquerda(no)
        #Caso 4: Direita-Esquerda
        if fb < -1 and self._fator(no.dir) > 0:
            no.dir = self._rotacao_direita(no.dir)
            return self._rotacao_esquerda(no)
        return no   #Nó já balanceado


    #Método para inserir um elemento na árvore AVL (lembrem-se que não há valores repetidos)
    def inserir(self, novo):        
        self.raiz = self._inserir(self.raiz, novo)
        print(f'\nAnimal inserido com sucesso (Código do animal: {novo.cod})')
    #Método auxiliar recursivo para fazer a inserção de um elemento
    def _inserir(self, no, novo):
        if no is None:
            return novo
        if novo.cod < no.cod:
            no.esq = self._inserir(no.esq, novo.cod)
        elif novo.cod > no.cod:
            no.dir = self._inserir(no.dir, novo.cod)
        else:
            return no   # duplicado, ignora
        # rebalancer na volta da recursão
        return self._rebalancear(no)
    #Método para remover um elemento da árvore AVL
    def remover(self, cod):        
        self.raiz = self._remover(self.raiz, cod)
    def _remover(self, no, cod):
        if no is None:
            return None
        if cod < no.cod:
            no.esq = self._remover(no.esq, cod)
        elif cod > no.cod:
            no.dir = self._remover(no.dir, cod)
        else:
            if no.esq is None:
                return no.dir
            if no.dir is None:
                return no.esq
            #Se tiver dois filhos: substitui pelo sucessor in-order (menor da subárvore direita)
            sucessor = self._minimo(no.dir)
            no.cod = sucessor.cod
            no.dir   = self._remover(no.dir, sucessor.cod)
        #Rebalancear na volta da recursão
        return self._rebalancear(no)
    #Método para achar o menor valor da subárvore
    def _minimo(self, no):
        while no.esq is not None:
            no = no.esq
        return no


    #Método para buscar um valor/elemento
    def buscar(self, cod):        
        return self._buscar(self.raiz, cod)
    #Método recursivo para buscar um valor
    def _buscar(self, no, cod):
        if no is None:
            return False
        if cod == no.cod:
            return no
        if cod < no.cod:
            return self._buscar(no.esq, cod)
        return self._buscar(no.dir, cod)
    #Método de listagem em ordem
    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        print(resultado[::-1])
    #Método recursivo para listagem em ordem
    def _em_ordem(self, no, resultado):
        if no is None:
            return
        self._em_ordem(no.esq, resultado)
        resultado.append(no.cod)
        self._em_ordem(no.dir, resultado)
    #Métodos para calcular a altura da árvore e o fator de balanceamento
    def altura(self):        
        return self._altura(self.raiz)
    def fator_balanceamento(self, valor):        
        no = self._localizar(self.raiz, valor)
        if no is None:
            raise ValueError(f"Valor {valor} não encontrado na árvore.")
        return self._fator(no)
    def _localizar(self, no, valor):        
        if no is None:
            return None
        if valor == no.cod:
            return no
        if valor < no.cod:
            return self._localizar(no.esq, valor)
        return self._localizar(no.dir, valor)



#####Menu de opções
arv = AVL()
ind = int(0)
#Travando o menu até o usuário inserir o número 6
while(ind != 6):
    #Escolha da função
    while(ind != 1 and ind != 2 and ind != 3 and ind != 4 and ind != 5 and ind != 6):
        try:
            #Solicitando input
            ind = int(input('Qual operação você deseja realizar?\n1. Catalogar espécie\n2. Alerta de extinção\n3. Resgatar espécie mais rara\n4. Buscar por código de raridade\n5. Relatório de emergência\n6. Encerrar\nInsira apenas o número da operação desejada: '))
            if(ind > 6 or ind < 1): print('O número precisa ser entre 1 e 6...')
        except:
            print('Erro: O valor inserido precisa ser um número\n')
    #Execução da função escolhida
    match ind:
        #1. Catalogar espécie
        case 1:
            #Criar um nó, repassar esse nó na inserção
            conti = str(input('\nInsira o continente de origem do animal: '))
            nome = str(input('\nInsira o nome comum do animal: '))
            nomeci = str(input('\nInsira o nome científico do animal: '))
            try:
                qtd = float(input('\nInsira a quantidade de amostras do animal: '))
                #Adicionando os valores no novo nó
                novo = No(conti, nome, nomeci, qtd)
                #Inserindo o novo nó na lista
                arv.inserir(novo)
            except:
                print('\nO valor inserido para a quantidade de amostras precisa ser numeros inteiros (O animal não foi adicionado)\n')
            ind = int(0)
        #2. Alerta de extinção
        case 2:
            print('Faltou fazer')
            ind = int(0)
        #3. Resgatar espécie mais rara
        case 3:
            try:
                busc = int(input('\nInsira o código de um ativo para buscar: '))
                arm = arv.buscar(busc)
                if(arm == False):
                    print('O valor não foi encontrado')
                else:
                    arv.buscar(arm)
                    arv.remover(arm)
            except:
                print('\nO código inserido não era numérico')
        #4. Buscar por código
        case 4:
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
        #5. Relatório de emergência
        case 5:
            arv.em_ordem()
            ind = int(0)
        #6. Encerrar
        case 6:
            print('Encerrando...')