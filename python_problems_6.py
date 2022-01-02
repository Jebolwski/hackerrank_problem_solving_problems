# https: // www.hackerrank.com/challenges/apple-and-orange/

def countApplesAndOranges(s, t, a, b, apples, oranges):
    countapples = 0
    countoranges = 0
    newapple = 0
    neworange = 0
    newapples = []
    neworanges = []
    for apple in apples:
        newapple = a+apple
        newapples.append(newapple)
    for orange in oranges:
        neworange = b+orange
        neworanges.append(neworange)
    for apple in newapples:
        if s <= apple <= t:
            countapples = countapples+1
    print(countapples)
    for orange in neworanges:
        if s <= orange <= t:
            countoranges = countoranges+1
    print(countoranges)
