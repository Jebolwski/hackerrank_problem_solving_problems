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

# https://www.hackerrank.com/challenges/cavity-map

def cavityMap(grid):
    grid = [list(x) for x in grid]
    
    for i in range(1,n-1):
        for j in range(1,n-1):
            if grid[i][j]>grid[i][j+1] and grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i-1][j]:
                grid[i][j]="X"
    return ["".join(x) for x in grid]

# https://www.hackerrank.com/challenges/manasa-and-stones

def stones(n, a, b):
    array=set()
    top=max(b,a)*(n-1)
    for i in range(n):
        array.add(top)
        top=(top-abs(a-b))
    array=sorted(array)
    return (array)

# https://www.hackerrank.com/challenges/service-lane/

def serviceLane(n, cases,width):
    array=[]
    
    for i,j in cases:
        array.append(min(width[i:j+1]))
        
    return array

# https://www.hackerrank.com/challenges/lisa-workbook

def workbook(n, k, arr):
    result = 0
    page=1
    
    for problems in arr:
        for index in range(1,problems+1):
            if index==page:
                result=result+1
            if index==problems or index%k==0:
                page=page+1
                
    return result

# https://www.hackerrank.com/challenges/camelcase/

def camelcase(s):
    count=1
    for i in s:
        if i.isupper():
            count=count+1
    return count

# https://www.hackerrank.com/challenges/strong-password

def minimumNumber(n, password):
    
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    low_count=0
    up_count=0
    spe_count=0
    num_count=0
    
    for i in password:
        if i in lower_case:
            low_count=low_count+1
        if i in upper_case:
            up_count=up_count+1
        if i in special_characters:
            spe_count=spe_count+1
        if i in numbers:
            num_count=num_count+1
    print("low_count:",low_count,"up_count:",up_count,"spe_count:",                 spe_count,"num_count",num_count)
    
    
    minus=low_count+up_count+spe_count+num_count
    
    
    result=0
    if num_count<1:
        result=result+1
    if low_count<1:
        result=result+1
    if up_count<1:
        result=result+1
    if spe_count<1:
        result=result+1
        
        
    if n<6 and 6-n<n:
        print("1")
        if spe_count!=0:
            spe_count=1
        else:
            spe_count=0
            
            
        if low_count!=0:
            low_count=1
        else:
            low_count=0
            
            
        if num_count!=0:
            num_count=1
        else:
            num_count=0
            
            
        if up_count!=0:
            up_count=1
        else:
            up_count=0
        return 6-n+(spe_count+num_count+low_count+up_count)
    elif n>6:
        return result
    else:
        print("2")
        return 6-n
    