#!/usr/bin/env ruby
# #############################################################################
# Course: cmps3500
# CLASS Project
# Ruby IMPLEMENTATION OF A CUSTOM MATRIX CALCULATOR
# date: 05/14/2021
# Student 1: Arielle Battle
# Student 2: Janneth Guarcas Garcia
# Student 3: Javier I. Medina
# Description: Implementation of a Matrix calculator in Ruby
# #############################################################################

require 'csv'

# #############################################################################
# function definitions 

# unary operations per requirements

def load_A
    matrix_A = CSV.parse(File.read("A.csv"), converters: :integer)
    # case for load failure "try again"
end


def load_B
    matrix_B = CSV.parse(File.read("B.csv"), converters: :integer)
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

# NOTE: 

# #############################################################################
# variables (may move this section)

# #############################################################################
# main script


display_menu

     


print "\nEnter choice selection number (1-23): "
selection = gets
# in progress testing
case selection
when String
    puts "it's a string"
when Fixnum
    puts "it's a number"
else
    puts "is neither"
end

# sanity check
matrix_A = CSV.parse(File.read("A.csv"), converters: :integer, headers: false)
matrix_B = CSV.parse(File.read("B.csv"), converters: :integer, headers: false)

puts "\n\nMatrices A and B loaded successfully."
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


