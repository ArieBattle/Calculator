# Course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION OF A CUSTOM MATRIX CALCULATOR
# date: 05/14/2021
# Student 1: Arielle Battle
# Student 2: Janet Garcia
# Student 3: Javier Medina
# Description: Implementation of a scientific calculator ..

import csv
import numpy as np

menu = {}
menu['\n01']="ADD A and B: A + B"
menu['02']="Subtract A from B: A - B"
menu['03']="Subtract B from A: B - A"
menu['04']="Multiply A and B: AB"
menu['05']="Multiply B and A: BA"
menu['06']="Copy A into B: A to B"
menu['07']="Copy B into A: B to A"
menu['08']="Swap A and B: A to B"
menu['09']="Load matrix: Load A"
menu['10']="Load matrix: Load B"
menu['11']="Make A and square identify matrix up to oder 10x10: A to I"
menu['12']="Make B and square identify matrix up to oder 10x10: B to I"
menu['13']="Scalar n times A: nAwhere n is an integer"
menu['14']="Scalar n times B: nA where n is an integer"
menu['15']="Determine of A: det(A)"
menu['16']="Determine of B: det(B)"
menu['17']="A transpose: A^T"
menu['18']="A transpose: B^T"
menu['19']="Inverse of A: A^-1"
menu['20']="Inverse of B: B^-1"
menu['21']="Integer power of A when A is a square matrix: A^n for 1 <= n <= 10"
menu['22']="Integer power of B when B is a square matrix: B^n for 1 <= n <= 10"
menu['23']="Exit"

#function for add
def add(A, B):
    return A + B

#function for subtract A - B
def subtractAB(A, B):
    return A - B

#function for subtract B - A
def subtractBA(A, B):
    return B - A

#function for multiply AB
def multiplyAB(A, B):
    return A * B

#function for multiply BA
def multiplyBA(A, B):
    return B * A

#function for copying A into B---------------------------
#not sure if he wants us to keep the original number for B, same goes for the one below or use the copy funct for deep or shallow copy
def copyAintoB(A, B):
    temp = 0
    temp = A
    B = temp
    return B

#function for copying B int A---------------------------
#same goes for this question
def copyBintoA(A, B):
    temp = 0
    temp = B
    A = temp
    return A

#function for making A and square identify matrix up to oder 10x10: A to I
#function for making B and square identify matrix up to oder 10x10: A to I
#function for scalar n times A
#function for scalar n times B
#function for det(A)
#function for det(B)
#function for transpose A
#function for transpose B
#function for inverse A
#function for inverse B
#function for Integer power of A when A is a square matrix
#function for Integer power of B when B is a square matrix

#while its not exit run menu program
while True:

    #get users input
    options=menu.keys()
    options.sort()

    for entry in options:
        print entry, menu[entry]

    #has to be 'raw_input' in order to make selections for menu
    selection = raw_input("\nEnter Choice: ")
    if selection =='1':
        A = float (input("Input integer for A: "))
        B = float (input("input integer for B: "))
        print A, "+", B, "=", add(A, B)

    elif selection == '2':
        A = float (input("Input integer for A: "))
        B = float (input("input integer for B: "))
        print A, ' - ', B, ' = ', subtractAB(A, B)

    elif selection =='3':
        A = float (input("Input integer for A: "))
        B = float (input("input integer for B: "))
        print A, " - ", B, " = ", subtractBA(A, B)

    elif selection == '4':
        A = float (input("Input integer for A: "))
        B = float (input("input integer for B: "))
        print B, " * ", A, " = ", multiplyAB(A, B)

    elif selection =='5':
        A = float (input("Input integer for A: "))
        B = float (input("input integer for B: "))
        print B, " * ", A, " = ", multiplyBA(A, B)

    elif selection == '6':
        A = float (input("Input integer for A: "))
        B = float (input("input integer for B: "))
        print "B = ", B, copyAintoB(A, B)

    elif selection =='7':
        A = float (input("Input integer for A: "))
        B = float (input("input integer for B: "))
        print  copyBintoA(A, B),"A = ", A,

    elif selection == '8':
        A = float (input("Input integer for A: "))
        B = float (input("input integer for B: "))
        print "\nBefore swap: A = ", A, " B = ", B

        temp = 0
        temp2 = 0
        temp = A
        del A
        temp2 = B
        del B
        A = temp2
        B = temp

        print "After Swapping: A = ", A, " B = ", B

    elif selection =='9':
        #this will open the file and read in the numbers
        with open('A.csv', 'rb') as f:
            reader = csv.reader(f)
            data_as_list = list(reader)
            print data_as_list

    elif selection == '10':
        #this will open the file and read in the numbers
        B = float (input("input integer for B: "))
        with open('B.csv', 'rb') as f:
            reader = csv.reader(f)
            data_as_list = list(reader)
            print data_as_list

    elif selection =='11':
        A = float (input("Input integer for A: "))

    elif selection == '12':
        B = float (input("input integer for B: "))

    elif selection =='13':
        A = float (input("Input integer for A: "))

    elif selection == '14':
        B = float (input("input integer for B: "))

    elif selection =='15':
        A = float (input("Input integer for A: "))
         reader = csv.reader(f)
         data_as_list = list(reader)
         #deter = np(data_as_list)


         print np.linalg.det(data_as_list)

    elif selection == '16':
        B = float (input("input integer for B: "))

    elif selection =='17':
        A = float (input("Input integer for A: "))

    elif selection == '18':
        B = float (input("input integer for B: "))

    elif selection == '19':
        A = float (input("Input integer for A: "))

    elif selection =='20':
        B = float (input("input integer for B: "))

    elif selection == '21':
        A = float (input("Input integer for A: "))

    elif selection =='22':
        B = float (input("input integer for B: "))

    elif selection == '23':
        print("\nExiting program")
        break

    else:
        print("\nMust be a number on menu!\n")
