# https://www.hackerrank.com/challenges/encryption/

def encryption(s):
    n = len(s)
    r = floor(sqrt(n))
    c = ceil(sqrt(n))
    result = []
    
    for i in range(c):
        temp=[]
        j=0
        while i+j<n:
            temp.append(s[i+j])
            j=j+c
        result.append("".join(temp))
        
    return " ".join(result)

# https://www.hackerrank.com/challenges/beautiful-triplets

def beautifulTriplets(d, arr):
    count=0
    m=Counter(arr)
    for num in arr:
        if m[num+d] and m[num+d+d]:
            count=count+1
    return count

# https://www.hackerrank.com/challenges/minimum-distances

def minimumDistances(a):
    array=[]
    array1=[]
    for i in range(len(a)):
        mini=a[i]
        for j in range(len(a)):
            if a[j]==a[i]:
                array.append(abs(i-j))
    array.sort()
    for item in array:
        if item not in array1:
            array1.append(item)
    if len(array1)==1:
        return "-1"
    else:
        return array1[1]

# https://www.hackerrank.com/challenges/climbing-the-leaderboard

def climbingLeaderboard(ranked, player):
    ranked=list(set(ranked))
    ranked.sort()
    n=len(ranked)
    i=0
    result=[]
    
    for alscore in player:
        while n>i and alscore>=ranked[i]:
            i=i+1
        result.append(n-i+1)
    return result

# https://www.hackerrank.com/challenges/jumping-on-the-clouds

def jumpingOnClouds(c):
    i=0
    jump=0
    while i<len(c)-1:
        if i+2==len(c) or c[i+2]==1:
            jump=jump+1
            i=i+1
        else:
            jump=jump+1
            i=i+2
    return jump

# https://www.hackerrank.com/challenges/kaprekar-numbers

def kaprekarNumbers(n, d):
    a=0
    array=[]
    for i in range(1,d+1):
        if i*i<d:
            isq=int(i)**2
            isq=str(isq)
            print(isq,isq[len(isq)-n])
            if isq[:len(isq)-n]+isq[len(isq)-n:]==i:
                array.append(isq)                
    print(array)

# https://www.hackerrank.com/challenges/halloween-sale    

def howManyGames(p, d, m, s):
    res = 0

    while s > 0:
        res += 1
        s -= p
        p = max(p - d, m)

    if s != 0:
        res -= 1

    return res

# https://www.hackerrank.com/challenges/insertionsort1

def insertionSort1(n, arr):
    key =arr[-1]
    i=n-1
    while i>0 and arr[i-1]>key:
        arr[i]=arr[i-1]
        print(*arr)
        i=i-1
    arr[i]=key
    print(*arr)