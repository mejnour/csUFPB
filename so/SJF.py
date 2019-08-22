import operator

def montaTupla(tempo_chegada, duracao_processo, qtd_processos):
    vec_ordenado = []
    aux_Tuple = ()
    for i in range(qtd_processos):
        aux_Tuple = (tempo_chegada[i], duracao_processo[i])
        vec_ordenado.append(aux_Tuple)
    
    # vec_ordenado.sort(key = operator.itemgetter(1))
    # print(vec_ordenado)
    return vec_ordenado

def calcTudo(qtd_processos, tupla):    
    tempo_espera = calcTempoEspera(qtd_processos, tupla)
    tempo_retorno = calcTempoRetorno(qtd_processos, _duracao_processo, tempo_espera)
    tempo_resposta = calcTempoResposta(qtd_processos, _duracao_processo, _tempo_chegada, tempo_espera)
    printaOut(tempo_espera, tempo_retorno, tempo_resposta)
    # print(_tempo_chegada)
    # print(_duracao_processo)

def calcTempoEspera(qtd_processos, tupla):
    processos_comp = 0
    tempo = 0
    testou = false
    tempo_espera = [0] * qtd_processos
    tempo_faltante = [0] * qtd_processos
    minm = 999999999
    short = 0
    for i in range(qtd_processos):
        tempo_faltante[i] = tupla[i][1]

    while (processos_comp != n): 
        for j in range(n): 
            if ((tupla[j][2] <= tempo) and
                (tempo_faltante[j] < minm) and tempo_faltante[j] > 0): 
                minm = tempo_faltante[j] 
                short = j 
                testou = True
        if (testou == False): 
            tempo += 1
            continue
            
        tempo_faltante[short] -= 1
        minm = tempo_faltante[short] 
        if (minm == 0): 
            minm = 999999999

        if (tempo_faltante[short] == 0): 
            processos_comp += 1
            testou = False

            fint = t + 1

            tempo_espera[short] = (fint - tupla[short][1] -    
                                tupla[short][2]) 

            if (tempo_espera[short] < 0): 
                tempo_espera[short] = 0
        
        t += 1
    return tempo_espera

def calcTempoRetorno(qtd_processos, duracao_processo, tempo_espera):
    tempo_retorno = [0] * qtd_processos
    # print(tempo_espera)
    # print(qtd_processos)
    # print(duracao_processo)
    for i in range(qtd_processos):
        # print("Ret = Te(", tempo_espera[i], ") + Tp(", duracao_processo[i], "), em i(", i, ")")
        tempo_retorno[i] = tempo_espera[i] + duracao_processo[i]
    
    # print(tempo_retorno)
    return tempo_retorno

def calcTempoResposta(qtd_processos, duracao_processo, tempo_chegada, tempo_espera):
    tempo_resposta = [0] * qtd_processos
    auxAcumuladora = [0] * qtd_processos
    for i in range(qtd_processos):

        if i == 0:
            tempo_resposta[0] = 0
            auxAcumuladora[0] = duracao_processo[0]
        else:
            # print("Resp: Ti(", tempo_chegada[i], "), Te(", tempo_espera[i], "), Du(", duracao_processo[i], "),  Aux(", auxAcumuladora[i - 1], ") em i(", i, ")")

            tempo_resposta[i] = auxAcumuladora[i - 1] - tempo_chegada[i]
            auxAcumuladora[i] = auxAcumuladora[i - 1] + duracao_processo[i]

    # print(tempo_resposta)
    return tempo_resposta

def calcMedia(vetor):
    total = 0
    for i in vetor:
        total = total + i

    media = total / len(vetor)
    return media

def printaOut(tempo_espera, tempo_retorno, tempo_resposta):
    print("SJF " + str(calcMedia(tempo_retorno)) + " " + str(calcMedia(tempo_resposta)) + " " + str(calcMedia(tempo_espera)))

def run(tempo_chegada, duracao_processo):
    qtd_processos = len(tempo_chegada)
    tupla = montaTupla(tempo_chegada, duracao_processo, qtd_processos)
    calcTudo(tupla, qtd_processos)