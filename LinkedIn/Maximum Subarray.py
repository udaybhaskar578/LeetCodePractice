'''
Name: Sai Uday Bhaskar Mudivarty
Problem: https://leetcode.com/problems/maximum-subarray/#/description
Reference: Geeks for geeks (http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        curr_max = nums[0]
        
        for i in xrange(1,len(nums)):
            curr_max = max(nums[i],curr_max+nums[i])
            max_so_far = max(curr_max,max_so_far)
        
        return max_so_far