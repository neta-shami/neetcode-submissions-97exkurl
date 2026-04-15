class TimeMap:

    def __init__(self):
        self.memory = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memory[key].append(tuple([timestamp , value]))
        
    def get(self, key: str, timestamp: int) -> str:

        ls = self.memory[key]
        if ls == [] or ls[0][0]>timestamp:
            return ""
        
        l , r = 0 ,len(ls)
        while l<r:
            mid = (l+r)//2
            if ls[mid][0] > timestamp:
                r = mid
            else:
                l = mid+1
        
        return ls[l-1][1]

        
