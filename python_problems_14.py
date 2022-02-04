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

# https://codingbat.com/prob/p107863

def lucky_sum(a, b, c):
  array=[]
  array.append(a)
  array.append(b)
  array.append(c)
  sum=0
  for i in range(3):
    if array[i]==13:
      break
    else:  
      sum=sum+array[i]
    
  return sum

# https://codingbat.com/prob/p100347

def no_teen_sum(a, b, c):
  arr=[]
  arr.append(a)
  arr.append(b)
  arr.append(c)
  for i in range(3):
    if 19>=arr[i]>=13 and (arr[i]!=15 and arr[i]!=16):
      arr[i]=0
  return sum(arr)

# https://www.hackerrank.com/challenges/pangrams/

def pangrams(s):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    arr=[]
    count=0
    s=s.lower()
    for a in alphabet:
        arr.append(a)    
    for i in arr:
        if i in s:
            count=count+1
    if count>=26:
        print(count,"panagram")
        return "pangram"
    else:
        print(count,"not panagram")
        return "not pangram"

# https://codingbat.com/prob/p129125

def date_fashion(you, date):
  if you>=8 or date>=8:
    if you<=2 or date<=2:
      return 0
    else:
      return 2 
  elif (you<=8 and date<=8) and you>2 and date>2:
    return 1
  else:
    return 0

# https://codingbat.com/prob/p135815

def squirrel_play(temp, is_summer):
  if is_summer and 100>=temp>=60:
    return True
  elif 90>=temp>=60 and not is_summer:
    return True
  else:
    return False

# https://www.hackerrank.com/challenges/caesar-cipher-1

def caesarCipher(s, k):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a','b','c','d','e']
    result=''
    if k==26:
        return s
    for i in s:
        if i in alphabet:
            rng=alphabet.index(i)+k
            if rng>=len(alphabet):
                result+=str(i)
            a=alphabet[rng]
            result+=str(a)
        if i not in alphabet:
            result+=str(i)
    return result     

# https://codingbat.com/prob/p184853

def big_diff(nums):
  for i in range(len(nums)):
    for j in range(i):
      if nums[j]>nums[i]:
        nums[i],nums[j]=nums[j],nums[i]
  return nums[len(nums)-1]-nums[0]

# https://codingbat.com/prob/p108886

def sum67(nums):
  count=True
  sum=0
  
  for i in range(0,len(nums)):
    
    if nums[i]==6:
      count=False
    elif count==False and nums[i]==7:
      count=True
    elif count==True:
      sum=sum+nums[i]
      
  return sum