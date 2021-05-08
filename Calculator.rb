#!/usr/bin/env ruby
# #############################################################################
# Course: cmps3500
# CLASS Project
# Ruby IMPLEMENTATION OF A CUSTOM MATRIX CALCULATOR
# date: 05/14/2021
# Student 1: Arielle Battle
# Student 2: Janneth Guarcas Garcia
# Student 3: Javier I. Medina
# Description: Implementation of a Matrix calculator in Ruby 05082021
# #############################################################################

require 'csv'

# #############################################################################
# function definitions 

# unary operations per requirements

# NOTES: 

# menu option 1:  
# funtion to load matrix A, takes no parameters, returns matrix
def load_A
    matrix = CSV.parse(File.read("A.csv"), converters: :integer)
    # case for load failure "try again"
end

# menu option 2: 
# function to load matrix B, takes no parameters, returns matrix
def load_B
    matrix = CSV.parse(File.read("B.csv"), converters: :integer)
    # case for load failure "try again"
end

# MENU 3*** make A and square indentity matrix up to oder 10x10: A to I ***
def A_to_I
    #code here
end

# MENU 4*** make B and square indentity matrix up to oder 10x10: A to I ***
def B_to_I
    #code here
end

# menu option 5: 
# function to scalar n times A: n * A where n is an integer, input N
def scale_A(n, matrix_A)
    row = matrix_A[0].length
    col = matrix_A.length
    new_A = Array.new(col){Array.new(row)}

    puts "Scaling Matrix A by n = #{n}"

    i = 0
    matrix_A.each { |array|
        j = 0
        puts array
        array.each { |element|
            new_A[i][j] = element * n
            j += 1
        }
        i += 1
    }
    return new_A
end

# menu option 6: 
# scalar n times B: n * B where n is an integer, input N
def scale_B(n, matrix_B)
    row = matrix_B[0].length
    col = matrix_B.length
    new_B = Array.new(col){Array.new(row)}

    puts "Scaling Matrix A by n = #{n}"

    i = 0
    matrix_B.each { |array|
        j = 0
        puts array
        array.each { |element|
            new_B[i][j] = element * n
            j += 1
        }
        i += 1
    }
    return new_B
end
# menu option 7
# determinant of A: det(A) MAY NEED TO COMBO AS ONE
def det_A(matrix_A)
    # check if matrix is square/non-square
    # rest of code
end

# menu option 8
# determinant of B: det(B) MAY NEED TO COMBO AS ONE
def det_B(matrix_B)
    # check if matrix is square/non-square
    # rest of code
end

# menu option 9
# A transpose: AT
def transpose_A(matrix_A)
    #
end

# menu option 10
# B transpose: BT
def transpose_B(matrix_B)
    #
end

# menu option 11
# inverse of A: A-1
def inverse_A(matrix_A)
    # check if matrix is square
    if is_square(matrix_A)
        puts "you may continue in finding inverse for A"
    else
        puts "Matrix A is NOT a square\n"
        puts "Please try another operation."
    end
end

# menu option 12
# inverse of B: B-1
def inverse_B(matrix_B)
    # check if matrix is square
    if is_square(matrix_B)
        puts "you may continue in finding inverse for B"
    else
        puts "Matrix B is NOT a square\n"
        puts "Please try another operation."
    end
end

# menu option 13
# integer power of A when A is an sqaure matrix: An for 1 ≤ n ≤ 10
def power_A(matrix_A)
    # check if matrix is square
    # rest of code
end

# menu option 14
# integer power of B when B is an sqaure matrix: Bn for 1 ≤ n ≤ 10 
def power_B(matrix_B)
    # check if matrix is square
    # rest of code
end

# binary operations section

# Add A and B: A + B
def add_AB(matrix_A, matrix_B)
    #
end

# Substract A from B: B - A
def sub_AB(matrix_A, matrix_B)
    #
end

# Substract B from A: A - B
def sub_BA(matrix_A, matrix_B)
    #
end

# Multiply A and B: AB
def mult_AB(matrix_A, matrix_B)
    #
end

# Multiply B and A: BA
def mult_BA(matrix_A, matrix_B)
    #
end

# copy A into B: A to B
def copy_AB(matrix_A, matrix_B)
    #
end

# copy B into A: B to A
def copy_BA(matrix_A, matrix_B)
    #
end

# Swap A and B: A to B
def swap_AB(matrix_A, matrix_B)
    #
end

# additional needed functions

# display menu
def display_menu

    puts "----------------------------------------------------------------\n" + 
        "\t\t\tMenu: Choose an option" + 
        "\n----------------------------------------------------------------"
    # clarify 3 and 4 instructions with prof.
    puts "Choice\tDescription\n\n1\tLoad Matrix A\n2\tLoad Matrix B\n" +
        "3\tSet Custom Square Matrix A\n4\tSet Custom Square Matrix B\n" + 
        "3*\tMake A and square indentity(?) matrix up to order 10x10\n" + 
        "4*\tMake B and square indentity(?) matrix up to order 10x10\n" +
        "5\tScalar n times A\n6\tScalar n times B\n" +
        "7\tDeterminant of A\n" + "8\tDeterminant of B\n" +
        "9\t\n" + "10\t\n" +
        "11\tInverse of A: A^-1\n" + "12\tInverse of B: B^-1\n" + 
        "13\t\n" +
        "14\t\n"

end

def check_continue
    valid = false
    while !valid
        print "\nDo you have more operations to perform? (Y/N): "
        cont = gets.chomp
        if cont == "Y" || cont == "y" || cont == "N" || cont == "n"
            user_input = cont
            valid = true
        else
            puts "Invalid choice. Try again"
        end
    end
    return user_input
end



# determine if the matrix is a square
def is_square(matrix)
    puts "youre in the square checker"
    row = matrix[0].length
    col = matrix.length
    puts row
    puts col
    if row == col
        perfect_square = true
    else
        perfect_square = false
    end
end

# NOTE: determine if is int, may be done by implicit function?

# #############################################################################
# variables (may move this section)

matrix_A = Array.new()
matrix_B = Array.new()

puts matrix_A
puts "ABOVE ME"

# may add default matrix cases in case of matrix load/input failure


# #############################################################################
# main script

user_input = "y"

while user_input == "y" || user_input == "Y"

    # display meu
    display_menu

    # obtain user operation choice, start of type checking code
    print "\nEnter choice selection number (1-23): "
    selection = gets.chomp

    case selection
    when '1'
        matrix_A = load_A        
        puts "\nYou have loaded Matrix A."
    when '2'
        matrix_B = load_B        
        puts "\nYou have loaded Matrix B"
    when '3'
        puts "it's a THREE, clarification required"
    when '4'
        puts "it's a FOUR, clarification required"
    when '5'
        if matrix_A.empty?
            print "\nMatrix A is EMPTY! Please Load Matrix A!\n"
        else
            print "Enter an integer to scale Matrix A: "
            user_scale_A = gets.chomp.to_i
            matrix_A = scale_A(user_scale_A, matrix_A)
        end
    when '6'
        # add check if matrices defined yet
        if matrix_B.empty?
            print"\nMatrix B is EMPTY! Please Load Matrix B\n"
        else
            print "Enter an integer to scale Matrix B: "
            user_scale_B = gets.chomp.to_i
            matrix_B = scale_B(user_scale_B, matrix_B)
        end
    when '11'
        if matrix_A.empty?
            print"\nMatrix A is EMPTY! Please Load Matrix B\n"
        else
            inverse_A(matrix_A)
        end
    when '12'
        if matrix_B.empty?
            print"\nMatrix B is EMPTY! Please Load Matrix B\n"
        else
            inverse_B(matrix_B)
        end
    else
        puts "NOT a valid choice, please try again."
    end

    user_input = check_continue
end



# sanity check zone
puts "\n\nMatrices A and B contents."
puts "Matrix A:"
# will print as singular col
# puts matrix_A
print matrix_A
puts "\n"

puts "\nMatrix B:\n"
# will print as singular col
# puts matrix_B
print matrix_B
puts "\n"

matrix_C = CSV.parse(File.read("C.csv"), converters: :integer)

if is_square(matrix_C)
    puts "C matrix is a square too"
end
