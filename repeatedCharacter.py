class Solution:
    def repeatedCharacter(self, s: str) -> str:
        string_length=len(s)
        my_hash = {}

        for i in range(string_length): 
            if s[i] in my_hash: 
                return s[i]
            else: 
               my_hash[s[i]] = True 


        
