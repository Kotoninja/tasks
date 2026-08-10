# https://www.codewars.com/kata/56bb9b7838dd34d7d8001b3c/train/python


def has_exit(maze):
    m = len(maze[0])
    n = len(maze)
    maze = [list(row) for row in maze]
    kx, ky = 0, 0

    kate_count = 0
    for i in range(n):
        for j in range(m):
            char = maze[i][j]
            if char == "k":
                if kate_count:
                    raise "There should no be multiple Kates"
                kx, ky = i, j
                kate_count += 1

    def find_exit(i, j):
        if i < 0 or i >= n or j < 0 or j >= m:
            return True

        if maze[i][j] == "#":
            return False

        maze[i][j] = "#"

        return (
            find_exit(i + 1, j)
            or find_exit(i - 1, j)
            or find_exit(i, j + 1)
            or find_exit(i, j - 1)
        )

    return bool(find_exit(i=kx, j=ky))


# print(has_exit(["###", "#k#", "###"]))
print(
    has_exit(
        maze=[
            "########",
            "# # ## #",
            "# #k#  #",
            "# # # ##",
            "# # #  #",
            "#     ##",
            "########",
        ]
    )
)
# print(has_exit(["###",
#                 "#k#",
#                 "###"]))
# print(has_exit(["###",
#                 "#k#",
#                 "###"]))
