class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past={}
        for  i in nums:
            comp=target-nums[i]
            if comp in past:
                return [past[comp],i]
            else:
                past[nums[i]]=i
        return []
        