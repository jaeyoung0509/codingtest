from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort(key=len) 
        target = strs[0]
        strs = strs[1:]
        for idx ,val in enumerate(target):
            for other in strs:
                print( val , other , other[idx])
                if other[idx] != val:
                    return target[:idx]
        return target

strs = ["flower","flow","flight"]
l = Solution().longestCommonPrefix(strs)
print(l)