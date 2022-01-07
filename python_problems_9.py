# https://www.hackerrank.com/challenges/bon-appetit/

def bonAppetit(bill, k, b):
    bill.pop(k)
    new_bill=sum(bill)/2
    
    if b-new_bill==0:
        print("Bon Appetit")
    else:
        print(int(b-new_bill))

# https://www.hackerrank.com/challenges/sock-merchant

        def sockMerchant(n, ar):
    s = 0
    for a in Counter(ar).values():
        s=s+int(a)//2
    return s

# https://www.hackerrank.com/challenges/drawing-book
    
    for i in range(n):
        if i*2==p or i*2==p-1:
            from_zero = i
    for i in range(n):
        if n-p!=1:
            if n-i*2==p or n-i*2==p+1:
                from_n = i
        else:
            if n%2!=0 and p%2==0:
                return 0
            elif n==2 and p==1:
                return 0
            else:
                return 1
    result = min(from_n,from_zero)
    return result

# https://www.hackerrank.com/challenges/counting-valleys

    def countingValleys(steps, path):
    count=0
    level=0
    result=0
    for i in path:
        if i=="U":
            count=count+1
        else:
            count=count-1
        if count==0 and i=="U":
            result=result+1
    return result