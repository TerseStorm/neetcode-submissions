class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [ [0] * len(text2) for _ in range(len(text1)) ]
        if text1[0] in text2[0]:
            matrix[0][0] = 1
        else:
            matrix[0][0] = 0
        for j in range(1,len(text2)):
            if text1[0] == text2[j]:
                matrix[0][j] = 1
            else:
                matrix[0][j] = matrix[0][j-1]
        for i in range(1, len(text1)):
            matrix[i][0] = matrix[i-1][0]
            if text2[0] == text1[i]:
                matrix[i][0] = 1
            else:
                matrix[i][0] = matrix[i-1][0]
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
        return matrix[-1][-1]