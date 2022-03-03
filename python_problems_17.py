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