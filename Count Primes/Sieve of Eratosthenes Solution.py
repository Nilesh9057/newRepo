class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        count=0
        l=[1 for i in range(0,n)]
        l[0]=l[1]=0
        for i in range(2,n):
            if l[i]==1:
                j=2
                while i*j<n:
                    l[i*j]=0
                    j+=1
        return l.count(1)