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

    avgWT = accu / len(processList)

    return avgWT

def turnAroundTime(nProcess, processList):
    accu = 0
    for i in range(nProcess):
        processList[i].taTime = processList[i].wTime + processList[i].peak
        accu += processList[i].taTime

    avgTAT = accu / len(processList)

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
    
    avgRT = accu / len(processList)

    return avgRT

def run(processList):
    nProcess = len(processList)
    avgWT = waitingTime(nProcess, processList)
    avgTAT = turnAroundTime(nProcess, processList)
    avgRT = responseTime(nProcess, processList)

    print("FCFS", avgTAT, avgRT, avgWT, end = "\n")