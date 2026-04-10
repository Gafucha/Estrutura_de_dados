
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaSimples:
    def __init__(self):
        self.inicio = None

    def inserir_fim(self, dado):
        None
    
    def inserir_inicio(self, dado):
        novo = No(dado)
        if self.inicio is None:
            self.inicio = novo
        else:
            novo.proximo = self.inicio
            self.inicio = novo

    def printlist(self):
        aux = self.inicio
        while aux:
            print(aux.dado, end='-> ')
            aux = aux.proximo

#Código Main
lista = ListaSimples()
lista.inserir_inicio(20)
lista.inserir_inicio(25)
lista.inserir_inicio(35)
lista.printlist()