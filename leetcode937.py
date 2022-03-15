from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        result = []
        for idx , log in enumerate(logs):
            tmp = log.split()
            if tmp[1].isnumeric() == False:
                letters.append([idx , tmp])
            else:
                digits.append([idx , tmp])
        letters.sort(key=lambda x:x[1][0])
        letters.sort(key = lambda x : x[1][1:])
        for letter in letters:
            result.append(logs[letter[0]])
        for digit in digits:
            result.append(logs[digit[0]])
        return result       
        
s = Solution()
print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]))
#print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print(1)