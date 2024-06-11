def prime_number_check(n):
    if n==1:
        return "Neither prime nor composite"
    count=0
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            count+=1
    if count>=2:
        return n,"Not a Prime number"
    else:
        return n,"Prime number"


print(prime_number_check(1001))

