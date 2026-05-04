lista = [7, 3, 4, 2, 3, 5, 2]

def pesquisar() -> int:
    achou = -1
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                #achou = lista[i]
                #break
                return lista[i]
    return achou

print(pesquisar())