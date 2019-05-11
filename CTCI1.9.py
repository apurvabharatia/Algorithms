class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        return len(A) == len(B) and B in A + A
"""
Check if one string is contained completely in twice of another string
"""