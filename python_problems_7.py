# https: // www.hackerrank.com/challenges/between-two-sets

def getTotalX(a, b):
    multa = []
    multb = []
    final = []
    totallen = len(a+b)
    for i in range(1, 101):
        for aa in a:
            if i % aa == 0:
                multa.append(i)
        for bb in b:
            if bb % i == 0:
                multb.append(i)
        potential = multa+multb

    for number in potential:
        if potential.count(number) == totallen:
            final.append(number)
    return len(set(final))


# https: // www.hackerrank.com/challenges/breaking-best-and-worst-records


    def breakingRecords(scores):
    array = []
    highest = 0
    lowest = 0

    for score in scores:
        array.append(score)
    temp = array[0]
    for score in scores:
        if temp < score:
            temp = score
            highest = highest+1
    temp = array[0]
    for score in scores:
        if temp > score:
            temp = score
            lowest = lowest+1
    return highest, lowest


# https: // www.hackerrank.com/challenges/the-birthday-bar


    def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count = count+1
    return count
