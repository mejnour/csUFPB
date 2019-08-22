import operator

def ordenaVec(tempo_chegada, duracao_processo, qtd_processos):
    vec_ordenado = []
    aux_Tuple = ()
    for i in range(qtd_processos):
        aux_Tuple = (tempo_chegada[i], duracao_processo[i])
        vec_ordenado.append(aux_Tuple)
    
    vec_ordenado.sort(key = operator.itemgetter(1))
    # print(vec_ordenado)
    return vec_ordenado

def calcTudo(vec_ord    enado, qtd_processos):
    _tempo_chegada = []
    _duracao_processo = []
    for i in vec_ordenado:            
        _tempo_chegada.append(i[0])
        _duracao_processo.append(i[1])
    
    print(_tempo_chegada)
    print(_duracao_processo)
    tempo_espera = calcTempoEspera(qtd_processos, _tempo_chegada, _duracao_processo)
    tempo_retorno = calcTempoRetorno(qtd_processos, _duracao_processo, tempo_espera)
    tempo_resposta = calcTempoResposta(qtd_processos, _duracao_processo, _tempo_chegada, tempo_espera)
    printaOut(tempo_espera, tempo_retorno, tempo_resposta)
    # print(_tempo_chegada)
    # print(_duracao_processo)

def calcTempoEspera(qtd_processos, tempo_chegada, duracao_processo):
    tempo_espera = [0] * qtd_processos
    for i in range(0, qtd_processos):
        if i == 0:
            tempo_espera[0] = 0 + tempo_chegada[i]
        else:
            tempo_espera[i] = duracao_processo[i - 1] + tempo_espera[i - 1] - (tempo_chegada[i] - tempo_chegada[i - 1])

    # print(tempo_espera)
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
    vec_ordenado = ordenaVec(tempo_chegada, duracao_processo, qtd_processos)
    calcTudo(vec_ordenado, qtd_processos)