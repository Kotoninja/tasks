# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/?envType=study-plan-v2&envId=programming-skills


def tictactoe(moves: list[list[int]]) -> str:
    field = [["_"] * 3 for _ in range(3)]

    for i in range(len(moves)):
        move = moves[i]
        print(move)
        if i % 2:
            field[move[0]][move[1]] = "O"
        else:
            field[move[0]][move[1]] = "X"

    def check_line(line) -> None | str:
        if len(line) == 1:
            if line == {"X"}:
                return "A"
            elif line == {"O"}:
                return "B"

    all_busy = 0
    for row in field:
        line = set(row)
        op = check_line(line)
        if op:
            return op
        if "_" not in row:
            all_busy += 1

    for i in range(len(field)):
        column = [field[j][i] for j in range(3)]
        line = set(column)
        op = check_line(line)
        if op:
            return op

    vert_right = [field[0][0], field[1][1], field[2][2]]
    print(vert_right)

    op = check_line(set(vert_right))
    if op:
        return op

    vert_left = [field[0][2], field[1][1], field[2][0]]

    op = check_line(set(vert_left))
    if op:
        return op

    if all_busy == 3:
        return "Draw"
    else:
        return "Pending"


# print(tictactoe([[0, 0], [2, 0], [0, 1], [2, 1], [0, 2]]))
# print(tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
# print(tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
