#!/usr/bin/env ruby
# #############################################################################
# Course: cmps3500
# CLASS Project
# Ruby IMPLEMENTATION OF A CUSTOM MATRIX CALCULATOR
# date: 05/14/2021
# Student 1: Arielle Battle
# Student 2: Janneth Guarcas Garcia
# Student 3: Javier I. Medina
# Description: Implementation of a Matrix calculator in Ruby 5/1/221 time: 1921
# #############################################################################

require 'csv'

# #############################################################################
# function definitions 

# unary operations per requirements

# to load matrix A, takes no parameters, returns nothing
# NOTES: * in-progress, may return the matrix at call
#        * checks for square may be implemented as another function

def load_A
    matrix = CSV.parse(File.read("A.csv"), converters: :integer)
    # case for load failure "try again"
end

# to load matrix B, takes no parameters, returns nothing
def load_B
    matrix = CSV.parse(File.read("B.csv"), converters: :integer)
    # case for load failure "try again"
end

# *** make A and square indentity matrix up to oder 10x10: A to I ***
def A_to_I
    #code here
end

# *** make B and square indentity matrix up to oder 10x10: A to I ***
def B_to_I
    #code here
end

# Condense descs
# scalar n times A: n * A where n is an integer, input N
def scale_A(n)
    #code here
    puts "Scaling Matrix A by n = #{n}"
end

# scalar n times B: n * B where n is an integer, input N
def scale_B(n)
    #code here
end

# determinant of A: det(A) MAY NEED TO COMBO AS ONE
def det_A(matrix_A)
    # check if matrix is square/non-square
    # rest of code
end

# determinant of B: det(B) MAY NEED TO COMBO AS ONE
def det_B(matrix_B)
    # check if matrix is square/non-square
    # rest of code
end

# A transpose: AT
def transpose_A(matrix_A)
    #
end

# B transpose: BT
def transpose_B(matrix_B)
    #
end
# inverse of A: A-1
def inverse_A(matrix_A)
    # check if matrix is square
    # rest of code
end

# inverse of B: B-1
def inverse_B(matrix_B)
    # check if matrix is square
    # rest of code
end

# integer power of A when A is an sqaure matrix: An for 1 ≤ n ≤ 10
def power_A(matrix_A)
    # check if matrix is square
    # rest of code
end

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
        "7\tDeterminant of A"
end

# determine if the matrix is a square
def is_square(matrix)
    # code here
end

# NOTE: determine if is int, may be done by implicit function?

# #############################################################################
# variables (may move this section)



# may add default matrix cases in case of matrix load/input failure


# #############################################################################
# main script

user_input = "y"

while user_input == "y" || user_input == "Y"

    display_menu

    print "\nEnter choice selection number (1-23): "
    selection = gets.chomp

    case selection
    when '1'
        matrix_A = load_A        
        puts "it's a ONE, You have loaded Matrix A"
    when '2'
        puts "it's a TWO, you have loaded Matrix B"
        matrix_B = load_B
    when '3'
        puts "it's a THREE, clarification required"
    when '4'
        puts "it's a FOUR, clarification required"
    when '5'
        # add check if matrices defined yet
        puts "it's a FIVE."
        print "Enter an integer to scale Matrix A: "
        user_scale_A = gets.chomp.to_i
        scale_A(user_scale_A)
    when '6'
        # add check if matrices defined yet
        puts "it's a SIX."
        print "Enter an integer to scale Matrix B: "
        user_scale_B = gets.chomp.to_i
        puts "Scaling Matrix A by n = #{user_scale_B}"
    else
        puts "NOT a valid choice, please try again."
    end

    # more for testing purposes
    #load_A
    #load_B

    # sanity check

    # load matrices A and B from current directory (for testing purposes)
    # same commands as in functions 1 and 2 (keep for testing purposes)
    #matrix_A = CSV.parse(File.read("A.csv"), converters: :integer, headers: false)
    #matrix_B = CSV.parse(File.read("B.csv"), converters: :integer, headers: false)
    puts "\nAction completed, do you have more operations to perform? (Y/N): "
    user_input = gets.chomp

end
puts "\n\nMatrices A and B contents."
puts "Matrix A:"
# puts matrix_A
print matrix_A
puts "\n"
puts "\nMatrix B:\n"
# puts matrix_B
print matrix_B
puts "\n"
