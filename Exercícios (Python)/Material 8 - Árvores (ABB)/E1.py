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
        dado = dado.lower()
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

    #Método para buscar os nomes que começam pelo prefixo
    def buscar(self, pref):
        pref = pref.lower()
        resultado = []
        self._buscar(self.raiz, pref, resultado)
        return resultado
    #Método recursivo para a busca pelo prefixo
    def _buscar(self, no, pref, resultado):
        #Verificando se o nó está vazio
        if no is None:
            return
        #Verificando se o prefixo é menor que o nó
        if pref < no.dado: #No caso de ser menor, ele vai pra esquerda
            self._buscar(no.esq, pref, resultado)
        
        #Verificando se o dado atual começa com o prefixo
        if no.dado.startswith(pref):
            resultado.append(no.dado)
        
        #Verificando se o prefixo é maior que o nó
        if pref + chr(127) > no.dado: #No caso de ser maior, ele vai pra direita
            self._buscar(no.dir, pref, resultado)
        



#Teste código
if __name__ == '__main__':
    arv = Abb()
    usuarios = ["mariana", "marcos", "mario", "ana", "marina", "bruna", "marcelo"]
    #Adicionando nomes aleatórios
    arv.inserir('bangbangkok')
    arv.inserir('bingbingkok')
    arv.inserir('dongdongkok')
    arv.inserir('mongmongkok')
    arv.inserir('mamangoistoblowup')
    #adicionando os nomes na lista pra arvore
    for i in usuarios:
        arv.inserir(i)
    #Imprimindo a lista
    print(arv.buscar(''))