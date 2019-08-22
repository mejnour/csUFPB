def calcTempoEspera(qtd_processos, tempo_chegada, duracao_processo):
    pass

def calcTempoRetorno(qtd_processos, duracao_processo, tempo_espera):
    pass

def calcTempoResposta(qtd_processos, duracao_processo, tempo_chegada, tempo_espera):
    pass

def calcMedia(vetor):
    total = 0
    for i in vetor:
        total = total + i

    media = total / len(vetor)
    return media

def printaOut(tempo_espera, tempo_retorno, tempo_resposta):
    print("FCFS " + str(calcMedia(tempo_retorno)) + " " + str(calcMedia(tempo_resposta)) + " " + str(calcMedia(tempo_espera)))

def run(tempo_chegada, duracao_processo):
    qtd_processos = len(tempo_chegada)
    tempo_espera = calcTempoEspera(qtd_processos, tempo_chegada, duracao_processo)
    tempo_retorno = calcTempoRetorno(qtd_processos, duracao_processo, tempo_espera)
    tempo_resposta = calcTempoResposta(qtd_processos, duracao_processo, tempo_chegada, tempo_espera)
    printaOut(tempo_espera, tempo_retorno, tempo_resposta)