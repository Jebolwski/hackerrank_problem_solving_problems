
# https://www.hackerrank.com/challenges/circular-array-rotation

def circularArrayRotation(a, k, queries,n):
    result = []
    k=k%n
    for q in queries:
        result.append(a[(n-k+q)%n])
    return result

# https://www.hackerrank.com/challenges/permutation-equation

def permutationEquation(p):
    result = []
    for i in range(1,len(p)+1):
        result.append(p.index(p.index(i)+1)+1)
    return result

# https://www.hackerrank.com/challenges/non-divisible-subset

def nonDivisibleSubset(k, s):
    # array = []
    # for i in range(len(s)):
    #     for j in range(i+1,len(s)):
    #         print("j :",j,"i :",i)
    #         array.append(array[i]+array[j])
    # array = list(set(array))
    # for i in array:
    #     if i%k==0 or k%i==0:
    #         array.remove(i)
    # return len(array)
    remainder = [0] * k
    for i in s:
        remainder[i%k]+=1
    
    maxnum = 0
    maxnum += min(remainder[0],1)
    
    if k%2==0:
        maxnum+=min(remainder[k//2],1)
        
    for i in range(1,k//2+1):
        if i!=k-i:
            maxnum+=max(remainder[i],remainder[k-i])
    
            
    return maxnum

# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/

def jumpingOnClouds(c, k):
    energy = 100
    i=0
    while True:
        if c[i]==1:
            energy=energy-3
        else:
            energy=energy-1
        i = (i+k)%n
        if i==0:
            break
    return energy
    
    # for i in range(len(c)):
    #     if i+k<len(c):
    #         a=c[i+k]
    #     if a==1:
    #         energy=energy-3
    #     else:
    #         energy=energy-1 
    # if a==c[0]:
    #     return energy

# https://www.hackerrank.com/challenges/find-digits

def findDigits(n):
    n=str(n)
    count=0
    for i in n:
        print(i)
        if int(i)!=0:
            if int(n)%int(i)==0:
                count=count+1
    return count


# https://www.hackerrank.com/challenges/append-and-delete/

def appendAndDelete(s, t, k):
    count=0
    
    for i,j in zip(s,t):
        if i==j:
            count=count+1
        else:
            break
        
    t_len = len(s)+len(t)
        
    if t_len<=2*count+k and t_len%2==k%2 or t_len<k:
        return "Yes"
    else:
        return "No"

# https://www.hackerrank.com/challenges/sherlock-and-squares

def squares(a, b):
    count=0
    for i in range(a,b+1):
        if math.sqrt(i)%1==0:
            count=count+1
    return count
    
    
    # if s==t:
    #     return "Yes"
    # else:
    #     array = []
    #     for i in range(len(s)):
    #         array.append(s[i])
    #     for i in range(len(t)):
    #         array.append(t[i])
    #     a=0
    #     while array[a]==array[len(t)+1+a]:
    #         if len(t)+1+a==len(array):
    #             break
    #         array.remove(array[a]) 
    #         array.remove(array[len(t)+1+a]) 
    #         a=a+1
    #         print(array)
    #     if len(array)<=k:
    #         return "Yes"
    #     else:
    #         return "No"

# https://www.hackerrank.com/challenges/extra-long-factorials/

def extraLongFactorials(n):
    result=1
    i=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            result = result*i
            i=i+1
        print(result)

# https://www.hackerrank.com/challenges/library-fine

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1<=y2 and m1<m2:
        return "0"
    elif y1<y2:
        return "0"
    elif d1<=d2 and (m1==m2 or m1<m2) and (y1==y2):
        return "0"
    elif d1>d2 and m1==m2 and y1==y2:
        return abs(d2-d1)*15
    elif m1>m2 and y1==y2:
        return abs(m1-m2)*500
    elif y1>y2:
        return 10000

# https://www.hackerrank.com/challenges/repeated-string

def repeatedString(s, n):
    count=0
    if len(s)==1 and s=="a":
        return n
    else:
        while len(s)<n:
            s=s+s
        array=[]
        for i in range(len(s)):
            array.append(s[i])    
        while len(array)>n:
            array.pop()
        print(s)
        for i in range(len(array)):
            if array[i]=="a":
                count=count+1
        return count

# https://www.hackerrank.com/challenges/equality-in-a-array

def equalizeArray(arr):
    c = Counter(arr)
    return len(arr)-max(c.values())

# https://www.hackerrank.com/challenges/taum-and-bday

def taumBday(b, w, bc, wc, z):
    return min(w*wc+b*bc,wc*(w+b)+b*z,bc*(b+w)+w*z)