# Staircase

# https: // www.hackerrank.com/challenges/staircase/

# Sample Input

# 6
# Sample Output

# #
# ##
# ###
# ####
# #####
# ######

# Mini-Max Sum

# https: // www.hackerrank.com/challenges/mini-max-sum

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example

# The minimum sum is and the maximum sum is . The function prints

# 16 24
# Function Description

# Complete the miniMaxSum function in the editor below.

# miniMaxSum has the following parameter(s):

# arr: an array of  integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format

# A single line of five space-separated integers.

# Constraints


# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14


def staircase(n):
    for i in range(n):
        for j in range(n-1-i, 0, -1):
            print(" ", end="")
        for k in range(0, i+1):
            print("#", end="")
        print("")


        def miniMaxSum(arr):
            arr.sort()
            min = arr[0]+arr[1]+arr[2]+arr[3]
            max = arr[1]+arr[2]+arr[3]+arr[4]
    print(min, max)