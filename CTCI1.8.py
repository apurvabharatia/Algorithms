#Zero matrix

"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        numRows = len(matrix)
        numCols = len(matrix[0])
        row = [0 for _ in range(numRows)]
        col = [0 for _ in range(len(matrix[0]))]
        for indexRow in range(numRows):
            for indexCol in range(numCols):
                if matrix[indexRow][indexCol] == 0:
                    row[indexRow] = 1
                    col[indexCol] = 1

        for index in range(len(row)):
            if row[index] == 1:
                matrix = self.nullifyRows(index, matrix)

        for index in range(len(col)):
            if col[index] == 1:
                matrix = self.nullifyCols(index, matrix)
        return matrix

    def nullifyRows(self, pos, matrix):
        l = len(matrix[0])

        for index in range(l):
            matrix[pos][index] = 0
        return matrix

    def nullifyCols(self, pos, matrix):
        l = len(matrix)
        for index in range(l):
            matrix[index][pos] = 0
        return matrix
