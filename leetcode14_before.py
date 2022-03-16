class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort(key=len) 
        target = strs[0]
        strs = strs[1:]
        s = 0
        for i in range(len(strs)):
            q = len([x for x in strs if x[i]==target[i]])
            if q > s:
                s = q
        if s == 0:
            return ''
        return target[:s]