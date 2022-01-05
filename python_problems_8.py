# https: // www.hackerrank.com/challenges/divisible-sum-pairs

def divisibleSumPairs(n, k, ar):

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[j]+ar[i]) % k == 0:
                count = count+1

    return count


# https: // www.hackerrank.com/challenges/day-of-the-programmer

def migratoryBirds(arr):
    array = []
    one_count = arr.count(1)
    two_count = arr.count(2)
    three_count = arr.count(3)
    four_count = arr.count(4)
    five_count = arr.count(5)

    array.append(one_count)
    array.append(two_count)
    array.append(three_count)
    array.append(four_count)
    array.append(five_count)

    if max(array) == one_count:
        return 1
    elif max(array) == two_count:
        return 2
    elif max(array) == three_count:
        return 3
    elif max(array) == four_count:
        return 4
    elif max(array) == five_count:
        return 5


        def dayOfProgrammer(year):

    if (1699 < year < 1918):
        if (year % 4 == 0):
            a = "12.09."+str(year)
            return a
        else:
            a = "13.09."+str(year)
            return a


# https: // www.hackerrank.com/challenges/day-of-the-programmer

    if (1917 < year < 1919):
        if (year % 4 == 0):
            a = "31.08."+str(year)
            return a
        else:
            a = "26.09."+str(year)
            return a

    if (1918 < year < 2701):
        if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
            a = "12.09."+str(year)
            return a
        else:
            a = "13.09."+str(year)
            return a
