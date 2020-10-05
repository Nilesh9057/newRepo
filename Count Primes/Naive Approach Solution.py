import math
class Solution:
    def countPrimes(self, n: int) -> int:
        count=0
        def prime(num):
            p=int(math.pow(num,1/2))
            for i in range(2,p+1):
                if num%i==0:
                    return False
            return True
        
        if n==0 or n==1 or n==2:
            return 0
        else:
            if n>2:
                count+=1
            for j in range(3,n):
                if j%2!=0:
                    if prime(j):
                        count+=1
        
        return count