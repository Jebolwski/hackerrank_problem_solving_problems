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