# Write a function

# https://www.hackerrank.com/challenges/write-a-function/

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap funct


def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))

# List Comprehensions

# https://www.hackerrank.com/challenges/list-comprehensions

# You are given three integers and representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

# Example


# All permutations of  are:
# .

# Print an array of the elements that do not sum to .


# Input Format

# Four integers  and, each on a separate line.

# Constraints

# Print the list in lexicographic increasing order.


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    list.append([i, j, k])
    print(list)

# Find the Runner-Up Score!

# https: // www.hackerrank.com/challenges/find-second-maximum-number-in-a-list


# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sorted = sorted(arr)
    index = int(n)-1
    for i in range(n):
        if sorted[index] == sorted[index-i]:
            a = sorted[(index-1)-i]
    print(a)


