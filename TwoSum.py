class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        n= len(nums)

        for i in range(n): 
            diff= target-nums[i]
            if diff in my_hash: 
                return [my_hash[diff], i]
            my_hash[nums[i]] =i 
        return[]

        
