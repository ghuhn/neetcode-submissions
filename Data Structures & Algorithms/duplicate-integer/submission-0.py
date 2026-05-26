class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            sample=nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==sample:
                    return True
        return False
                
                
        