import random
from collections import deque
class No:
    #Definindo o construtor
    def __init__(self, titulo, artista, dur, gen):
        #ID único
        self.id = int(random.randint(1, 9999))
        #Número de repetições da música
        self.rep = int(0)
        #Duração da música
        self.dur = int(dur)
        #Gênero musical
        self.gen = str(gen)
        self.titulo = str(titulo)
        self.artista = str(artista)
        self.esq = None
        self.dir = None
class Lista:
    #Definindo o construtor
    def __init__(self):
        self.raiz = None
    #Método para inserir
    def inserir(self, novo):
        #Verificando se o valor está na lista
        while(self.buscar(novo.id) != False):
            #Se o valor já estiver na lista, gera outro número, até a chave ser única
            novo.id = random.randint(1, 9999)
        #No caso do elemento não estar na lista, inserir ele
        #Verificando se a lista está vazia
        if(self.raiz is None):
            #Se estiver vazia adicionar o nó como raiz
            self.raiz = novo
        else: #No caso de não estar vazia, usar o inserir recursivo
            self._inserir(self.raiz, novo)
        print(f'\nA música foi adicionada com sucesso! (id da música: {novo.id})')
    #Método da inserção recursivo
    def _inserir(self, no_atual, novo):
        #Se o novo for menor que o nó atual, ir para a esquerda
        if(novo.id < no_atual.id):
            #Se a esquerda estiver vazia, inserir ali
            if(no_atual.esq is None):
                no_atual.esq = novo
            else: #Se a esquerda tiver valor, chamar a recursividade para esquerda
                self._inserir(no_atual.esq, novo)
        else: #No caso do novo ser maior que o valor atual, ir para a direita
            #Se a direita estiver vazia, inserir a ali mesmo
            if(no_atual.dir is None):
                no_atual.dir = novo
            else: #Se a direita tiver um valor, chamar a recursividade para direita
                self._inserir(no_atual.dir, novo)
    #Método para buscar dentro da lista e retornar o valor se encontrar ele
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)
    #Método recursivo de busca
    def _buscar(self, no_atual, valor):
        #Se o nó atual estiver vazio, retornar falso
        if(no_atual is None):
            return False
        #Se o nó atual for o que procuramos, retornar verdadeiro
        elif(no_atual.id == valor):
            return no_atual
        #No caso de não ser nenhum dos dois, continuar procurando pra esquerda
        elif(valor < no_atual.id):
            return self._buscar(no_atual.esq, valor)
        #No caso de não estar para a esquerda, procurar para a direita
        return self._buscar(no_atual.dir, valor)
    #Método para remover valores (Filtragem)
    def remover(self, valor):
        #Verificando se o valor procurado está na lista
        if(self.buscar(valor) == False):
            #Se não achar, printar erro
            print(f"O id {valor} não existe na árvore.")
            #Encerrar o código se não achar
            return
        #No caso de achar o valor na lista, passar a lista para o _remover()
        self.raiz = self._remover(self.raiz, valor)
        #Notificação pro usuário que foi removido
        print(f"A música de id {valor} removido com sucesso.")
    #Método para remover recursivo (Remoção)
    def _remover(self, no_atual, valor):
        #Verifica se acabaram os valores do ramo
        if(no_atual is None):
            return no_atual
        #Procura o valor pra esquerda
        if(valor < no_atual.id):
            no_atual.esq = self._remover(no_atual.esq, valor)
        #Procura o valor pra direita
        elif(valor > no_atual.id):
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
                no_atual.id = sucessor.id
                #Remove o sucessor da subárvore direita
                no_atual.dir = self._remover(no_atual.dir, sucessor.id)
        #Retorna o valor atual para terminar a troca de lugares
        return no_atual
    #Método para achar o menor valor
    def menor(self, no):
        #Indo pra esquerda até não poder mais
        while(no.esq is not None):
            no = no.esq
            #Retorna o nó de valor mais baixo
        return no
    #Método pra listar os valores da árvore (Só o top5)
    def listop5(self):
        #Criando uma lista dupla para armazenar o top5
        arm = deque([])
        #Verificando se a árvore está vazia
        if(self.raiz == None):
            #Informando que a árvore está vazia
            print('\nA árvore está vazia!')
        #Caso a árvore não esteja vazia
        else:
            #Chamando o método recursivo
            self._listop5(self.raiz, arm)
            #Percorrendo a lista do top5
            for i in range(0, len(arm)):
                #Imprimindo os dados da música atual
                print(f'\n~~~~~~~~~~{i+1}º Música:~~~~~~~~~~\nID da música: {arm[i].id}\nNome da música: {arm[i].titulo}\nArtista: {arm[i].artista}\nNúmero de repetições: {arm[i].rep}\nDuração da música: {arm[i].dur}\nGênero musical: {arm[i].gen}')
    #Método recursivo pra percorrer a árvore
    def _listop5(self, no_atual, arm):
        #Verificando se o nó atual existe
        if(no_atual != None):
            #Percorrendo o lado esquerdo da árvore
            self._listop5(no_atual.esq, arm)
            #Verificando se a lista está vazia
            if(len(arm) == 0):
                #Adicionando o primeiro elemento
                arm.append(no_atual)
            #A lista já possui valores
            else:
                #Variável para controlar se a música foi inserida
                inserido = False
                #Percorrendo a lista do top5
                for i in range(0, len(arm)):
                    #Verificando se a música atual possui mais repetições
                    if(no_atual.rep > arm[i].rep):
                        #Criando uma lista auxiliar
                        arm1 = deque([])
                        #Copiando os valores anteriores
                        for u in range(0, i):
                            #Adicionando o elemento atual na nova lista
                            arm1.append(arm[u])
                        #Adicionando a nova música
                        arm1.append(no_atual)
                        #Copiando os valores restantes
                        for u in range(i, len(arm)):
                            #Adicionando os valores restantes
                            arm1.append(arm[u])
                        #Limpando a arm
                        while(len(arm) > 0):
                            #Removendo as músicas da arm
                            arm.pop()
                        #Copiando as músicas da auxiliar para a arm
                        while(len(arm1) > 0):
                            #Adicionando as músicas na arm
                            arm.append(arm1.popleft())
                        #Essa música já foi inserida
                        inserido = True
                        break
                    #Verificando se as músicas possuem a mesma quantidade de repetições
                    elif(no_atual.rep == arm[i].rep):
                        #Verificando se o ID da música atual é menor
                        if(no_atual.id < arm[i].id):
                            #Criando uma lista auxiliar
                            arm1 = deque([])
                            #Copiando as músicas anteriores
                            for u in range(0, i):
                                #Adicionando o nó atual na arm1
                                arm1.append(arm[u])
                            #Adicionando a nova música
                            arm1.append(no_atual)
                            #Copiando as músicas restantes
                            for u in range(i, len(arm)):
                                #Adicionando as músicas restantes
                                arm1.append(arm[u])
                            #Limpando a lista original
                            while(len(arm) > 0):
                                #Removendo as músicas da arm
                                arm.pop()
                            #Copiando as músicas da arm1 para a arm
                            while(len(arm1) > 0):
                                #Adicionando músicas na lista original
                                arm.append(arm1.popleft())
                            #Essa música já foi inserida
                            inserido = True
                            break
                #Verificando se a música não foi inserida
                if(inserido == False):
                    #Adicionando a música ao final da lista
                    arm.append(no_atual)
            #Verificando se a lista possui mais que 5 elementos
            if(len(arm) > 5):
                #Removendo o último elemento da lista
                arm.pop()
            #Percorrendo o lado direito da árvore
            self._listop5(no_atual.dir, arm)
        #Caso o nó recebido seja vazio
        else:
            #Retornando para a chamada anterior
            return
    #Método pra listar os elementos da árvore em ordem considerando gênero musical
    def listargen(self):
        #Se a árvore estiver vazia, não listar
        if(self.raiz == None):
            print('\nA árvore está vazia!')
        #Tem elementos na árvore
        else:
            arm = []
            self._listargen(self.raiz, arm, input('Qual gênero musical você deseja buscar?'))
            #Retornando a lista
            for i in range(0, len(arm)):
                print(f'\n~~~~~~~~~~{i+1}º Música:~~~~~~~~~~\nID da música: {arm[i].id}\nNome da música: {arm[i].titulo}\nArtista: {arm[i].artista}\nNúmero de repetições: {arm[i].rep}\nDuração da música: {arm[i].dur}\nGênero musical: {arm[i].gen}')
    #Método recursivo pra percorrer a lista
    def _listargen(self, no_atual, arm, gen):
        #Verificando se o nó atual tem valor
        if(no_atual is not None): #Se tiver valor, percorrer
            #Percorrer o lado esquerdo
            self._listargen(no_atual.esq, arm, gen)
            #Guardando o valor atual
            if(no_atual.gen == gen):
                arm.append(no_atual)
            #Percorrer o lado direito
            self._listargen(no_atual.dir, arm, gen)
        else:
            return
#####Menu de opções
ind = int(0)
arv = Lista()
#Travando o menu até o usuário inserir o número 7
while(ind != 7):
    #Escolha da função
    while(ind != 1 and ind != 2 and ind != 3 and ind != 4 and ind != 5 and ind != 6 and ind != 7):
        #Verificação de erros
        try:
            #Solicitando input
            ind = int(input('\nQual operação você deseja realizar?\n1. Cadastrar música\n2. Buscar música por ID\n3. Ouvir música por ID\n4. Remover música por ID\n5. Top-5 músicas\n6. Relatório de músicas por gênero\n7. Encerrar o código\nInsira apenas o número da operação desejada: '))
            if(ind > 7 or ind < 1): print('O número precisa ser entre 1 e 7...')
        except:
            print('\nO valor inserido precisa ser um número\n')
    #Execução da função escolhida
    match ind:
        #1. Cadastro da música
        case 1:
            #Criar um nó, repassar esse nó na inserção
            titulo = str(input('\nInsira o título da música: '))
            artista = str(input('\nInsira o artista da música: '))
            genero = str(input('\nInsira o gênero da música: '))
            try: #No caso de todos os valores estarem certo, executar o código principal
                durac = int(input('\nInsira a duração da música (em segundos): '))
                #Adicionando os valores no novo nó
                novo = No(titulo, artista, durac, genero)
                #Inserindo o novo nó na lista
                arv.inserir(novo)
            except: #No caso de ter um valor errado (durac), avisar e não adicionar o elemento
                print('\nO valor da duração deve ser somente números inteiros, por isso a música não foi inserida\n')
            #Reiniciando o menu
            ind = int(0)
        #2. Buscar música por ID
        case 2:
            #Verificando que o usuário vai inserir um número
            try:
                busc = int(input('Insira o id de uma música para buscarmos: '))
                no = arv.buscar(busc)
                if(no == False):
                    print('\nA música inserida não foi encontrada\n')
                else:
                    print(f'\nA música de id {no.id} se chama "{no.titulo}", do artista {no.artista}, a música dura {no.dur} segundos, ela foi reproduzida {no.rep} vezes e ela é do gênero musical "{no.gen}"\n')
            except:
                print('O id da música precisa ser um id numérico (Só números inteiros)\n')
            #Reiniciando o menu
            ind = int(0)
        #3. Ouvir música
        case 3:
            #Verificando que o usuário vai inserir um número
            try:
                busc = int(input('Insira o id da música que você deseja ouvir: '))
                no = arv.buscar(busc)
                #Verificando se ele encontrou a música
                if(no == False): #Não encontrou
                    print('\nA música inserida não foi encontrada\n')
                #No caso de encontrar, adicionar repetição
                else:
                    no.rep += 1
                    print(f'\nA música "{no.titulo}" foi ouvida com sucesso!\n')
            except:
                print('\nO id da música precisa ser somente números inteiros')
            #Reiniciando o menu
            ind = int(0)
        #4. Remover música
        case 4:
            #Verificando que o usuário vai inserir um número
            try:
                rem = int(input('Insira o id da música a ser removida: '))
                no = arv.remover(rem)
            except:
                print('O id inserido precisa ser composto por números inteiros')
            #Reiniciando o menu
            ind = int(0)
        #5. Relatório das top5
        case 5:
            arv.listop5()
            #Reiniciando o menu
            ind = int(0)
        #6. Relatório por gênero musical
        case 6:
            arv.listargen()
            #Reiniciando o menu
            ind = int(0)
        #7. Encerrar
        case 7:
            print('Encerrando...')