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
    quantum = 2
    accu = 0
    index = 0
    wTimeL = [0] * nProcess
    resTimeL = [0] * nProcess
    ready = []

    # lista auxiliar guarda quais processos tiveram
    # os tempos de resposta já calculados
    aux = []
    while finished != True:
        skip = False
        # Inicialmente, se o tamanho de ready for 0,
        # preenche com o que tiver pronto
        if (len(ready) == 0):
            for i in processList:
                if (time >= i.arrival) and (i not in ready):
                    ready.append(i)

        # Aqui começa o merengue
        if (ready[0].rPeak >= quantum):

            index = processList.index(ready[0])
            # Caso o processo não esteja em aux, ele entra e
            # em seguida é guardado o tempo de resposta dele.
            if (processList[index] not in aux):
                aux.append(processList[index])
                resTimeL[index] = time - processList[index].arrival
                      
            # Se o pico restante for exatamente igual ao
            # quantum, então sabemos que este processo vai
            # terminar. Sendo assim, aproveitamos pra
            # calcular o tempo de espera dele.
            if (processList[index].rPeak == quantum):
                processList[index].rPeak -= quantum
                time += quantum
                wTimeL[index] = time - processList[index].peak - \
                    processList[index].arrival
                skip = True

            if (skip != True):
                processList[index].rPeak -= quantum
                time += quantum

            # Checa se existem outros processos, neste novo
            # tempo, disponíveis para entrar na fila de prontos.
            for j in processList:
                if (time >= j.arrival) and (j not in ready) and (j.rPeak > 0):
                    ready.append(j)
            
            # Exclui o processo da lista de prontos e,
            # caso o tempo de pico dele não tenha chegado a 0,
            # reintroduz o mesmo processo ao final da fila.
            ready.pop(0)
            if (processList[index].rPeak > 0):
                ready.append(processList[index])
        
        elif (0 < ready[0].rPeak < quantum):

            index = processList.index(ready[0])
            if (processList[index] not in aux):
                aux.append(processList[index])
                resTimeL[index] = time - processList[index].arrival

            processList[index].rPeak -= ready[0].rPeak
            time += ready[0].rPeak
            wTimeL[index] = time - processList[index].peak - \
                processList[index].arrival
            
            # Checa se existem outros processos, neste novo
            # tempo, disponíveis para entrar na fila de prontos.
            for j in processList:
                if (time >= j.arrival) and (j not in ready) and (j.rPeak > 0):
                    ready.append(j)
            
            # Exclui o processo da lista de prontos.
            ready.pop(0)

        if len(ready) == 0:
            finished = True

    return resTimeL, wTimeL

def run(processList):
    nProcess = len(processList)
    
    reTimeL, wTimeL = organizer(nProcess, processList)

    avgWT = waitingTime(nProcess, wTimeL)
    avgTAT = turnAroungTime(nProcess, wTimeL, processList)
    avgRT = responseTime(nProcess, reTimeL)

    print("RR", avgTAT, avgRT, avgWT, end = "\n")