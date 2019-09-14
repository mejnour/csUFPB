import sys
from time import process_time

def insertionSort(unord_list):
    for i in range(1, len(unord_list)):
        index = i - 1
        while True:
            if (unord_list[index + 1] <= unord_list[index]):
                anterior = unord_list[index]
                unord_list[index] = unord_list[index + 1]
                unord_list[index + 1] = anterior
                
                index -= 1
                if (index < 0):
                    break

            else:
                break 

    # print(unord_list)

def run():
    try:
        file = open(sys.argv[1], 'r')

        uList = file.read().splitlines()
        uList = [int(x) for x in uList]

        insertionSort(uList)
        t1_stop = process_time()
        elapsed = ( t1_stop - t1_start )
        print("Elapsed time: {0:.2f}s".format(elapsed))

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    t1_start = process_time()
    run()