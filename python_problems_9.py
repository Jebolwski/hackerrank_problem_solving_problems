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