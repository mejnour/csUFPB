import sys, os
from time import process_time

def countingSort(uList):
    maximum = max(uList)
    minimum = min(uList)

    oList = []

    # Separação e definição entre CountingNegatives e
    # CountingPositives. Pra resolver o problema
    # dos índices num único array
    if (minimum < 0):
        countingN = [0] * (abs(minimum) + 1)
        countingP = [0] * (maximum + 1)
    else:
        countingP = [0] * (maximum + 1)

    # Conta a quantidade de elementos presentes em uList.
    # Negativos vão em countingN e positivos em countingP.
    # O zero vai em countingP.
    for i in range(len(uList)):
        if (uList[i] < 0):
            countingN[abs(uList[i])] += 1
        else:
            countingP[uList[i]] += 1

    # Soma acumulada de countingN e countingP.
    for j in range(1, len(countingN)):
        countingN[j] = countingN[j] + countingN[j - 1]
    for j in range(1, len(countingP)):
        countingP[j] = countingP[j] + countingP[j - 1]

    # Shifting da soma acumulada.
    for k in range(len(countingN) - 1, -1, -1):
        countingN[k] = countingN[k - 1]
    for k in range(len(countingP) - 1, -1, -1):
        countingP[k] = countingP[k - 1]
        if k == 0:
            countingP[k] = 0

    # Descrição das ordenações feitas a seguir:
    #
    # # Ordenação da lista auxiliar auxOrdN,
    # # que recebe todos os negativos em decrescente e
    # # depois os inverte para a ordem certa
    #
    # # Ordenação da lista auxiliar auxOrdP,
    # # que recebe todos os elementos pertencentes a N*
    # 
    # # Caso existam zeros, eles serão adicionados a
    # # lista auxiliar auxOrdZ.
    auxOrdN = [0] * (len(uList))
    auxOrdP = [0] * (len(uList))
    auxOrdZ = []

    for l in range(len(uList)):
        if (uList[l] < 0):
            auxOrdN[countingN[abs(uList[l])]] = uList[l]
            countingN[abs(uList[l])] += 1
        elif (uList[l] > 0):
            auxOrdP[countingP[uList[l]]] = uList[l]
            countingP[uList[l]] += 1
        else:
            auxOrdZ.append(0)

    auxOrdP = [x for x in auxOrdP if x != 0]
    auxOrdN = [x for x in auxOrdN if x != 0]
    auxOrdN.reverse()

    # Lista final ordenada, oList, recebendo as
    # contribuições negativas, positicas e de zeros abaixo.
    oList = auxOrdN + auxOrdZ + auxOrdP
    
    # print(oList)
    # print(len(uList))
    # print(len(oList))

def run():
    try:
        file = open(sys.argv[1], 'r')

        uList = file.read().splitlines()
        uList = [int(x) for x in uList]

        countingSort(uList)

        t1_stop = process_time()
        print("Elapsed: {0:.2f}".format(t1_stop - t1_start))

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(str(e))

if __name__ == "__main__":
    t1_start = process_time()
    run()