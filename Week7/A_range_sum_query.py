class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.DP = [0] #DP[i] stores "prefix sum" up to i.  This means the sum of all elements of the array up to i.
        for x in nums:
            self.DP.append(x + self.DP[-1])
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.DP[j+1] - self.DP[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)