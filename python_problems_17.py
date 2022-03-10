# https://www.hackerrank.com/challenges/word-order/


n = int(input().strip())
words=[]
count=[]
words_lite=[]

for i in range(n):
    word = input().strip()
    words.append(word)


for i in words:
    if i not in words_lite:
        words_lite.append(i)


for i in words_lite:
    count.append(words.count(i))


print(len(words_lite))
print(*count)

# https://www.hackerrank.com/challenges/py-collections-ordereddict

N = int(input())
items=[]
items_lite=[]
names=[]
names_lite=[]
prices=[]
prices_lite=[]
result=[]
for i in range(N):
    item = input().split()
    price = item[len(item)-1:len(item)]
    name = item[0:len(item)-1]
    items.append(item)
    prices.append(price)
    names.append(name)

for i in names:
    if i not in names_lite:
        names_lite.append(i)

for i in prices:
    if i not in prices_lite:
        prices_lite.append(i)

for i in items:
    if i not in items_lite:
        items_lite.append(i)

for i in items_lite:
    print(*i[:len(i)-1],int(i[len(i)-1])*items.count(i))

# https://www.hackerrank.com/challenges/compress-the-string

s = input()
count = 1
result=[]
i=0
while(i<len(s)-2):
    while(s[i]==s[i+1]):
        count = count + 1
        i=i+1
    result.append((count,int(s[i])))
    i=i+1
    count=1
if s[len(s)-2]==s[len(s)-1]:
    result.append((2,int(s[len(s)-1])))
else:
    result.append((1,int(s[len(s)-1])))
    result.append((1,int(s[len(s)-2])))
print(*result)

# https://www.hackerrank.com/challenges/capitalize

def solve(s):
    print(s.split())
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
    
# https://www.hackerrank.com/challenges/py-set-add/

array = []
num = input()
for i in range(int(num)):
    a = input()
    if a not in array:
        array.append(a)
print(len(array))

# https://www.hackerrank.com/challenges/text-wrap/

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

# https://www.hackerrank.com/challenges/exceptions/

a = input()
for i in range(int(a)):
    b = input()
    try:
        c, b = b.split()
        print(int(c)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as v:
        print("Error Code:",v)

# https://www.hackerrank.com/challenges/py-introduction-to-sets

def average(array):
    return sum(set(array))/len(set(array))

# https://www.hackerrank.com/challenges/symmetric-difference

m_val = input()
m = input()
n_val = input()
n = input()
arr=[]
arr1=[]
n = n.split()
m = m.split()

for i in n:
    if i in m:
        pass
    else:
        arr.append(i)
        
for i in m:
    if i in n:
        pass
    else:
        arr.append(i)
        
        
for i in range(len(arr)):
    arr[i] =int(arr[i])
    
arr.sort()
for i in arr:
    if i not in arr1:
        arr1.append(i)
for i in arr1:
    print(i)

# https://www.hackerrank.com/challenges/python-mod-divmod/

import math
sayi = input()
bolen = input()
print(math.floor(int(sayi)/int(bolen)))
print(int(sayi)%int(bolen))
print("("+str(math.floor(int(sayi)/int(bolen)))+",",str(int(sayi)%int(bolen))+")")

# https://www.hackerrank.com/challenges/python-power-mod-power/

a = input()
b = input()
m = input()

print(int(a)**int(b))
print(int(a)**int(b)%int(m))

# https://www.hackerrank.com/challenges/python-eval

a = input()
print(eval(a[6:len(a)-1]))

# https://www.hackerrank.com/challenges/no-idea

n = input()
m = input()
A = input()
B = input()

array=[]

for i in n:
    array.append(i)
    
for j in m:
    array.append(j)
    
while " " in array:
    array.remove(" ")
    

count=0
array = list(set(array))

for i in A:
    if i in array:
        count+=1

for j in B:
    if j in array:
        count-=1

print(count)

# https://www.hackerrank.com/challenges/maximize-it

K=input()
M=input()
N=input()
L=input()

arrayL=[]
arrayK=[]
arrayM=[]
arrayN=[]

for i in K.split():
    i = int(i)
    arrayK.append(i)
arrayK.sort()
k = arrayK[len(arrayK)-1]

for i in N.split():
    i = int(i)
    arrayN.append(i)
arrayN.sort()
n = arrayN[len(arrayN)-1]**2


for i in M.split():
    i = int(i)
    arrayM.append(i)
arrayM.sort()
m = arrayM[len(arrayM)-1]**2


for i in L.split():
    i=int(i)
    arrayL.append(i)
arrayL.sort()
l = arrayL[len(arrayL)-1]**2

print( m + n + l % k)

# https://www.hackerrank.com/challenges/py-set-intersection-operation/

nums = input()
a = input()
another =input()
b = input()
arr_a=[]
arr_b=[]
array=[]

for i in a.split():
    arr_a.append(i)


    
for i in b.split():
    arr_b.append(i)


for i in arr_a:
    if i in arr_b:
        array.append(i)
print(len(array))

# https://www.hackerrank.com/challenges/py-set-difference-operation/

N1 = int(input())
storage1 = set(input().split())

N2 = int(input())
storage2 = set(input().split())

storage3 = storage1.difference(storage2)

print(len(storage3))

# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation

a=input()
b=input()
c=input()
d=input()


b=set(b.split())
d=set(d.split())

print(len(b.symmetric_difference(d)))

# https://www.hackerrank.com/challenges/py-set-union/

a=input()
b=input()
c=input()
d=input()


b=set(b.split())
d=set(d.split())

print(len(b.union(d)))
    
    