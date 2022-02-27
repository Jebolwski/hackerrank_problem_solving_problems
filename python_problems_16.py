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

# https://www.hackerrank.com/challenges/alternating-characters
    
def alternatingCharacters(s):
    count=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count=count+1
    return count

# https://www.hackerrank.com/challenges/icecream-parlor

def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]+arr[i]==m:
                return i+1,j+1

# https://www.hackerrank.com/challenges/marcs-cakewalk

def marcsCakewalk(calorie):
    total=0
    calorie.sort()
    calorie.reverse()
    for i in range(len(calorie)):
        print("2^",i,"*",calorie[i])
        total+=(int(math.pow(2,i)))*calorie[i] 
        print((2^i)*calorie[i],total)
    return total   

# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/

def minimumAbsoluteDifference(arr):
    array = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            array.append(abs(arr[i]-arr[j]))
    array.sort()
    i = 0
    while array[i]==0:
        i+=1
    return array[i+1]

# https://www.hackerrank.com/challenges/correctness-invariant

def insertion_sort(l):
    for i in range(len(l)):
        for j in range(i):
            if l[j]>l[i]:
                l[j],l[i]=l[i],l[j]

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))

# https://www.hackerrank.com/challenges/missing-numbers/

def missingNumbers(arr, brr):
    result=[]
    result1=[]
    for i in brr:
        if i in arr and arr.count(i)==brr.count(i):
            pass
        else:
            result.append(i)
            
    for i in result:
        if i not in result1:
            result1.append(i)
            
    result1.sort()
    return result1

# https://www.hackerrank.com/challenges/two-strings

def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return "YES"
        return "NO"

# https://www.hackerrank.com/challenges/richie-rich

def highestValuePalindrome(s, n, k):
    array=[]
    if len(s)==1:
        return "9"
    for i in s:
        array.append(i)
    count=0
    if len(s)%2==1:
        a=int(math.floor(len(s)/2))
    else:
        a=int(len(s)/2)
    for i in range(a):
        if array[i]==array[len(s)-i-1]:
            pass
        else:
            count+=1
            array[len(s)-i-1]="9"
            array[i]="9"
    if count>k:
        return "-1"
    for i in range(a):
        if array[i]==array[len(s)-i-1] and array[i]!=9:
            count+=1
            array[i]="9"
            array[len(s)-i-1]="9"
            print(array,count,k)
            if count>=k:
                break
            
            
    arr=""     
    for i in array:
        arr+=i   
    return arr

# https://www.hackerrank.com/challenges/strange-code/

def strangeCounter(t):
    array = []
    num=3
    temp=num
    while(len(array)<1500):
        for i in range(num,0,-1):
            array.append(num)
            num=num-1
        num=temp*2
        temp=temp*2
    return array[t-1]

# https://www.hackerrank.com/challenges/chocolate-feast

def chocolateFeast(n, c, m):
    total = int(n/c);
    
    empty_wrapper = total
    
    while empty_wrapper >= m:
        
        temp = int(empty_wrapper/m)
    
        total = total + temp
        
        empty_wrapper = empty_wrapper - (temp*m) + temp

    return total


# https://www.hackerrank.com/challenges/flatland-space-stations/

def flatlandSpaceStations(n, c):
    
    array=[]
    array1=[]
    array2=[]
    for i in range(n):
        array.append(i)
    for i in c:
        for j in array:
            if j in c:
                array1.append(0)
            else:
                for a in range(len(c)):
                    array2.append(abs(c[a]-j))
                array1.append(min(array2))
                array2=[]
                
                
    return max(array1)

# https://codingbat.com/prob/p189616

def count_evens(nums):
  count=0
  for i in nums:
    if i%2==0:
      count=count+1
  return count

# https://www.hackerrank.com/challenges/find-a-string/

def count_substring(string, sub_string):
    count=0
    
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            count=count+1
    return count

# https://www.hackerrank.com/challenges/string-validators

def isalnum(s):
    count_number=0
    count_letter=0
    nums=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(s)):
        if s[i] in nums:
            count_number=count_letter+1
        else:
            count_letter=count_letter+1
    if count_number>0 and count_letter>0:
        return "True"
    return "False"
def isalpha(s):
    count=0
    nums=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(s)):
        if s[i] in nums:
            return "False"
        else:
            if s[i]<s[i+1]:
                count=count+1
    if count==len(s):
        return "True"
    return "False"
def isdigit(s):
    count=0
    nums=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(s)):
        if i not in nums:
            count=count+1
    if count>0:
        return "True"
    return "False"
def islower(s):
    count=0
    for i in s:
        if i.lower()==i:
            count=count+1
    if count==len(s):
        return "True"
    return "False"
def isupper(s):
    count=0
    for i in s:
        if i.upper()==i:
            count=count+1
    if count==len(s):
        return "True"
    return "False"

print(isalnum(s))
print(isalpha(s))
print(isdigit(s))
print(islower(s))
print(isupper(s))

# https://www.hackerrank.com/challenges/merge-the-tools

def merge_the_tools(string, k):
    array = []
    array1 = []
    for i in range(0,len(string),k):
        array.append(string[i:i+k])
        
    for i in range(int(len(string)/k)):
        array1.append([])
        
    for i in range(int(len(string)/k)):
        for j in array[i]:
            if j not in array1[i]:
                array1[i].append(j)
    string=""
    for i in array1:
        for j in range(int(len(string)/k)):
            
            print(i[0:2])