# stri="hello"

# print(stri.split("l"))


# word = 'geeks, for, geeks'
  
# # Splits at ','
# print(word.split(','))

# word = 'CatBatSatFatOr'
  
# # Splitting at t
# print(word[len(word)-3:])


a="AliMerb"

for i in a:
    print(i.isupper())


def make_bricks(small,big,goal):
    array=[]
    for s in range(1,small+1):
        for b in range(1,big+1):
            if b*5+s==goal:
                array.append(True)
    for i in array:
        if i==False:
            array.remove(i)
    if len(array)>0:
        print(True)
    else:
        print(False)

make_bricks(3, 1, 8)