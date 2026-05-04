#Criando a classe de Nó
class No:
    #Definindo o construtor
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
#Criando a classe da Árvore binária de busca
class Abb:
    def __init__(self):
        self.raiz = None
    
    #Método para inserir um dado na árvore binária de busca
    def inserir(self, dado):
        self.raiz = self._inserir(self.raiz, dado)
    #Método recursivo para inserir um dado na árvore
    def _inserir(self, no, dado):
        #Verificando se o elemento atual está vazio
        if no is None: #Se estiver vazio, coloca o valor inserido no Nó
            return No(dado)
        #Verificando se o valor atual é menor que o valor do nó
        if dado < no.dado: #Se for menor que o nó, entra no elemento da esquerda e verifica se o nó é None (Recursivo)
            no.esq = self._inserir(no.esq, dado)
        elif dado > no.dado: #Se for maior que o nó, entra no elemento da direita e verifica se o nó é None (Recursivo)
            no.dir = self._inserir(no.dir, dado)
        #Passando por todos os loops ele vai retornar o nó para a variável pai
        return no

    #Método para fazer o percurso em ordem
    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado
    #Método auxiliar recursivo para fazer o percurso em ordem
    def _em_ordem(self, no, resultado):
        #Verificando se o nó atual está vazio
        if no is None: #Se estiver vazio, guarda o valor do nó atual
            return
        #No caso do nó atual não estar vazio, verificar pra que lado ir
        self._em_ordem(no.esq, resultado) #Se houver lado esquerdo, ele vai para o lado esquerdo
        resultado.append(no.dado) #Salvar o resultado do nó atual
        self._em_ordem(no.dir, resultado) #Se não houver lado esquerdo, ele vai pro lado direito
    #Método pra remover um elemento da lista
    def remover(self, dado):
        self.raiz = self._remover(self.raiz, dado)

    #Método auxiliar (recursivo) pra remoção de um elemento
    def _remover(self, no, dado):
        if no is None: #Se estiver vazio, retorna o espaço vazio
            return None
        #No caso do nó atual não estar vazio, verificar pra que lado ir
        if dado < no.dado: #Se o valor buscado for menor que o do elemento, ir para a esquerda
            no.esq = self._remover(no.esq, dado) #Ir para o elemento da esquerda
        elif dado > no.dado: #Se o valor buscado for maior que o do elemento, ir para a direita
            no.dir = self._remover(no.dir, dado) #Ir para o elemento da direita
        else:
            #caso 1 --> O nó não tem filhos
            if no.esq is None and no.dir is None:
                return None
            #caso 2 --> O nó tem 1 filho
            if no.esq is None:
                return no.dir
            if no.dir is None:
                return no.esq
            #caso 3 --> O nó possui 2 filhos
            sucessor = self.buscar_menor(no.dir)
            no.dado = sucessor.dado
            no.dir = self._remover(no.dir, sucessor.dado)
        return no

    #Método para buscar um elemento na lista
    def buscar_menor(self, no):
        aux = no
        while aux.esq is not None:
            aux = aux.esq
        return aux
                
#Teste código
if __name__ == '__main__':
    print('*' * 85)
    arv = Abb()
    arv.inserir(15)
    arv.inserir(7)
    arv.inserir(67)
    arv.inserir(69)
    arv.inserir(10)
    arv.inserir(25)
    print(arv.em_ordem())
    arv.remover(67)
    print(arv.em_ordem())