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


def staircase(n):
    for i in range(n):
        for j in range(n-1-i, 0, -1):
            print(" ", end="")
        for k in range(0, i+1):
            print("#", end="")
        print("")
