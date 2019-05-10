#242. Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}

        for letter in s:
            if letter in dict_s:
                dict_s[letter] += 1
            else:
                dict_s[letter] = 1

        for letter in t:
            if letter in dict_t:
                dict_t[letter] += 1
            else:
                dict_t[letter] = 1
        if dict_s == dict_t:
            return True
        return False

"""
Questions to ask: 
Does case matter?
Do white spaces matter?

Alternative solution:
Sort both and compare
"""