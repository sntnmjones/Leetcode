class Solution:
    '''
    solution: https://www.youtube.com/watch?v=Pr6T-3yB9RM
    '''
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)

        carGroups = []
        for car in cars:
            pos, spd = car
            timeRemaining = (target - pos) / spd
            
            carGroups.append(timeRemaining)

            # Compare the latest two timeRemainings. The first item in carGroups
            # will be the car closet to the target. So if the -1 is less than -2,
            # it means one of the cars further from the target is faster, resulting 
            # in a joined car group.
            if len(carGroups) >= 2 and carGroups[-1] <= carGroups[-2]:
                carGroups.pop()

        return len(carGroups)