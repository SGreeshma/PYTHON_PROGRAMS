# SEIVE OF EROTOSTHENESIS

#time complexity : O(N**2)
def isPrime(num):
    c=0
    for i in range(1, n+1):
        if(num%i==0):
            c+=1
    return c==2
n=int(input())
count=0
for num in range(2, n):
    if(isPrime(num)):
        count+=1
print(count)