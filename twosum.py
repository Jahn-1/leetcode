class Solution:
    # Brute Force. O(n^2)
    def twoSumBruteForce(self, nums, target):
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if (idx1 == idx2):
                    continue
                elif (num1 + num2 == target):
                    return [idx1, idx2]
                  
	# Optimized. O(n)
    def twoSum(self, nums, target): 
        numsDict = {}
        for idx, num in enumerate(nums):
            numsDict[num] = idx # the last index of a particular number so that duplicate numbers still work.
		
      	for idx, num in enumerate(nums):
            if (target - num in numsDict and numsDict[target-num] != idx):
                return [idx, numsDict[target-num]]
		
                    