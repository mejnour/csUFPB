import sys

def swap(elem1, elem2):
    pass

def partition(A, inicio, fim):
    pass
    pivo = A[inicio]
    i = inicio - 1
    j = fim + 1

    while True:
        while (A[i] <= pivo):
            i += 1

        while (A[j] <= pivo
            j -= 1

        if (i >= j):
            break;
        
        swap(A[i], A[j])

    swap(A[inicio], A[j])

def quickSort(A, l, r):
    pass
    if (l < r):
        q = partition(A, l, r)
        quickSort(A, l, (q - 1))
        quickSort(A, (q + 1), r)

def run():
    pass

if __name__ == "__main__":
    pass
    run()