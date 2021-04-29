# Course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION OF A CUSTOM MATRIX CALCULATOR
# date: 05/14/2021
# Student 1: Arielle Battle
# Student 2: 
# Student 3: 
# Description: Implementation of a scientific calculator ..

menu = {}
menu['1']="ADD A and B: A + B"
menu['2']="Subtract A from B: B - A"
menu['3']="Subtract B from A: A - B"
menu['4']="Multiply A and B: AB"
menu['5']="Multiply B and A: BA"
menu['6']="Copy A into B: A to B"
menu['7']="Copy B into A: B to A"
menu['8']="Swap A and B: A to B"
menu['9']="Load matrix: Load A"
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

while True:
    options=menu.keys()
    options.sort()
    for entry in options:
        print entry, menu[entry]

    #has to be 'raw_input' in order to make selections 
    selection = raw_input("Please select: ")
    if selection =='1':
        print("Input integer for A: ")
        print("Input integer for A: ")

    elif selection == '23':
        print("\nBYE")
        break
    else:
        print("\nMust be a number on menu!\n")
