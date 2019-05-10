#String compression

"""
Implement a method to perform basic string compression using the counts of repeated characters.
"""

def stringCompression(word):
    cnt = 1
    prev = word[0]
    result = ""
    for index in range(1, len(word)):
        if word[index] != word[index - 1]:
            result += prev + str(cnt)
            prev = word[index]
            cnt = 1
        else:
            cnt += 1
    return result

print(stringCompression("aaabbccaa"))