# ACM @ UCI
# Week 1 Problem 6
# Longest Consecutive Sequence (https://leetcode.com/problems/longest-consecutive-sequence/description/)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = set(nums)
		# creates hashset in python. hashset has O(1) time to see if element exists
		# hashset takes O(n) space as n amounts of storage needs to be allocated
        consec_count = 0
        for num in nums:# O(n) iterations 
            if num-1 not in lookup:
                tmp_count = 1
                while num+1 in lookup:
				# maximum O(n) iterations, but special case: if n operations taken then for all other elements, O(1) operations
				# O(n+const_1+const_2+const_3 ... + const_n) -> ~O(n + const*n) -> O(2*(const+1)*n) -> ~O(n) * as n->inf
				# ^const^ is integer depending on operations I do in each iteration of for loop without while loop, it'd be ~10 in this case
                    tmp_count+=1
                    num+=1
                consec_count = max(consec_count,tmp_count)
        return consec_count
		# O(n) time and space
