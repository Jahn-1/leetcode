class Solution:
    def productExceptSelf(self, nums):
        left = []
        leftNum = 1
        for i, num in enumerate(nums):
            left.append(leftNum)
            leftNum *= num
            
        right = []
        rightNum = 1
        for i, num in enumerate((nums)[::-1]):
            right.append(rightNum)
            rightNum *= num
        
        right = right[::-1]
        
        ans = []
        for i in range(len(left)):
            ans.append(right[i] * left[i])
            
            
        return ans
    