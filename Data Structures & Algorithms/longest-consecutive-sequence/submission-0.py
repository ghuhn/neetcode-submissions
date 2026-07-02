class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter=1
        nums_arr=list(set(sorted(nums)))
        for i in range(len(nums_arr)-1):
            if nums_arr[i]+1==nums_arr[i+1]:
                counter+=1
                i=nums_arr.index(nums_arr[i]+1)
            else:
                i+=1
        return counter

        