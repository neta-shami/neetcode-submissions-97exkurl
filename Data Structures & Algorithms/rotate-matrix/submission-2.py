class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        f = n//2 
        
        for i in range(f):
            topRow = leftCol = i
            bottomRow = rightCol = n-1-i
            for offset in range(rightCol - leftCol):
                temp = matrix[topRow][leftCol+offset]
                matrix[topRow][leftCol+offset] = matrix[bottomRow-offset][leftCol]
                matrix[bottomRow-offset][leftCol] = matrix[bottomRow][rightCol - offset]
                matrix[bottomRow][rightCol - offset] = matrix[topRow+offset][rightCol]
                matrix[topRow+offset][rightCol] = temp
        