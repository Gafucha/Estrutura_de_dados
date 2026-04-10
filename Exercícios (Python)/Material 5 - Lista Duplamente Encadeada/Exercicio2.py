#Importando a classe "Lista" de outro arquivo
from lista_dupla import Lista

#Função para rotacionar pelos valores
def rotacionar(lista, k):
    inic = lista.inicio
    contador = int(0)
    #Contando todos os valores da lista
    while(inic is not None):
        contador+=1
        inic = inic.dir
    #Reiniciando o contador para uso futuro
    inic = lista.inicio
    #Verificando se o valor é desnecessáriamente maior
    if(k > contador):
        #Ajeitando o valor caso ele seja desnecessáriamente maior
        k = (k % contador)
    #Encontrando o novo inicio
    arm1 = lista.inicio
    for _ in range(k):
        arm1 = arm1.dir
    #Definindo os novos valores
    inic = arm1
    fina = arm1.esq
    #Fazendo a troca de valores
    inic.esq = None
    fina.dir = None
    lista.fim.dir = lista.inicio
    lista.inicio.esq = lista.fim
    lista.fim = fina
    lista.inicio = inic



#Código
arm1 = Lista()
arm1.inserir_final(1)
arm1.inserir_final(2)
arm1.inserir_final(3)
arm1.inserir_final(4)
arm1.inserir_final(5)
arm1.inserir_final(6)
rotacionar(arm1, 2)
arm1.printlist()