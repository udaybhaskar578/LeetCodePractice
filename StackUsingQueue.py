'''
Author: Sai Uday Bhaskar Mudivarty
Program: https://leetcode.com/problems/implement-stack-using-queues/#/description
'''
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stacklist = list()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stacklist.insert(0,x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.empty():
            return self.stacklist.pop(0)
        else:
            return None
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.empty():
            return self.stacklist[0]
        else:
            return None
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stacklist) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Using Deque from collections

from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deq=deque()
        
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.deq.append(x)
        for i in range(0, len(self.deq)-1):
            first=self.deq.popleft()
            self.deq.append(first)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.deq.popleft()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.deq[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.deq)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()