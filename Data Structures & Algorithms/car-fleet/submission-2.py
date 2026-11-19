class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # sort position and speed:
        position, speed = zip(*sorted(zip(position, speed), reverse=True))
        speed = list(speed)
        position = list(position)
        #return position, speed
        # the stack stores a candidate fleet.
        fleetwoodStack = []
        res = 0
        for i in range(len(position)):
            if not fleetwoodStack:
                fleetwoodStack.append(i)
                continue
            # if the fleet in the stack is too slow to catch the next car, empty the stack and increment res:
            currentCarTimeToDest = (target - position[i]) / speed[i]
            fleetTimeToDest = (target - position[fleetwoodStack[-1]]) / speed[fleetwoodStack[-1]]
            if fleetTimeToDest < currentCarTimeToDest:
                fleetwoodStack.clear()
                res += 1
                fleetwoodStack.append(i)
            else:
                position[i] = position[fleetwoodStack[-1]]
                speed[i] = speed[fleetwoodStack[-1]]
                fleetwoodStack.append(i)
        return 1 + res
