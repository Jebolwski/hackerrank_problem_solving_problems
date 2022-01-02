# https: // www.hackerrank.com/challenges/apple-and-orange/

# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     countapples = 0
#     countoranges = 0
#     newapple = 0
#     neworange = 0
#     newapples = []
#     neworanges = []
#     for apple in apples:
#         newapple = a+apple
#         newapples.append(newapple)
#     for orange in oranges:
#         neworange = b+orange
#         neworanges.append(neworange)
#     for apple in newapples:
#         if s <= apple <= t:
#             countapples = countapples+1
#     print(countapples)
#     for orange in neworanges:
#         if s <= orange <= t:
#             countoranges = countoranges+1
#     print(countoranges)

s = "8hypotheticall0mm24y6wxz"


def missingCharacters(s):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    englet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    sarray = []
    for ss in s:
        return ss
        sarray.append(ss)
    # for engletter in englet:
    #     for letters in sarray:
    #         if str(engletter) == str(letters):
    #             englet.remove(engletter)
    for number in numbers:
        for letters in sarray:
            if str(number) == str(letters):
                numbers.remove(number)
    return sarray


missingCharacters(s)
