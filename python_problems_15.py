# https://codingbat.com/prob/p170842

def double_char(str):
  stra=''
  for i in str:
      stra=stra+i
      stra=stra+i
  return stra

# https://codingbat.com/prob/p167246

def count_hi(str):
  count=0
  array=[]
  for i in range(len(str)-1):
    if str[i]=='h' and str[i+1]=='i':
      count=count+1
  return count

# https://codingbat.com/prob/p164876

def cat_dog(str):
  dog_count=0
  cat_count=0
  
  
  for i in range(len(str)-2):
    if str[i:i+3]=='dog':
      dog_count=dog_count+1
      
    if str[i:i+3]=='cat':
      cat_count=cat_count+1 

  return dog_count==cat_count  

# https://codingbat.com/prob/p119308

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i]==2 and nums[i+1]==2:
      return True
  return False

# https://codingbat.com/prob/p189616

def count_evens(nums):
  count=0
  for i in nums:
    if i%2==0:
      count=count+1
  return count


# https://codingbat.com/prob/p174314


def end_other(a, b):
  a=a.lower()
  b=b.lower()


  if a in b[len(b)-len(a):] or b in a[len(a)-len(b):]:
    return True
  return False

# https://codingbat.com/prob/p149391

def xyz_there(str):
  for i in range(len(str)-2):
    if str[i:i+3]=="xyz" and str[i-1]!=".":
      return True
  return False

# https://codingbat.com/prob/p179960

def make_chocolate(small, big, goal):
  biggie=1
  if small+big*5<goal:
    return -1
  
  if big*5<=goal:
    return goal-big*5
    
  while biggie*5<=goal:
    biggie+=1
  if goal-5*(biggie-1)<=small:
    return goal-5*(biggie-1)
  else:
    return -1

# https://codingbat.com/prob/p179960

def round10(num):
  if num%10>=5:
    return 10-num%10+num
  else:
    return num-num%10
    
    
def round_sum(a, b, c):
  return round10(a)+round10(b)+round10(c)

# https://codingbat.com/prob/p160533

def close_far(a, b, c):
  if abs(abs(b)-abs(c))<=1 or abs(abs(a)-abs(c))<=1:
    if a+b+c==8 or a+b+c==9 or a+b+c==23:
      return True
    return False
  else:
    return True
    
# https://www.hackerrank.com/challenges/beautiful-binary-string

  def beautifulBinaryString(b):
    count=0
    b=str(b)
    i=0
    while i<len(b):
        if b[i:i+3]=="010":
            count=count+1
            i=i+3
        else:
            i=i+1
    return count