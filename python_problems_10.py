# https://www.hackerrank.com/challenges/electronics-shop

def getMoneySpent(keyboards, drives, b):
    array = []
    for i in keyboards:
        for j in drives:
            if j+i<=b:
                array.append(j+i)
                array.sort()
                res = array[len(array)-1]

    if array:
        return res 
    else:
        return -1     