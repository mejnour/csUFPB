import sys
import fcfsOO
import sjfOO
import rr4OO
from processOO import Process

def buildProcess(arquivo):
    raw = arquivo.read().splitlines()
    
    arrivalTime = [x.split(" ")[0] for x in raw]
    peakTime = [x.split(" ")[1] for x in raw]

    processList = [Process(x + 1, int(arrivalTime[x]), int(peakTime[x])) \
        for x in range(len(arrivalTime))]

    return processList
    

def run():
    try:
        name = sys.argv[1]
        arq = open(name, 'r')

        pList = buildProcess(arq)

        fcfsOO.run(pList)
        sjfOO.run(pList)
        rr4OO.run(pList)

    except Exception as e:
        print("Deu mopa nessa porra")
        print(str(e))

if __name__ == "__main__":
    run()