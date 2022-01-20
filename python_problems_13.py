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
        