from typing import List
class Solution:
    '''
    1. 이진트리를 이용해서 계산 -> 위치를 바꾸기 때문에 땡
    2. dynamic programming 을 이용하기
    
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1  ,  len(nums) ):
            val = 0
            if nums[i-1] > 0:
                val = nums[i-1]
            nums[i] = nums[i] + val
        return max(nums)


nums = [-2,1,-3,4,-1,2,1,-5,4]
s= Solution()
q = s.maxSubArray(nums)
print(q)