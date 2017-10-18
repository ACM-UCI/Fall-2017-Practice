# ACM @ UCI
# Week 1 Problem 7
# First Missing Positive (https://leetcode.com/problems/first-missing-positive/description/)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.append(0) #don't wanna worry about overflow/index+-1 stuff...
        # only 2 extra memory storage is needed (n and nums[-1]) for any value of nums, so O(1) space
        
        for a in range(n): #O(n)
            while nums[a]>0 and nums[a]<=n and nums[a] != a:
			# maximum n iterations but again special case as then the list would be ordered
			# would never go into this while loop at that point. Refer to previous problem to
			# find time complexity
                if nums[nums[a]] == nums[a]: #edge case if nums has duplicate values,no point in swapping
                    break
                nums[nums[a]],nums[a] = nums[a],nums[nums[a]] #swap
        for a in range(1,n+1):# check which one is out of place
            if a != nums[a]:
                return a
        return len(nums) #edge case if nums is ordered
		# O(n) time
		# O(1) space
