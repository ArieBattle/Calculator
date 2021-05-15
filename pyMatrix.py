#!/uesr/bin/env python

'''
CLASS PROJECT
COURSE: CMPS3500
STUDENTS:
    Arielle Battle
    Javier Medina
DESC: Implementation of Matrix calculator using Python
'''

import csv
import numpy as np
import cgi

def getMenu():
    print("1. View Matrix A")
    print("2. View Matrix B")
    print("3. Add A + B")
    print("4. Subtract A - B")
    print("5. Subtract B - A")
    print("6. Multiply A * B")
    print("7. Multiply B * A")
    print("8. Copy A to B")
    print("9. Copy B to A")
    print("10. Swap A and B")
    print("11. Make A and square identity matrix up to order 10x10: A to I")
    print("12. Make B and square identity matrix up to order 10x10: B to I")
    print("13. Scalar n times A: nA where n is an int")
    print("14. Scalar n times B: nA where n is an int")
    print("15. Determinant of A: det(A)")
    print("16. Determinant of B: det(B")
    print("17. A transpose: A^T")
    print("18. B transpose: B^T")
    print("19. Inverse of A: A^-1")
    print("20. Inverse of B: B^-1")
    print("21. Int power of A when A is a square matrix: A^n for 1 <= n <=10")
    print("22. Int power of B when B is a square matrix: B^n for 1 <= n <=10")
    print("23. Load new matrix")
    print("0. Exit")
    
    print("24: Print Menu")
    

def load_in_A():
    A=[]
    csv_file = open('A.csv', 'r')
    matrix = csv.reader(csv_file, delimiter=',')
    for row in matrix:
        A.append(row)
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                A[i][j] = int(A[i][j])
            
    return A

def load_in_B():
    B=[]
    csv_file = open('B.csv', 'r')
    matrix = csv.reader(csv_file, delimiter=',')
    for row in matrix:
        B.append(row)
        for i in range(0, len(B)):
            for j in range(0, len(B[0])):
                B[i][j] = int(B[i][j])
    return B


def loadGeneric():
    gen = []
    global is_matrix
    is_matrix = False
    
    if('mat_file' in globals()):
        csv_file = open(mat_file, 'r')
    matrix = csv.reader(csv_file, delimiter=',')
    for row in matrix:
        gen.append(row)
        for i in range(0, len(gen)):
            for j in range(0, len(gen[0])):
                try:
                    is_matrix = True
                    gen[i][j] = int(gen[i][j])
                except ValueError:
                    print("Trouble loading matrix. Make sure each value is of type integer!")
                    return[None]
    return gen

def addMatrices(mat1, mat2):
    addMat = [[0 for i in range(len(mat1))] for j in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            addMat[i][j] = mat1[i][j] + mat2[i][j]
    return addMat

def matrixSubtraction(mat1, mat2):
    subMat = [[0 for i in range(len(mat1))] for j in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            subMat[i][j] = mat1[i][j] - mat2[i][j]
    return subMat

def CopyMatrix(mat1,mat2):
    mat1 = mat2
    return mat1

def swapAB():
    matrix1 = load_in_A()
    matrix2 = load_in_B()

    temp = matrix2
    matrix2 = matrix1
    matrix1 = temp

    print("matrix A: \n")
    print(np.matrix(matrix1))
    print("matrix B: \n")
    print(np.matrix(matrix2))

def multiply_matrix(mat1, mat2):
    res = [[0 for col in range(len(mat2[0]))] for rows in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

def identityMatrix(size):
    if(size==1):
        return [1]
    
    iden = [[0 for i in range(size)] for j in range(size)]

    for i in range(len(iden)):
        for j in range(len(iden)):
            if(i == j):
                iden[i][j] = 1
    return iden

def identityA(size):
    matA = load_in_A()
    matA = identityMatrix(size)
    print(np.matrix(matA))


def identityB(size):
    matB = load_in_B()
    matB = identityMatrix(size)
    print(np.matrix(matB))

def scalarMultiplication(matrix, n):
    res = [[None] * len(matrix) for step in range(len(matrix))]

    for i in range(len(res)):
        for j in range(len(res)):
            res[i][j] = matrix[i][j] * n
    return res

def Determinant(matrix):
    if(len(matrix) == 2):
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det

    dsum = 0

    for cur_col in range(len(matrix)):
        sign = (-1) ** (cur_col)

        sDet = Determinant(cofactor(matrix, 0, cur_col))

        dsum += (sign * matrix[0][cur_col] * sDet)

        return dsum

def cofactor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def cofactorNo(matrix, i, j):
    subMatrix = [[None] * (len(matrix)-1) for x in range(len(matrix)-1)]
    subRow = 0
    subCol = 0

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            if(row != i and col != j):
                subMatrix[subRow][subCol] = matrix[row][col]
                subCol += 1
                if(subCol == (len(matrix)-1)):
                    subCol = 0
                    subRow += 1

    return subMatrix

def transposeMatrix(matrix):
    mat = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return mat

def inverseMatrix(matrix):
    dt = Determinant(matrix)

    adj = adjointMatrix(matrix)
    
    inv = [[None] * len(matrix) for step in range(len(matrix))]
    for i in range(len(adj)):
        for j in range(len(adj)):
            inv[i][j] = adj[i][j]/float(dt)
    return inv

def adjointMatrix(matrix):
    adj = [[None]*len(matrix) for step in range(len(matrix))]
    if(len(matrix) == 1):
        adj = [1]
        return adj
    
    sign = 1

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if((i+j)%2 ==0):
                sign = 1
            else:
                sign = -1
            adj[j][i] = sign * Determinant(cofactorNo(matrix, i, j))

    return adj

def matrixPower(matrix):
    matRow = len(matrix)
    matCol = len(matrix[0])
    global power

    if matRow == matCol:
        power = -1
        tmp = matrix
        power = int(input("Enter a value n to raise matrix to: \n"))
        
        if(power > 0):
            for i in range(power-1):
                tmp = multiply_matrix(matrix, tmp)
            return tmp
        else:
            print("enter valid power")
    else:
        print("Must provide a square matrix")

getMenu()

# Load in matrices before main body runs

matrixA = load_in_A()
matrixB = load_in_B()

#this will get the data entered from html page
#selection = request.GET['select']
selection = 99 #Base case


while selection != 0:

    selection = int(input("\nEnter choice 1-23 (24 to see menu or 0 to exit): "))
    
    if selection == 1:
        print("A: \n")
        print(np.matrix(matrixA))

    elif selection == 2:
        print("B: \n")
        print(np.matrix(matrixB))
    
    elif selection == 3:
        add_result = addMatrices(matrixA, matrixB)
        print("Added matrix: \n")
        print(np.matrix(add_result))
    
    elif selection == 4:
        AsubB = matrixSubtraction(matrixA, matrixB)
        print("A - B = \n")
        print(np.matrix(AsubB))
    
    elif selection == 5:
        BsubA = matrixSubtraction(matrixB, matrixA)
        print("B - A = \n")
        print(np.matrix(BsubA))

    elif selection == 6:
        AmultB = multiply_matrix(matrixA, matrixB)
        print("A * B: \n")
        print(np.matrix(AmultB))

    elif selection == 7:
        BmultA = multiply_matrix(matrixB, matrixA)
        print("B * A: \n")
        print(np.matrix(BmultA))

    elif selection == 8:
        copyAB = CopyMatrix(matrixA, matrixB)
        print("B copied into A: \n")
        print(np.matrix(copyAB))
    
    elif selection == 9:
        copyBA = CopyMatrix(matrixB, matrixA)
        print("A copied into B: \n")
        print(np.matrix(copyBA))
    
    elif selection == 10:
        print("Swapped matrices: \n")
        swap = swapAB()
        print(swap)
        
    elif selection == 11:
        if(len(matrixA[0]) == len(matrixA)):
            print("identity for matrix A: \n")
            idenA = identityA(len(matrixA))
        else:
            print("A is not a square matrix")
    
    elif selection == 12:
        if(len(matrixB[0]) == len(matrixB)):
            print("identity for matrixB: \n")
            idenB = identityB(len(matrixB))
        else:
            print("B is not a square matrix")

    elif selection == 13:
        nA = int(input("Input a value n to multiply matrix A by: "))
        scalarA = scalarMultiplication(matrixA, nA)
        print("Matrix A multiplied by " + str(nA) + ":\n")
        print(np.matrix(scalarA))
    
    elif selection == 14:
        nB = int(input("Input a value n to multiply matrix B by: "))
        scalarB = scalarMultiplication(matrixB, nB)
        print("Matrix B multiplied by " + str(nB) + ":\n")
        print(np.matrix(scalarB))

    elif selection == 15:
        if(len(matrixA[0]) == len(matrixA)):
            detA = Determinant(matrixA)
            print("The determinant of matrix A is : "+ str(detA))
        else:
            print("Determinant must be a square matrix")

    elif selection == 16:
        if(len(matrixB[0]) == len(matrixB)):
            detB = Determinant(matrixB)
            print("The determinant of matrix B is: "+ str(detB))
        else:
            print("Determinant must be a square matrix")
    
    elif selection == 17:
        tposeA = transposeMatrix(matrixA)
        print("Matrix A transposed: \n")
        print(np.matrix(tposeA))

    elif selection == 18:
        tposeB = transposeMatrix(matrixB)
        print("Matrix B transposed: \n")
        print(np.matrix(tposeB))

    elif selection == 19:
        invA = inverseMatrix(matrixA)
        print("the inverse matrix for A is: \n")
        print(np.matrix(invA))
    
    elif selection == 20:
        invB = inverseMatrix(matrixB)
        print("The inverse matrix for B is: \n")
        print(np.matrix(invB))
    
    elif selection == 21:
        powA = matrixPower(matrixA)
        if('power' in globals()):
            print("Matrix with given power " + str(power) +":\n")
        print(np.matrix(powA))

    elif selection == 22:
        powB = matrixPower(matrixB)
        if('power' in globals()):
            print("Matrix B with given power "+ str(power) +":\n")
        print(np.matrix(powB))

    elif selection == 23:
        global mat_file
        mat_file = str(raw_input('Type in new .csv matrix file: \n'))


        new_matrix = loadGeneric()
        if('is_matrix' in globals()):
            if(is_matrix == True):
                print("New matrix Loaded: \n")
                print(np.matrix(new_matrix))
        else:
            continue

    elif selection == 24:
        getMenu()

    elif selection < 0:
        print("\nPLEASE ENTER A VALID INPUT")
        getMenu()
    
    elif selection > 23:
        print("\nPLEASE INPUT A VALID INPUT")
        getMenu()


