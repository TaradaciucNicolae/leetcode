class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        
        string_x = str(x)
        reversed_string_x = string_x[::-1]

        #print(x, string_x)
        if reversed_string_x == string_x:
            return True
        else:
            return False
     
     
     
     
     
     
        # if x < 0:
        #     return False

        # original = x
        # reversed_num = 0

        # while x > 0:
        #     digit = x % 10 # grabbing the last digit

        #     reversed_num = reversed_num * 10 + digit # adding the last digit to the reversed number

        #     x //= 10 # Removing the last digit the we previously used

        # return original == reversed_num
