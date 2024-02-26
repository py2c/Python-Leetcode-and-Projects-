class Solution:
    def reverse(self, x: int) -> int:        
        
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        sign =1 if x >=0 else -1
        x= abs(x)

        reversed_num = 0
        while x !=0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            if reversed_num >INT_MAX:
               return 0
            x //=10


        reversed_num *= sign

        if reversed_num <INT_MIN:
           return 0


        return reversed_num          
