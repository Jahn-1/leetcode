class Solution:
    def maxSubArray(self, nums):
        maxCurr = maxGlobal = float('-inf')
                          
        for num in nums:
            # is the current number higher than the current number + running total?
            # if the current number is greater than the entire sum previous to it, 
            # we are starting from there.
            maxCurr = max(num, maxCurr + num)
            maxGlobal = max(maxCurr, maxGlobal)
        
        return maxGlobal
    
        # [-2,1,-3,4,-1,2,1,-5,4]
        # [-2] -> maxCurr   = max(-2, -inf + -2) = -2
        #      -> maxGloabl = max(-2, -inf)      = -2
        
        # [1]  -> maxCurr   = max(-2, -2 + 1)    = -1
        #      -> maxGlobal = max(-1, -2)        = -1
        
        # [-3]  -> maxCurr   = max(-1, -1 - 3)   = -1
        #      -> maxGlobal = max(-1, -1)        = -1
        
        # [4]  -> maxCurr   = max(4, -1 + 4)     = 4  
        #      -> maxGlobal = max(-1, 4)         = 4
        
        # in this iteration, maxCurr drops below maxglobal.
        # we keep this like this for the max sum of a CONTIGUOUS subarray of the array
        # [-1]  -> maxCurr   = max(-1, 4 + -1)   = 3 
        #       -> maxGlobal = max(3, 4)         = 4
        
        # [2]   -> maxCurr   = max(2, 3 + 2)     = 5
        #       -> maxGlobal = max(5, 4)         = 5