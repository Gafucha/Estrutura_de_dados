from lista_dupla import Lista

class Carro():
    def __init__(self, marca: str, modelo: str, valor: float):
        self.marca = marca
        self.modelo = modelo
        self.valor = float(valor)
    
    def __str__(self):
        return f"\nMarca = {self.marca}\nModelo = {self.modelo}\nValor = R$ {self.valor}\n"        
    
    #Listando todos os carros dentro da lista
    def listar_carros(self):
        arm1 = lista.inicio
        while(arm1 is not None):
            print(arm1.dado)
            arm1 = arm1.dir
    #Listando todos os carros que possuem o modelo pesquisado
    def buscar_modelo(self, val):
        arm1 = lista.inicio
        while(arm1 is not None):
            if(arm1.dado.modelo == val):
                print(arm1.dado)
            arm1 = arm1.dir
    #Descobrindo e imprimindo o carro mais caro
    def carro_mais_carro(self):
        arm1 = lista.inicio
        carrocaro = float(0)
        while(arm1 is not None):
            if(arm1.dado.valor > carrocaro):
                carrocaro = float(arm1.dado)
            arm1 = arm1.dir
        print(f'O carro mais caro é: {carrocaro}')
    #Calculando a média do valor dos carros
    def calc_media(self):
        arm1 = lista.inicio
        med = float(0)
        while(arm1 is not None):
            med += arm1.dado.valor
            arm1 = arm1.dir
        med = med / lista.tamanho
        print(f'A média do valor dos carros é: {med}')

    


#Código
lista = Lista()
lista.inserir_final(Carro('minecarroças', 'bigorner', 5000))
lista.inserir_final(Carro('minecarroças', 'the witherer', 3000))
lista.inserir_final(Carro('minecarroças', 'creeperer', 7000))
lista.printlist()
