# Course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION OF A CUSTOM MATRIX CALCULATOR
# date: 05/14/2021
# Student 1: Arielle Battle
# Student 2: Janneth Guarcas Garcia
# Student 3: Javier Medina
# Description: Implementation of a Matrix calculator in Python 2

import csv
import sys
import codecs
import math
import numpy as np

menu = {}
menu['\n01']="Load matrix: Load B"
menu['02']="Load matrix: Load A"
menu['03']="ADD A and B: A + B"
menu['04']="Subtract A from B: A - B"
menu['05']="Subtract B from A: B - A"
menu['06']="Multiply A and B: AB"
menu['07']="Multiply B and A: BA"
menu['08']="Copy A into B: A to B"
menu['09']="Copy B into A: B to A"
menu['10']="Swap A and B: A to B"
menu['11']="Make A and square identify matrix up to order 10x10: A to I"
menu['12']="Make B and square identify matrix up to order 10x10: B to I"
menu['13']="Scalar n times A: nA where n is an integer"
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

A = []
B = []

#file for loading a file for A.csv
def loadingA(AFile):
    with codecs.open(AFile, 'r', encoding="utf-8-seg") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for item in row:
                A.append(int(item))
        print (" ")
        print ("A is loaded")
        print (A)

#file for loading a file for B.csv
def loadingA(AFile):
    with codecs.open(AFile, 'r', encoding="utf-8-seg") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for item in row:
                A.append(int(item))
        print (" ")
        print ("A is loaded")
        print (A)

#function for add

#function for subtract A - B
#function for subtract B - A
#function for multiply AB
#function for multiply BA
#function for copying A into B
#function for copying B into A

#function for making A and square identify matrix up to oder 10x10: A to I
def squareIdentityA(A):
    global numpyForA
        ANumpy = np.array(A) #converts listA into an np array
        NoElem = len(ANumpy)
        root = math.sqrt(NoElem)
        if int(root + 0.5) ** 2 != NoElem or NoElem > 100:
            print " "
            print "File A can't be squared or is beyond the scope of a 10X10 matrix"
            print "number of elements: ", NoElem
        else:
            size = int(root)
            Aarray = np_array.reshape(size,size) #reshape matrix square dimensions
            print " "
            print "File A square identity matrix of ",np.shape(Aarray)# print A square matrix
            print aAarray

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
        print (entry, menu[entry])

    #has to be 'raw_input' in order to make selections for menu
    selection = raw_input("\nEnter Choice #: ")
    if selection =='1':
        result = np.sum(Afile_numpy, Bfile_numpy)
        print (result)

        #this will open the file and read in the numbers
        with open('A.csv', 'rb') as f:
            reader = csv.reader(f)
            data_as_list = list(reader)
            print (data_as_list)

        print (Afile_numpy)

    elif selection == '2':
        result = np.subtract(Afile_numpy, Bfile_numpy)
        print (result)

        #this will open the file and read in the numbers
        B = int (input("input integer for B: "))
        with open('B.csv', 'rb') as f:
            reader = csv.reader(f)
            data_as_list = list(reader)
            print (data_as_list)

        print (Bfile_numpy)

    elif selection == '3':
        result = np.subtract(Bfile_numpy, Afile_numpy)
        print (result)

    elif selection == '4':
        result = np.dot(Afile_numpy, Bfile_numpy)
        print (result)

    elif selection == '5':
        result = np.dot(Bfile_numpy, Afile_numpy)
        print (result)

    elif selection == '6':
        AFilecopy = np.matrix(Afile_numpy)
        result = np.copy(AFilecopy)
 
    elif selection == '7':
        
    elif selection == '8':
        #opens file for A.csv
        Afile = open("A.csv")
        Afile_numpy = np.genfromtxt(Afile, delimeter = ",", skip_header = 1)

        #this will copy and then print
        result = np.concatenate(Afile, delimeter = ",", skip_header = 1)
        print(result)

    elif selection == '9':
        #opens file fro B.csv
        Bfile = open("B.csv")
        Bfile_numpy = np.genfromtxt(Bfile, delimeter = ",", skip_header = 1)

        #this will copy and then print
        result = np.concatenate(Bfile, delimeter = ",", skip_header = 1)
        print(result)

    elif selection == '10':
       
    elif selection == '11':
       
    elif selection == '12':

    elif selection == '13':

    elif selection == '14':

    elif selection == '15':

    elif selection == '16':

    elif selection == '17':

    elif selection == '18':

    elif selection == '19':

    elif selection == '20':

    elif selection == '21':

    elif selection == '22':

    elif selection == '23':
        print("\nExiting program")
        break

    else:
        print("\nMust be a number on menu!\n")
