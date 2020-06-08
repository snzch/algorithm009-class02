# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1:
#
#  输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
#
#
#  示例 2:
#
#  输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [['0'] * cols for _ in range(rows)]

        def dfs(row, col):
            if row > rows - 1 or row < 0 or \
                    col > cols - 1 or col < 0 or\
                    visited[row][col] == '1' or \
                    grid[row][col] == '0':
                return

            visited[row][col] = '1'
            for d in directions:
                next_row, next_col = row + d[0], col + d[1]
                dfs(next_row, next_col)

        nums = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c] == '0' and grid[r][c] == '1':
                    nums += 1
                    dfs(r, c)
        return nums


# leetcode submit region end(Prohibit modification and deletion)
