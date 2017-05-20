'''
Name: Sai Uday Bhaskar Mudivarty
Problem: https://leetcode.com/problems/nested-list-weight-sum/#/description
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # Uses Level order traversal technique and a queue
        if len(nestedList) == 0: return 0
        queue = []
        result = 0
        for n in nestedList:
            # append List with associating it with its depth
            queue.append((n, 1))
        while queue:
            #pop the next item in stack and its depth information
            next, depth = queue.pop(0)
            if next.isInteger():
               result += depth * next.getInteger()
            else:
                for i in next.getList():
                    queue.append((i,depth+1))
        return result
        
        
'''
Recursive Solution: Refer https://github.com/kamyu104/LeetCode/blob/master/Python/nested-list-weight-sum.py
    def depthSumHelper(nestedList, depth):
        res = 0
        for l in nestedList:
            if l.isInteger():
                res += l.getInteger() * depth
            else:
                res += depthSumHelper(l.getList(), depth + 1)
        return res
    return depthSumHelper(nestedList, 1)
'''