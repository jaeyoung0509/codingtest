
class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_SIZE= 2**31
        sign = []
        num = ''
        
        s= s.strip()
        if len(s) == 0:
            return 0


        #get sign 
        for idx ,val in enumerate(s):
            if val == '+':
                sign.append(1)
            elif val == '-':
                sign.append(-1)
            elif val.isnumeric():
                s = s[idx:]
                break
            else:
                break
        if len(sign) == 0:
            sign.append(1)

        #get numbers
        for i in s:
            if i.isnumeric():
                num += i
            else: 
                break

        if num== ''  or len(sign) >1:
            return 0

        result = int(num) * sign[-1]
        if result >= MAX_SIZE-1 :
            return MAX_SIZE - 1
        if result <= -1 * MAX_SIZE:
            return (MAX_SIZE * -1 ) 
        return result


sol = Solution()
print(sol.myAtoi("abc  def"))
