class Solution:
    def containsDuplicateBrute(self, nums):
        # brute force
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if (idx1 != idx2 and num1 == num2):
                    return True
        
        return False
      
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))