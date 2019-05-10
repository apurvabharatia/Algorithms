#URLify

"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters
and that you are given the "true" length of the string.
"""

def URLify(word):
    result = ""
    if word[0] == " ":
        result += '%20'
    else:
        result += word[0]

    for letter in range(1, len(word)):
        if result[letter - 1] == '%20':
            continue
        elif word[letter] == " ":
            result += '%20'
        else:
            result += word[letter]
    return result

print(URLify("ajsd lajhdjs   aj "))

"""
https://www.geeksforgeeks.org/urlify-given-string-replace-spaces/
"""
