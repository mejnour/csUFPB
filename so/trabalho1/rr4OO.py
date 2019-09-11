def waitingTime(nProcess, wTimeL):
    accu = 0
    for i in wTimeL:
        accu += i
    
    avgWT = accu / nProcess
    return avgWT

def turnAroungTime(nProcess, wTimeL, processList):
    accu = 0
    for i in range(len(wTimeL)):
        accu += wTimeL[i] + processList[i].peak
    
    avgTAT = accu / nProcess
    return avgTAT

def responseTime(nProcess, reTimeL):
    accu = 0
    for i in reTimeL:
        accu += i

    avgRT = accu / nProcess
    return avgRT

def organizer(nProcess, processList):
    finished = False
    time = 0
    quantum = 4
    accu = 0
    index = 0
    wTimeL = [0] * nProcess
    reTimeL = [0] * nProcess
    auxOrder = []

    while finished != True:
        for i in processList:
            if (i.rPeak >= quantum) and (time >= i.arrival):
                if (i not in auxOrder):
                    auxOrder.append(i)
                    reTimeL[index] = time - i.arrival

                time += quantum

                if (i.rPeak == quantum):
                    wTimeL[index] = time - i.peak + (reTimeL[index])
                    accu += 1

                i.rPeak -= quantum

            elif (0 < i.rPeak < quantum) and (time >= i.arrival):
                if (i not in auxOrder):
                    auxOrder.append(i)
                    reTimeL[index] = time

                time += i.rPeak
                i.rPeak = 0

                wTimeL[index] = time - i.peak + (reTimeL[index])

                accu += 1

            index += 1

        index = 0
        if accu == nProcess:
            finished = True

    
    return reTimeL, wTimeL

def run(processList):
    nProcess = len(processList)
    
    reTimeL, wTimeL = organizer(nProcess, processList)

    avgWT = waitingTime(nProcess, wTimeL)
    avgTAT = turnAroungTime(nProcess, wTimeL, processList)
    avgRT = responseTime(nProcess, reTimeL)

    print("RR", avgTAT, avgRT, avgWT, end = "\n")