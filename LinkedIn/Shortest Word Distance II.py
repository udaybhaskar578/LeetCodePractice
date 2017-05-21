'''
Name: Sai Uday Bhaskar Mudivarty
Problem: https://leetcode.com/problems/shortest-word-distance-ii/#/description
'''
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = {}
        for index, w in enumerate(words):
            self.dic[w] = self.dic.get(w, []) + [index]
        print(self.dic)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min([abs(i1 - i2) for i1 in self.dic[word1] for i2 in self.dic[word2]])

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)