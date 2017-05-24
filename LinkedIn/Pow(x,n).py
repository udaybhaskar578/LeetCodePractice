'''
Name: Sai Uday Bhaskar Mudivarty
Problem: https://leetcode.com/problems/powx-n/#/description
Reference: https://github.com/criszhou/LeetCode-Python/blob/master/050.%20Pow(x%2C%20n).py
Initial thoughts were to use x**n
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0:
            return 0
        if n==0:
            return 1
        if n<0:
            x = 1.0 / x
            n = -n
        if n==1:
            return x
        if n%2==1:
            return x * self.myPow(x**2, n//2)
        else:
            return self.myPow(x**2, n//2)