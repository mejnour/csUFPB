import re
import FCFS
import SJF
import RR

def populaVec(arq):
    aux = []
    tempo_chegada = []
    duracao_processo = []
    for i in arq:
        aux = i.split(" ")
        auxRE = re.match(r"[0-9]+", aux[1])
        
        tempo_chegada.append(int(aux[0]))
        duracao_processo.append(int(auxRE.group(0)))
    
    FCFS.run(tempo_chegada, duracao_processo)
    SJF.run(tempo_chegada, duracao_processo)
    # RR.run(tempo_chegada, duracao_processo)

def leArq():
    print('O arquivo de input deve estar no mesmo diretorio que este codigo fonte.')
    print('Entre com o nome seguido de extensao do arquivo de input como no exemplo.')
    print('Ex.: \n> input.txt')

    while True:
        try:
            nome_arq = input('> ')
            
            if (nome_arq == 'quit' or nome_arq == 'Quit'): return -1

            path = nome_arq
            arq = open(path, 'r')

            break
        except:
            print('Nao conseguiu fazer load do arquivo. Tente novamente.')
            print('- \'quit\' para terminar este programa.')
            continue

    print('Arquivo carregado.')
    populaVec(arq)

def run():
    leArq()
    
if __name__ == '__main__':
    run()