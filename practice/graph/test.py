from collections import deque


def distinctIsland(arr, n, m):
    rows, cols = n, m
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
                    and arr[nrow][ncol] == 1
                    and (nrow, ncol) not in visited
                ):
                    _deque.append((nrow, ncol))
                    current_pattern.append((nrow - row, ncol - col))
                    visited.add((nrow, ncol))
        return tuple(current_pattern)

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and arr[i][j] == 1:
                _deque.append((i, j))
                patterns.add(bfs(i, j))

    return len(patterns)
