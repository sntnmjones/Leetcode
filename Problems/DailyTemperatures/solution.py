class Solution:
    # Solution explanation: https://www.youtube.com/watch?v=cTBiBSnjO3c
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysUntilHigherTemp = [0 for _ in temperatures]
        prevDayAndTemp = [] # [(temp, index)]

        for curDay, curDayTemp in enumerate(temperatures):
            while prevDayAndTemp and curDayTemp > prevDayAndTemp[-1][0]:
                prevDayTemp, prevDay = prevDayAndTemp.pop()
                daysUntilHigherTemp[prevDay] = curDay - prevDay
            prevDayAndTemp.append((curDayTemp, curDay))
        
        return daysUntilHigherTemp

        '''
        I had a hard time making sense of this so made the code verbose.
        Hopefully between that and the diagnosis below, it helps others.

        day 0
        for 0, 73 in enumerate(temperatures):
            while [] and curDayTemp > prevDayAndTemp[-1][0]:
                ...
            [].append((73, 0))

        day 1
        for 1, 74 in enumerate(temperatures):
            while [(73,0)] and 74 > 73:
                73, 0 = [(73,0)].pop()
                daysUntilHigherTemp[0] = 1 - 0
                # daysUntilHigherTemp = [1,0,0,0,0,0,0,0]
            [].append((74, 1))

        day 2
        for 2, 75 in enumerate(temperatures):
            while [(74, 1)] and 75 > 74:
                74, 1 = [(74, 1)].pop()
                daysUntilHigherTemp[1] = 2 - 1    
                # daysUntilHigherTemp = [1,1,0,0,0,0,0,0]
            [].append((75, 2))

        day 3
        for 3, 71 in enumerate(temperatures):
            while [(75, 2)] and 71 > 75:
                ...
            [(75, 2)].append((71, 3))
        
        day 4
        for 4, 69 in enumerate(temperatures):
            while [(75, 2),(71, 3)] and 69 > 71:
                ...
            [(75, 2),(71, 3)].append((69, 4))

        day 5
        for 5, 72 in enumerate(temperatures):
            while [(75, 2),(71, 3),(69, 4)] and 72 > 69:
                69, 4 = [(75, 2),(71, 3),(69, 4)].pop()
                daysUntilHigherTemp[4] = 5 - 4 
                # daysUntilHigherTemp = [1,1,0,0,1,0,0,0]
            # looping
            while [(75, 2),(71, 3)] and 72 > 71:
                71, 3 = [(75, 2),(71, 3)].pop()
                daysUntilHigherTemp[3] = 5 - 3 
                # daysUntilHigherTemp = [1,1,0,2,1,0,0,0]
            # looping
            while [(75, 2)] and 72 > 75:
                ...
            [(75, 2)].append((72, 5))

        day 6
        for 6, 76 in enumerate(temperatures):
            while [(75, 2),(72, 5)] and 76 > 72:
                72, 5 = [(75, 2),(72, 5)].pop()
                daysUntilHigherTemp[5] = 6 - 5 
                # daysUntilHigherTemp = [1,1,0,0,1,1,0,0]
            # looping
            while [(75, 2)] and 76 > 75:
                75, 2 = [(75, 2)].pop()
                daysUntilHigherTemp[2] = 6 - 2 
                # daysUntilHigherTemp = [1,1,4,2,1,1,0,0]
            # looping
            while [] and curDayTemp > prevDayAndTemp[-1][0]:
                ...
            [].append((76, 6))

        day 7
        for 7, 73 in enumerate(temperatures):
            while [(76, 6)] and 73 > 76:
                ...
            [(76, 6)].append((73, 7))  

        '''
