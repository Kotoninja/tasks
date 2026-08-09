# https://leetcode.com/problems/robot-bounded-in-circle/description/?envType=study-plan-v2&envId=programming-skills

import math


def isRobotBounded(instructions: str) -> bool | str:
        x_axis = 0
        y_axis = 0


        directions = 90
        for _ in range(4):
            for move in instructions:
                match move:
                    case "L":
                        directions += 90
                    case "R":
                        directions -= 90
                    case "G":
                        step = math.radians(directions)

                        y_axis += round(math.sin(step))
                        x_axis += round(math.cos(step))
                            
            if not x_axis and not y_axis:
                return True
        return False


print(isRobotBounded("GGLLGG"))
print(isRobotBounded("GG"))
print(isRobotBounded("GL"))