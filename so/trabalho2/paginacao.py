import sys

def fifo(pList):
    miss = 0
    hits = 0
    memFrames = pList[0]
    pListActual = []
    index = 0

    # Aqui testa-se 3 casos:
    #     i. Se o elemento já está em pListActual
    #     ii. Se pListActual ainda esta sendo populada
    #     iii. Se o elemento não está em pListActual
    for i in range(1, len(pList)):
        
        # Caso o elemento esteja em pListActual, acumula-se
        # um hit e se avança pro próximo ciclo do loop.
        # Faz-se assim pra se evitar que o index atualize ao
        # final.
        if (pList[i] in pListActual):
            hits += 1
            continue

        # Este teste é um capricho da linguagem. Como eu não
        # posso popular inicialmente pListActual com um
        # numero memFrames de 0s, só me resta criar a lista
        # vazia. Em python, listas vazias não aceitam declaração
        # direto pra um indice, obrigando o programador usar
        # o .append(). Então eu populo a lista e acumulo +1 miss
        elif (i <= memFrames):
            pListActual.append(pList[i])
            miss += 1

        # No caso do elemento de pList não existir em pListActual e
        # pListActual já estar completamente populada, obviamente 
        # trata-se de um miss. Neste caso, eu faço a atribuição
        # diretamente ao indice e acumulo +1 miss.
        else:
            pListActual[index] = pList[i]
            miss += 1

        # O controle de atribuição aos indices de pListActual é
        # feito atraves da variavel index. Esta variavel é atualizada
        # de 1 em 1 até atingir um valor maior que memFrames. Quando
        # isto acontece, ela é zerada e o processo recomeça.
        index += 1
        if (index > memFrames - 1):
            index = 0
    
    print("FIFO", miss)

def otm(pList):
    miss = 0
    hits = 0
    memFrames = pList[0]
    pListActual = []
    index = 0
    priority = 0
    priority1 = [0] * memFrames
    priority2 = [0] * memFrames

    for i in range(1, len(pList)):
        if (pList[i] in pListActual):
            hits += 1
            priority2 = [x - 1 for x in priority2]
            priority2[pListActual.index(pList[i])] = len(pListActual)
            continue

        elif (i <= memFrames):
            pListActual.append(pList[i])
            miss += 1
            priority2[index] = index + 1
            index += 1

        else:
            for j in range(len(pListActual)):
                for k in range(i + 1, len(pList)):
                    if (pListActual[j] == pList[k]):
                        priority1[j] = priority
                        priority -= 1

            if (0 in priority1):
                auxIndex = [x for x, y in enumerate(priority1) if y == 0]
                auxMin = [priority2[x] for x in auxIndex]

                pListActual[priority2.index(min(auxMin))] = pList[i]

                priority2 = [x - 1 for x in priority2]
                priority2[pListActual.index(pList[i])] = len(pListActual)

            else:
                pListActual[priority1.index(min(priority1))] = pList[i]
                priority2 = [x - 1 for x in priority2]
                priority2[pListActual.index(pList[i])] = len(pListActual)

            miss += 1

        priority = 4
        priority1 = [0 for x in priority1]

    print("OTM", miss)

def lru(pList):
    miss = 0
    hits = 0
    memFrames = pList[0]
    pListActual = []
    index = 0
    priority = 0
    priority2 = [0] * memFrames

    for i in range(1, len(pList)):
        if (pList[i] in pListActual):
            hits += 1
            priority2 = [x - 1 for x in priority2]
            priority2[pListActual.index(pList[i])] = len(pListActual)
            continue

        elif (i <= memFrames):
            pListActual.append(pList[i])
            miss += 1
            priority2[index] = index + 1
            index += 1

        else:
            pListActual[priority2.index(min(priority2))] = pList[i]
            priority2 = [x - 1 for x in priority2]
            priority2[pListActual.index(pList[i])] = len(pListActual)

            miss += 1

    print("LRU", miss)
    pass

def buildPageList(file):
    # Le o arquivo file e popula o vetor raw com os elementos
    # de cada linha de file, excluindo os \n
    raw = file.read().splitlines()

    # Popula um vetor pList (PageList) com os casts pra int de
    # todos os elementos de raw[]
    pList = [int(x) for x in raw]
    return pList

def run():
    try:
        file = open(sys.argv[1], 'r')

        pList = buildPageList(file)

        fifo(pList)
        otm(pList)
        lru(pList)

    except Exception as e:
        print("Erro!")
        print(str(e))

if __name__ == "__main__":
    run()