import sys
from time import process_time

def selectionSort(unord_list):
    index = 0
    checked = False
    for i in range(len(unord_list)):
        selection = unord_list[i]
        checked = True
        for j in range(i + 1, len(unord_list)):
            if (unord_list[j] < selection):
                selection = unord_list[j]
                index = j
                checked = False
        
        # Variavel checked resolve problema dos indices
        # não atualizaveis (comentar tudo de checked pra simular
        # problema)
        if (checked == True):
            continue

        swap = unord_list[i]
        unord_list[i] = selection
        unord_list[index] = swap

        # if (i >= len(unord_list) - 5):
        #     print("A - - - - - - - - - - - - - -")
        #     print("i", i)
        #     print("sel", selection)
        #     aux = [unord_list[x] for x in range(len(unord_list) - 5, len(unord_list))]
        #     print(aux)
        #     print("B - - - - - - - - - - - - - -")
        
    # print(unord_list)
        
def run():
    try:
        file = open(sys.argv[1], 'r')
        uList = file.read().splitlines()
        uList = [int(x) for x in uList]
        
        selectionSort(uList)
        
        t1_stop = process_time()
        print("Elapsed: {0:.3f}".format(t1_stop - t1_start))

    except Exception as e:
        print(str(e))

    # uList = [26, 1000, 58119, -2, 14, -29, -14, 24, -48, 8, 42]
    # selectionSort(uList)

if __name__ == "__main__":
    t1_start = process_time()
    run()