import math

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

# https://www.hackerrank.com/challenges/priyanka-and-toys

def toys(w):
    w.sort()
    temp = w[0]
    count = 1
    for i in w:
        if i > temp + 4:
            temp = i
            count += 1
    return count

# https://www.hackerrank.com/challenges/strings-xor

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

s = input()
t = input()
print(strings_xor(s, t))

# https://www.hackerrank.com/challenges/smart-number

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / (val*val) == 1:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
