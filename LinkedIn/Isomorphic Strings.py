'''
Name: Sai Uday Bhaskar Mudivarty
Problem: https://leetcode.com/problems/isomorphic-strings/#/description
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            return self.checkIsoMorphic(t,s) and self.checkIsoMorphic(s,t)
                 
    def checkIsoMorphic(self,s,t):
        res = {}
        for i,letter in enumerate(s):
            if letter not in res:
                res[letter] = t[i]
            elif res[letter] != t[i]:
                return False
        return True
                    