'''
Name: Sai Uday Bhaskar Mudivarty
Problem: https://leetcode.com/problems/shortest-word-distance/#/description
'''
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist, start, end = float("inf"), None, None
        for i,word in enumerate(words):
            if word == word1:
                start = i
            elif word == word2:
                end = i
                
            if start is not None and end is not None:
                dist = min(dist, abs(start - end))
        return dist
            