class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(speed)
        for i in range(n):
            position[i] = [position[i] , speed[i]]
        
        position.sort()

        fleets = 0
        maxArriveTime= -1
        for j in range(n-1 , -1 , -1):
            arrivelTime =  (target - position[j][0]) / position[j][1]

            if maxArriveTime < arrivelTime:
                fleets+=1
                maxArriveTime = arrivelTime
        return fleets


