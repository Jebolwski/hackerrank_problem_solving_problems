# https: // www.hackerrank.com/challenges/divisible-sum-pairs

def divisibleSumPairs(n, k, ar):

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[j]+ar[i]) % k == 0:
                count = count+1

    return count
