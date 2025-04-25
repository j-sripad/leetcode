class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [0]*len(speed)
        for i in range(len(speed)):
            cars[i] = [position[i],speed[i]]
        cars.sort(key = lambda x: x[0],reverse = True)
        stk =[]
        for p,s in cars:
            ctime = ( target - p ) / s
            if not stk or stk[-1] < ctime:
                stk.append(ctime)
        return len(stk)