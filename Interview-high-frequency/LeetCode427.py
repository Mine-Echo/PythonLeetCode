# 建立四叉树


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        return self.constructCore(grid, 0, len(grid), 0, len(grid[0]))

    def constructCore(
        self, grid: list[list[int]], i1: int, i2: int, j1: int, j2: int
    ) -> Node:
        if i1 >= i2:
            return None
        if i1 + 1 == i2:
            return Node(grid[i1][j1], True, None, None, None, None)
        val = grid[i1][j1]
        for i in range(i1, i2):
            for j in range(j1, j2):
                if grid[i][j] != val:
                    return Node(
                        val,
                        False,
                        self.constructCore(
                            grid, i1, (i1 + i2) // 2, j1, (j1 + j2) // 2
                        ),
                        self.constructCore(
                            grid, i1, (i1 + i2) // 2, (j1 + j2) // 2, j2
                        ),
                        self.constructCore(
                            grid, (i1 + i2) // 2, i2, j1, (j1 + j2) // 2
                        ),
                        self.constructCore(
                            grid, (i1 + i2) // 2, i2, (j1 + j2) // 2, j2
                        ),
                    )
        return Node(val, True, None, None, None, None)


if __name__ == "__main__":
    grid = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1]]
    Solution().construct(grid)
