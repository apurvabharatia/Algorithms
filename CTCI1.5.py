#One Away

"""
There are three types of edits that can be performed on strings: insert a character, remove a character or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
"""

def replace(word1, word2):

    flag = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if flag == True:
                return False
            flag = True
    return True

def insertDelete(smaller, greater):

    index_smaller = 0
    index_greater = 0

    while(index_smaller < len(smaller) and index_greater < len(greater)):
        if smaller[index_smaller] != greater[index_greater]:
            if index_smaller != index_greater:
                return False
            index_greater += 1
        index_smaller += 1
        index_greater += 1

    return True


def oneAway(word1, word2):

    if len(word1) == len(word2):
        return replace(word1, word2)

    if len(word1) + 1 == len(word2):
        return insertDelete(word1, word2)

    if len(word2) + 1 == len(word1):
        return insertDelete(word2, word1)

print(oneAway("pale", "bake"))

"""
**Combine replace and insertDelete into one method.
"""
