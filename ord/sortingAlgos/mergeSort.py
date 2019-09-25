import sys

def mergeSort(A, p, r):
    pass
    if p < r:
        q = floor( (p + r) / 2)
        mergeSort(A, p, q)
        mergeSort(A, (q + 1), r)
        merge(A, p, q, r)
        

def merge(A, p, q, r):
    pass
    L = [A[x] for x in range(p, q)]
    R = [A[x] for x in range((q + 1), r)]

    L.append(INF)
    R.append(INF)

    i = j = 1
    for k in range(p, r):
        if (L[i] < R[j]):
            A[k] = L[i]
            i += 1
        
        else:
            A[k] = R[j]
            j += 1

def run():
    pass

if __name__ == "__main__":
    pass
    run()