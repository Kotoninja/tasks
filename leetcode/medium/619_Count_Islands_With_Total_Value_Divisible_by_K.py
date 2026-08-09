# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/description/?envType=problem-list-v2&envId=array


def countIslands(grid: list[list[int]], k: int) -> int:
        island_count = 0

        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0

            if not grid[i][j]:
                return 0

            current_value = grid[i][j]

            grid[i][j] = 0

            total_sum = current_value
            total_sum += dfs(i + 1, j)
            total_sum += dfs(i - 1, j)
            total_sum += dfs(i, j + 1)
            total_sum += dfs(i, j - 1)
            return total_sum

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                number = grid[i][j]

                if number:
                    result = dfs(i, j)
                    if not (result % k):
                        island_count += 1
        return island_count


print(
    countIslands(
        grid=[
            [2, 1, 0],
            [5, 0, 5],
        ],
        k=5,
    )
)
