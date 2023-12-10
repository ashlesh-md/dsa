from collections import deque


def number_of_distinct_icelands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    _deque = deque()
    patterns = set()

    def bfs(row, col):
        current_pattern = []
        while _deque:
            current_row, current_col = _deque.popleft()
            for direction in [(-1, 0), (0, +1), (+1, 0), (0, -1)]:
                nrow = current_row + direction[0]
                ncol = current_col + direction[1]
                if (
                    0 <= nrow < rows
                    and 0 <= ncol < cols
                    and grid[nrow][ncol] == 1
                    and (nrow, ncol) not in visited
                ):
                    _deque.append((nrow, ncol))
                    current_pattern.append((nrow - row, ncol - col))
                    visited.add((nrow, ncol))
        return tuple(current_pattern)

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and grid[i][j] == 1:
                _deque.append((i, j))
                patterns.add(bfs(i, j))

    return len(patterns)


if __name__ == "__main__":
    grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    print(number_of_distinct_icelands(grid))
