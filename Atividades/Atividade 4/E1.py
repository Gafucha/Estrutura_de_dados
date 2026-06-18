import heapq

#Criando o Nó
class No:
    def __init__(self, peso, car=None, esquerda=None, direita=None):
        self.peso = peso
        self.car = car
        self.esquerda = esquerda
        self.direita = direita

#Criando o Indexador
class Indexer:
    def __init__(self):
        self.ind = 0
    def compressor(self, texto):
        cod = gera_cod(texto)
        freq = Frequencias(texto)
        print("\n=== TABELA CARACTERE -> CÓDIGO ===")
        for c in sorted(freq.keys()):
            exibicao = repr(c)[1:-1]
            print(f"Caractere: {exibicao:<10} \nFreq.: {freq[c]:<5}\nCódigo: {cod[c]}")
        #Armazenando os valores originais comprimidos e a taxa
        originais, comprimidos, taxa = estatisticas(texto)
        #Imprimindo tudo
        print("\\n=== ESTATÍSTICAS ===")
        print(f"Bits originais   : {originais}")
        print(f"Bits comprimidos : {comprimidos}")
        print(f"Taxa de compressão: {taxa:.1f}%")
    #Função pra iniciar
    def iniciar(self):
        self.ind = 0
        #Verificando se o usuário inseriu um valor válido
        while self.ind != 2:
            try:
                while self.ind != 1 and self.ind != 2:
                    self.ind = int(input("Qual operação você gostaria de realizar?\n1. Comprimir texto\n2. Encerrar\nInsira apenas o número da operação: "))
                #Verificando que opção o usuário escolheu
                match self.ind:
                    #1. Comprimir o texto
                    case 1:
                        texto = input("Insira um texto para a compressão e transmissão: ")
                        self.compressor(texto)
                        self.ind = 0
                    #2. Encerrar
                    case 2:
                        print("\nEncerrando...")
            except:
                print("\nDigite apenas números válidos!\n")
                self.ind = 0

#Função pra contar quantas vezes o caractere aparece no texto
def Frequencias(texto: str) -> dict[str, int]: #Transformando a respsota de str pra dicionário
    freq = {}
    for c in texto:
        freq[c] = freq.get(c, 0) + 1
    return freq

#Função pra transformar o texto na árvore de Huffman
def Arvorificador(texto: str):
    #Se não colocar texto nenhum
    if texto == None:
        return None
    #Calculando a frequência com que cada letra aparece
    freq = Frequencias(texto)
    #Guardando a ordem em que cada uma aparece pela primeira vez
    ord = []
    ja = set()
    #Verificando se os elementos já estão dentro da ordem
    for c in texto:
        #Se ainda não estiver, adicionar na lista da ordem
        if c not in ja:
            ja.add(c)
            ord.append(c)
    #Montando a árvore (min-heap)
    armheap = []
    contador = 0
    #Colocando os elementos na árvore
    for c in ord:
        no = No(freq[c], car=c)
        heapq.heappush(armheap, (freq[c], contador, no))
        contador += 1
    #Se o texto só tiver um caractere
    if len(armheap) == 1:
        return armheap[0][2]
    #Verificando se tem mais de um nó e montando a árvore
    while len(armheap) > 1:
        #Removendo o filho da esquerda
        peso1, ord1, no1 = heapq.heappop(armheap)
        #Removendo o filho da direita
        peso2, ord2, no2 = heapq.heappop(armheap)
        #Adicionando o elemento na árvore
        novo = No(peso1 + peso2, esquerda=no1, direita=no2)
        heapq.heappush(armheap, (novo.peso, contador, novo))
        contador += 1
    return armheap[0][2]

#Função pra gerar o código de cada caractere
def gera_cod(texto: str) -> dict[str, str]:
    #Montando a árvore
    raiz = Arvorificador(texto)
    #Se a raiz for zero retorna vazio
    if raiz is None:
        return {}
    #Montando os códigos
    cod = {}
    #Verificando se o caractere da raiz é vazio
    if raiz.car is not None:
        cod[raiz.car] = "0"
        return cod

    #Função pra percorrer e gerar os códigos
    def percorrer(no, codigo):
        if no.car is not None:
            cod[no.car] = codigo
            return
        #Percorrendo pros lados da árvore
        percorrer(no.esquerda, codigo + "0")
        percorrer(no.direita, codigo + "1")
    #Chamando a função criada
    percorrer(raiz, "")
    return cod

#Função pra calcular os bits comprimidos
def bits_comprimidos(texto: str) -> int:
    #Se o texto for vazio retornar 0
    if not texto:
        return 0
    #Calculando a frequência de cada caractere
    freq = Frequencias(texto)
    cod = gera_cod(texto)
    total = 0
    for car, quantidade in freq.items():
        total += quantidade * len(cod[car])
    return total

#Função pra calcular os valores extras
def estatisticas(texto: str) -> tuple[int, int, float]:
    bits_orig = len(texto) * 8
    bits_comp = bits_comprimidos(texto)
    #Se os bits forem 0 a taxa é 0
    if bits_orig == 0:
        taxa = 0.0
    else: #Se tiver valor, fazer o cálculo
        taxa = ((bits_orig - bits_comp) / bits_orig) * 100
    return bits_orig, bits_comp, taxa



###Testando código
if __name__ == "__main__":
    index = Indexer()
    index.iniciar()