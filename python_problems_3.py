# String Split and Join

# https: // www.hackerrank.com/challenges/python-string-split-and-join

# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Function Description

# Complete the split_and_join function in the editor below.

# split_and_join has the following parameters:

# string line: a string of space-separated words
# Returns

# string: the resulting string
# Input Format
# The one line contains a string consisting of space separated words.

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    print(line)

# Diagonal Difference

# https://www.hackerrank.com/challenges/diagonal-difference

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix is shown below:

# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

# Function description

# Complete the  function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference
# Input Format

# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

# Constraints

# Output Format

# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.


def diagonalDifference(arr):
    right = 0
    left = 0
    for i in range(n):
        if -1 < n-i <= n:
            right += arr[i][i]
            left += arr[i][n-1-i]
    return abs(left-right)


# Plus Minus

# https://www.hackerrank.com/challenges/plus-minus

# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example

# There are  elements, two positive, two negative and one zero. Their ratios are, and . Results are printed as:

# 0.400000
# 0.400000
# 0.200000
# Function Description

# Complete the plusMinus function in the editor below.

# plusMinus has the following parameter(s):

# int arr[n]: an array of integers
# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with digits after the decimal. The function should not return a value.

# Input Format

# The first line contains an integer, , the size of the array.
# The second line contains  space-separated integers that describe .

# Constraints


# Output Format

# Print the following  lines, each to  decimals:

# proportion of positive values
# proportion of negative values
# proportion of zeros


def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for i in range(n):
        if arr[i] > 0:
            pos = pos + 1
        elif arr[i] == 0:
            zer = zer + 1
        else:
            neg = neg + 1
    neg = neg / n
    pos = pos / n
    zer = zer / n
    print(pos)
    print(neg)
    print(zer)
