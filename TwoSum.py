'''
Author: Sai Uday Bhaskar Mudivarty
Question: https://leetcode.com/problems/two-sum/
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
           complement = target - nums[i]
           indexofc = nums.index(complement)
           if indexofc != -1:
               if indexofc != i:
                   result.append(i)
                   result.append(indexofc)
                   break
        return result
        