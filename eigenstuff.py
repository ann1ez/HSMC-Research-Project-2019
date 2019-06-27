#first create a txt file called matrix and type in the matrix
#returns E-values and E-vectors for a specified matrix in the file matrix.txt

import numpy as np
import scipy.linalg as la
def read():
    f = open('matrix.txt', 'r')
    temp = f.read().split('\n')
    arr = []
    for i in temp:
        if i == '':
            continue
        arr.append(i.split(" "))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
    return arr

def main():
    arr = read()
    matrix = np.array(arr)
    print("Given the matrix:")
    print(matrix)
    evals, evecs = la.eig(matrix)
    evals = evals.real
    print("Eigenvalues")
    print(evals)
    print("Corresponding eigenvectors")
    print(evecs)

if __name__ == '__main__':
    main()
