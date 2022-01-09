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

# https://www.hackerrank.com/challenges/electronics-shop/

    def getMoneySpent(keyboards, drives, b):
        array = []
        for keyb in keyboards:
            for dri in drives:
                if dri+keyb<=b:
                    array.append(dri+keyb)

        array.sort()                

        if array:
            return array[len(array)-1]
        else:
            return -1   


    # https://www.hackerrank.com/challenges/cats-and-a-mouse

    def catAndMouse(x, y, z):
        if abs(y-z)>abs(x-z):
            return "Cat A"
        elif abs(x-z)>abs(y-z):
            return "Cat B"
        else:
            return "Mouse C"


    # https://www.hackerrank.com/challenges/magic-square-forming

    def formingMagicSquare(s):
        s = sum(s,[])

        magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1,       2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5,       7, 8, 1, 6], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]

        minimumcost = sys.maxsize

        for mag in magic:
            diff = 0
            for i,j in zip(s,mag):
                diff = diff+abs(i-j)
            minimumcost = min(minimumcost,diff)
        return minimumcost