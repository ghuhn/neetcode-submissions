class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past={}
        for  i in range(len(nums)):
            comp=target-nums[i]
            if comp in past:
                return [i,past[comp]]
            else:
                past[nums[i]]=i
        return []
        