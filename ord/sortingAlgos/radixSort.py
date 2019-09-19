import sys
from time import process_time

def sorting(uList, ref):

    # auxOrdP, auxOrdN e auxOrdZ, respectivamente,
    # auxiliam na ordenação das keys (refs) para 
    # elementos de uList positivos, negativos e zeros.
    auxOrdP = []
    auxOrdN = []
    auxOrdZ = []
    oList = []

    # Tentando inserir nas listas auxiliares, através 
    # de um slicing, o componente [i, -ref] de cada elemento. 
    # Quando não é possível, coloca 0 no lugar.
    for i in range(len(uList)):
        if uList[i] > 0:
            try:
                auxOrdP.append([i, int(str(uList[i])[-(ref)])])
            except:
                auxOrdP.append([i, 0])
        
        elif uList[i] < 0:
            try:
                auxOrdN.append([i, int(str(uList[i])[-(ref)])])
            except:
                auxOrdN.append([i, 0])

        else:
            auxOrdZ.append([i, 0])

    # A ordenação é feita usando a função sorted()
    # do python, garantidamente stable.
    #
    # Como o código acima desconsidera número negativos
    # (dê um print nessa lista auxOrdN pra entender),
    # resolveu-se usando essa trambicagem abaixo, 
    # que ordena os elementos negativos como se fossem 
    # positivos, e, quando ref é garantidamente o último, 
    # sabemos que não há mais o que ordenar, assim segue 
    # que a lista é invertida.
    auxOrdP = sorted(auxOrdP, key = lambda reff: reff[1])
    auxOrdN = sorted(auxOrdN, key = lambda reff: reff[1])
    if (ref == len(str(max(uList)))):
        auxOrdN.reverse()

    # A lista oList é então construída, adicionando os 
    # elementos negativos, os zeros e os positivos, 
    # nesta ordem.
    for j in range(len(auxOrdN)):
        oList.append(uList[auxOrdN[j][0]])  
    for j in range(len(auxOrdZ)):
        oList.append(uList[auxOrdZ[j][0]])
    for j in range(len(auxOrdP)):
        oList.append(uList[auxOrdP[j][0]])

    uList = oList
    return uList

# Define que algarismo vai ser a key da ordenação
# e repete até que o ultimo algarismo do maior
# numero seja "contemplado"
def radixSort(uList):
    # Garante que maximum seja o maior numero,
    # independente se positivo ou negativo.
    if (abs(min(uList)) > max(uList)):
        maximum = min(uList)
    else:
        maximum = max(uList)
    alga = 1

    while (len(str(maximum)) >= alga):
        uList = sorting(uList, alga)
        alga += 1
        
def run():
    try:
        file = open(sys.argv[1], 'r')
        uList = file.read().splitlines()
        uList = [int(x) for x in uList]

        radixSort(uList)
        t1_stop = process_time()
        print('Elapsed: {0:.2f}'.format(t1_stop - t1_start))
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    t1_start = process_time()
    run()