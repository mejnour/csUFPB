def waitingTime(nProcess, processList):
    accu = 0
    for i in range(nProcess):
        if i == 0:
            processList[i].wTime = i + processList[i].arrival
            accu += processList[i].wTime
        else:
            processList[i].wTime = processList[i - 1].peak + processList[i - 1].wTime - \
                (processList[i].arrival - processList[i - 1].arrival)
            accu += processList[i].wTime

    avgWT = accu / nProcess

    return avgWT

def turnAroungTime(nProcess, processList):
    accu = 0
    for i in range(nProcess):
        processList[i].taTime = processList[i].wTime + processList[i].peak
        accu += processList[i].taTime

    avgTAT = accu / nProcess

    return avgTAT

def responseTime(nProcess, processList):
    accuPeak = [0] * nProcess
    accu = 0
    for i in range(nProcess):
        if i == 0:
            processList[i].rTime = 0
            accuPeak[i] = processList[i].peak
            accu += processList[i].rTime
        else:
            processList[i].rTime = accuPeak[i - 1] - processList[i].arrival
            accuPeak[i] = accuPeak[i - 1] + processList[i].peak
            accu += processList[i].rTime
    
    avgRT = accu / nProcess

    return avgRT

def organizer(nProcess, processList):
    finished = False
    time = 0
    order = [processList[x] for x in range(len(processList))]
    trueOrder = []

    order = sorted(order, key = lambda process: process.peak)

    while finished != True:
        for i in order:
            if (time >= i.arrival) and (i not in trueOrder):
                trueOrder.append(i)
                time += i.peak
                break

        if len(trueOrder) == nProcess:
            finished = True
        
    return trueOrder

def run(processList):
    nProcess = len(processList)

    newOrdList = organizer(nProcess, processList)

    avgWT = waitingTime(nProcess, newOrdList)
    avgTAT = turnAroungTime(nProcess, newOrdList)
    avgRT = responseTime(nProcess, newOrdList)

    print("SJF", avgTAT, avgRT, avgWT, end = "\n")