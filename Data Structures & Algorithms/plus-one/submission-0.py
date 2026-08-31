class Solution:
    import math
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        num=0
        digi=0
        output=[]
        for i in range(0,len(digits)):
            num+=math.pow(10,i)*digits[i]
        plus_one=int(num)+1
        while plus_one:
            digi=plus_one%10
            plus_one=plus_one//10
            output.append(digi)
        return output[::-1]

            

        