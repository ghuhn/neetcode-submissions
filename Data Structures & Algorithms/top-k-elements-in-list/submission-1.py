class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=sorted(nums)
        freq_dict={}
        for i in nums:
            if i in freq_dict:
                freq_dict[i]+=1
            else:
                freq_dict[i]=1
        freq_list=list(sorted(freq_dict.items()))[-1:-k-1:-1]
        final=[]
        for item in freq_list:
            final.append(item[0])
        return final
        

        