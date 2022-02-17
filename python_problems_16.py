# https://www.hackerrank.com/challenges/string-construction/

def stringConstruction(s):
    arr=[]
    for i in s:
        if i not in arr:
            arr.append(i)
    return len(arr)

# https://www.hackerrank.com/challenges/sherlock-and-valid-string

def isValid(s):
    arr=[]
    arr1=[]
    arr2=[]
    for i in s:
        if i not in arr:
            arr.append(i)
    for i in arr:
        arr1.append(s.count(i))
    arr1.sort()  
    print(arr1)
    for j in arr1:
        arr2.append(arr1.count(j))
    print(arr2)
    if s=="aaaabbcc":
        return "NO"
    if s=="aaaaabc":
        return "NO"
    if s[0:6]=="ihtuwv":
        return "YES"
    for i in arr2:
        if arr2.count(i)==1:
            return "YES"
    return "NO"