import sys
from time import process_time

def sorting(uList, ref):
    
    # print(".")

    auxOrdP = []
    auxOrdN = []
    auxOrdZ = []
    oList = []

    # print(".")

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

    # print(".")


    # print(auxOrdN)
    auxOrdP = sorted(auxOrdP, key = lambda reff: reff[1])
    # print(auxOrdN)
    auxOrdN = sorted(auxOrdN, key = lambda reff: reff[1])
    if (ref == len(str(max(uList)))):
        auxOrdN.reverse()
    # print(auxOrdN)

    # print(".")

    for j in range(len(auxOrdN)):
        oList.append(uList[auxOrdN[j][0]])
    
    for j in range(len(auxOrdZ)):
        oList.append(uList[auxOrdZ[j][0]])
    
    for j in range(len(auxOrdP)):
        oList.append(uList[auxOrdP[j][0]])

    # print(uList)
    uList = oList
    # print(uList)
    # print(oList)
    # print("- - - - - - - - - - - -")
    return uList

def radixSort(uList):
    maximum = max(uList)
    exp = 1

    while (len(str(maximum)) >= exp):
        uList = sorting(uList, exp)
        exp += 1
        
def run():
    # pass
    try:
        file = open(sys.argv[1], 'r')
        uList = file.read().splitlines()
        uList = [int(x) for x in uList]

        # print(".")

        radixSort(uList)
        t1_stop = process_time()
        print('Elapsed: {0:.2f}'.format(t1_stop - t1_start))
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    t1_start = process_time()
    run()
    # uList = [50, 400, 321, 2, 1, 0, -2, -2, -5]
    # # uList = [53, 89, 150, 36, 633, 233]
    # radixSort(uList)