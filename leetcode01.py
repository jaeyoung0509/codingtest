from typing import List
class Solution:
    '''
    (Time Complexity) : O(n**2)
    (Space Complexity) : O(1)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in  range(len(nums) -1 ):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]

class Solution:
    '''
    (Time Complexity) : O(n)
    (Space Complexity) : O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx ,val in enumerate(nums):
            m = target - val
            if m in hash :
                return [hash[m] , idx]
            else:
                hash[val] = idx            
        ...
        