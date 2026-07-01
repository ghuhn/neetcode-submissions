class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict={}
        output=[]
        for i in nums:
            if i in freq_dict:
                freq_dict[i]+=1
            else:
                freq_dict[i]=1
        return list(freq_dict.keys())[:-3:-1]
        

        