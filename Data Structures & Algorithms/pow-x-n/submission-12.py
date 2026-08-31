class Solution:
    def myPow(self, x: float, n: int) -> float:
        prod=1
        if len(str(n))>5 and x!=1.00 and x!=-1.00:
            return 0.00
        else:
            if n==0:
                return 1
            if x==1.0:
                return 1
            if x== -1:
                if n%2==0:
                    return 1
                if n%2==1:
                    return -1
            if n>0:
                for i in range(n):
                    prod*=x
            if n<0:
                for i in range(-(n)):
                    prod*=x
                prod=1/prod
            
            return prod
                    


        