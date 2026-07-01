class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict={}
        for string in strs:
            sorted_str="".join(sorted(string))
            if sorted_str not in string_dict:                
                string_dict[sorted_str]=[string]
            else:
                string_dict[sorted_str].append(string)
        return list(string_dict.values())
              