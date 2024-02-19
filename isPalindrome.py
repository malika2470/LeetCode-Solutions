class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0: 
            return False
        stri_x=str(x)
        left_point=0
        right_point= len(stri_x)-1

        while (left_point < right_point): 
            if not (stri_x[left_point] == stri_x[right_point]): 
                return False
            left_point +=1
            right_point-=1
        return True
