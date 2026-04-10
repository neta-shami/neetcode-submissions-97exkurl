class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = 9 

        for row in board:
            seen = set()
            for element in row:
                if element == ".":
                    pass
                else:
                    if element in seen:
                        return False
                    else:
                        seen.add(element)
        
        for col in range(n):
            seen = set()
            for row in range(n):
                element = board[row][col]
                if element == ".":
                    pass
                else:
                    if element in seen:
                        return False
                    else:
                        seen.add(element)

         
        for group1 in range(3):
            for group2 in range(3):
                seen = set()
                for row in range(n):
                    if row // 3 == group1:
                        for col in range(n):
                            if col // 3 == group2:
                                element = board[row][col]
                                if element == ".":
                                    pass
                                else:
                                    if element in seen:
                                        return False
                                    else:
                                        seen.add(element)
        return True

        

        


        