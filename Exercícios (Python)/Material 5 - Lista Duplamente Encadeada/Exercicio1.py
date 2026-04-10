#Importando a lista do outro arquivo
from lista_dupla import Lista

#Criando a primeira lista
listaComum = Lista()
#Criando a segunda lista
listaPremium = Lista()
#Criando a lista intercalada
listaInter = Lista()

#Função para percorrer os valores das listas e intercalar
def perco(val1, val2):
    elem = int(0)
    p1 = val1.inicio
    p2 = val2.inicio
    #Percorrendo cada elemento
    while p1 is not None and p2 is not None:
        #Inserindo os valores atuais na nova lista
        listaInter.inserir_final(p1.dado)
        listaInter.inserir_final(p2.dado)
        #Atribuindo o próximo valor a variável
        p1 = p1.dir
        p2 = p2.dir
    #Caso ainda existam elementos sobrando na lista1
    while val1 is not None:
        listaInter.inserir_final(p1.dado)
        p1 = p1.dir
    #Caso ainda existam elementos sobrando na lista2
    while val2 is not None:
        listaInter.inserir_final(p2.dado)
        p2 = p2.dir
        

#Preenchendo a primeira lista
listaComum.inserir_final(1)
listaComum.inserir_final(3)
listaComum.inserir_final(5)
listaComum.inserir_final(7)
listaComum.inserir_final(9)
listaPremium.inserir_final(2)
listaPremium.inserir_final(4)
listaPremium.inserir_final(6)
listaPremium.inserir_final(8)
listaPremium.inserir_final(10)
perco(listaComum, listaPremium)
listaInter.printlist()