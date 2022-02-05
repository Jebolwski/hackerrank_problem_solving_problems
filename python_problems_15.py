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