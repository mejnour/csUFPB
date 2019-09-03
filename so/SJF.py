import sys

def calcTemposFinais(tamanho, chegada, duracao):
    temposFinais = [0] * tamanho
    restante = duracao
    terminou = False
    tempo = 0
    picoRef = sys.maxsize
    picoMin = 0
    indice = 0
    indiceRef = 0

    while terminou != True:
        for i in range(tamanho):
            if (chegada[i] <= tempo):

                # print("Entrou.")
                # print("i:", i)
                print("Restante:", restante[i])
                print("Tempo:", tempo)
                # print("Chegada:", chegada[i])
                # print("Duracao:", duracao[i])
                # print("Pico de Referencia:", picoRef)
                print("Pico Minimo:", picoMin)
                # print("- - - - - - - -")

                tempos_iguais = [x for x in chegada if x == chegada[i]]
                print(tempos_iguais)

                indices_chegadas_iguais = [y for y, x in enumerate(chegada) if x == chegada[i]]
                print(indices_chegadas_iguais)

                valores_indices = [restante[x] for x in indices_chegadas_iguais if x >= 0]
                print(valores_indices)

                # Calcula o pico mínimo entre os valores dos picos dos indices, excluindo o 0
                try:
                    picoMin = min([x for x in valores_indices if x != 0])
                    if ((restante[i] == picoMin) and (picoMin < picoRef)):
                        indice = i
                except:
                    print("+ + + + + + + + + +")
                    continue

                if ((restante[i] == picoMin) and (picoMin != 0) and (picoMin < picoRef) and (indice == i)):
                    restante[i] -= 1
                    picoRef = picoMin

                    if restante[i] == 0:
                        temposFinais[i] = tempo + 1
                        picoRef = sys.maxsize
                        picoMin = 0

                    tempo += 1

                    print(restante)
                    print(temposFinais)
                    print("+ + + + + + + + + +")
                    continue

                print("+ + + + + + + + + +")

        # if (max(restante) == 0):
        #     terminou = True

        if tempo >= 44:
            terminou = True

if __name__ == "__main__":
    cheg = [0, 0, 4, 4]
    dur = [20, 10, 6, 8]
    tam = len(cheg)
    calcTemposFinais(tam, cheg, dur)
