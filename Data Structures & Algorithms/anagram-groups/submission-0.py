from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            sorted_key = "".join(sorted(s))
            ans[sorted_key].append(s)
        
        return list(ans.values())