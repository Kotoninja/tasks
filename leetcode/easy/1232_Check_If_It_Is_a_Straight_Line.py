# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/?envType=study-plan-v2&envId=programming-skills


def checkStraightLine(coordinates: list[list[int]]) -> bool:
    x0, y0 = coordinates[0][0], coordinates[0][1]
    x1, y1 = coordinates[1][0], coordinates[1][1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i][0], coordinates[i][1]

        if (y - y0) * (x1 - x0) != (y1 - y0) * (x - x0):
            return False

    return True


print(checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(checkStraightLine([[0, 0], [0, 1], [0, -1]]))
print(checkStraightLine([[2, 4], [2, 5], [2, 8]]))
print(checkStraightLine([[1, -8], [2, -3], [1, 2]]))
print(checkStraightLine([[0, 0], [0, 5], [5, 5], [5, 0]]))
