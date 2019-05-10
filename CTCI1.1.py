#Is Unique
"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

"""

def isUnique(word):

    d = {}
    for letter in word:
        if letter in d:
            return False
        d[letter] = 1

    return True

result = isUnique("triala")
print( result)

"""
ASCII vs Unicode

ASCII defines 128 characters, which map to the numbers 0–127. Unicode defines (less than) 221 characters, which, similarly, map to numbers 0–221 (though not all numbers are currently assigned, and some are reserved).

Unicode is a superset of ASCII, and the numbers 0–128 have the same meaning in ASCII as they have in Unicode. For example, the number 65 means "Latin capital 'A'".

Because Unicode characters don't generally fit into one 8-bit byte, there are numerous ways of storing Unicode characters in byte sequences, such as UTF-32 and UTF-8.

------------

Bit vector: 1 for each letter in the alphabet
Make true if that letter is present in the string. If you are trying to set True and it is already true, return False.

------------

No Additional data structures:
1.) Compare each alphabet with every other alphabet (O(n^2)).
2.) Sort and linearly check if to consecutive letters are same.

"""
