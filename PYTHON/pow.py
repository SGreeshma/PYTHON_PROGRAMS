def myPow(x, n):
    if(n==0):
        return 1
    if(n%2==1):
        return x*myPow(x, n-1)
    return myPow(x*x, n//2)
def getPow(x, n):
    if(n>=0):
        return myPow(x, n)
    return 1/myPow(x, -n)
x=2
n=6
print(myPow(x, n))

# method-2 : power sum in a optimal way
class Solution(object):
    def power(self, x, n):
        if(n==0): #base condition
            return 1
        if(n%2==1): #checking whether its even or odd
            return x*self.power(x, n-1) #x*x**n-1
        return self.power(x*x, n//2) #x*x**n//2
    def myPow(self, x, n):
        if(n<0):
            x=1/x
        n=abs(n) # to make n value +ve
        return self.power(x, n)        