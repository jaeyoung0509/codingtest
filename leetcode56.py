from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        1 4 4 5
        1 3 2 6
        1 4 1 5  
        for solving this problem ,
        1 )  sort  by  first value
        2 )   
        result = [intervals[0]]
        intervals = intervals[1:]
        and keep comapring result.end <->  interval.start   which is more big
        😣 caution 
        for avoid , index range error  Use python slice (-1) 
        '''
        if len(intervals) == 1 : 
            return intervals
        
        intervals.sort()
        result = [intervals[0]]
        for idx ,  interval in  enumerate(intervals[1:]) :
            if (result[-1] == interval):
                continue
            elif result[-1][1] >=  interval[0]:
                result[-1] =  [result[-1][0]  , max(result[-1][1] ,  interval[1])]
            else:
                result.append(interval)
        return result 
            
                
s = Solution()
intervals = [[1,4],[0,2],[3,5]]
t = s.merge(intervals)
print(t)