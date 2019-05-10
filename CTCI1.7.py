#Rotate Matrix
"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for row in range(l):
            for col in range(row, l):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        ind = 0
        for row in matrix:
            matrix[ind] = row[::-1]
            ind += 1
        return matrix


"""
row = row[::-1] won't work becuase it is a shallow copy
"""
