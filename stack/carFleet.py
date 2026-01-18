#Time complexity: O(n)
#Stack question from Neetcode

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        myhash = {}
        for i in range(len(position)):
            myhash[position[i]] = i
        position.sort(reverse=True)
        stack = [position[0]]
        frontspeed = speed[myhash[stack[0]]]
        for i in range(1, len(position)):
            rear = position[i]
            front = stack[-1]
            distance = front - rear
            rearspeed = speed[myhash[position[i]]]
            sdif = rearspeed - frontspeed
            if sdif<=0:
                stack.append(position[i])
                frontspeed = speed[myhash[position[i]]]
                 #cant catch
                continue
            catchstep = distance / sdif
            leftstep = (target-front) / frontspeed
            if leftstep < catchstep:
                stack.append(position[i])
                frontspeed = speed[myhash[position[i]]]
                 #cant catch
        return len(stack)