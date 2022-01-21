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

        