#Palindrome Permutation

"""
Given a string, write a function to check if it is a permutation of a palindrome.
"""

def checkPalindromePermutation(word):

    d = {}
    for letter in word:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    tempWord = list(set(word))
    flag = 0
    for letter in tempWord:
        if d[letter] % 2 == 1:
            if flag == 1:
                return False
            flag = 1
    return True

print(checkPalindromePermutation(""))

"""
1.) Create a bit vector of alphabets and have a variable that keeps track of how many bits have odd count.
In the end if that variable is greater than 1, return false.
Advantage: No additional look up in the hash table required after one pass over the string.

2.) Treat the bit vector table like a switch board. Turn "on" (set to 1) if count is odd, else 0.
If there are more than 1 "on" values, return False.


"""
