'''
Name: Sai Uday Bhaskar Mudivarty
Problem: https://leetcode.com/problems/valid-perfect-square/#/description

'''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        else:
            start,end = 1,num
            while start <= end:
                mid = start + (end - start)/2
                sqrrt = mid * mid
                if sqrrt == num:
                    return True
                if sqrrt < num:
                    start = mid+1
                else:
                    end = mid-1
        return False