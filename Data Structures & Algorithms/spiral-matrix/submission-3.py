class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        topRow = leftCol = 0
        bottomRow = m
        rightCol = n

        while leftCol < rightCol and topRow < bottomRow:
            
            for j in range(leftCol , rightCol):
                result.append(matrix[topRow][j])
            topRow+=1
            for i in range(topRow , bottomRow):
                result.append(matrix[i][rightCol-1])
            rightCol-=1
            
            if rightCol <= leftCol or bottomRow <= topRow :
                return result 
            for j in range(rightCol-1 , leftCol-1 ,-1):
                result.append(matrix[bottomRow-1][j])
            bottomRow-=1
            for i in range(bottomRow-1 ,topRow-1 ,-1):
                result.append(matrix[i][leftCol])
            leftCol+=1

        return result






            




            




        