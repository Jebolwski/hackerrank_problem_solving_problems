# https://www.hackerrank.com/challenges/funny-string/

def funnyString(s):
    
    array=[]
    array_diff=[]
    reverse_array=[]
    reverse_array_diff=[]
    for i in range(len(s)):
        array.append(ord(s[i]))
    for i in range(len(array)):
        array_diff.append(abs(array[i]-array[i-1]))    
        
    for i in range(len(s)-1,-1,-1):
        reverse_array.append(ord(s[i]))
    for i in range(len(reverse_array)):
        reverse_array_diff.append(abs(reverse_array[i]-reverse_array[i-1]))
    if reverse_array_diff==array_diff:
        return "Funny"
    else:
        return "Not Funny"

# https://www.hackerrank.com/challenges/gem-stones

def gemstones(arr):
    result =set(arr[0])
    
    for i in range(1,n):
        temp=set(arr[i])
        
        result = result.intersection(temp)
    return len(result)  

# https://www.hackerrank.com/challenges/mars-exploration

def marsExploration(s):
    help="SOS"
    count=0
    for i in range(0,len(s),3):
        if s[i:i+3][0]!="S":
            count=count+1
        if s[i:i+3][1]!="O":
            count=count+1
        if s[i:i+3][2]!="S":
            count=count+1

# https://www.hackerrank.com/challenges/hackerrank-in-a-string/

def hackerrankInString(s):
    i=0
    target="hackerrank"
    for char in s:
        if target[i]==char:
            i+=1
            
            
            if i==len(target):
                return "YES"
    
    return "NO"