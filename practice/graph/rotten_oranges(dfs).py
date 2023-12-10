# By using DFS it is only possible to make all the oranges rotten it is not possible to calculate the level or time
from collections import deque


# def rotten_oranges(matrix):
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     rows, cols = len(matrix), len(matrix[0])
#     visited = []
#     _deque = deque()

#     def bfs():
#         while _deque:
#             r, c, time = _deque.popleft()
#             visited.append((r, c, time))
#             for x, y in zip(dx, dy):
#                 current_row, current_col = r + x, c + y
#                 if (
#                     0 <= current_row < rows
#                     and 0 <= current_col < cols
#                     and matrix[current_row][current_col] == 1
#                 ):
#                     matrix[current_row][current_col] = 2
#                     _deque.append((current_row, current_col, time + 1))

#     for row in range(rows):
#         for column in range(cols):
#             if matrix[row][column] == 2:
#                 _deque.append((row, column, 0))
#     bfs()
#     if any(1 in row for row in matrix):
#         return -1
#     return visited[-1][-1] if visited else 0


def rotten_oranges(matrix):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    rows, cols = len(matrix), len(matrix[0])
    visited = []
    _deque = deque()

    total_time = 0

    for row in range(rows):
        for column in range(cols):
            if matrix[row][column] == 2:
                _deque.append((row, column, 0))

    while _deque:
        r, c, time = _deque.popleft()
        visited.append((r, c, time))
        total_time = max(time, total_time)
        for x, y in zip(dx, dy):
            current_row, current_col = r + x, c + y
            if (
                0 <= current_row < rows
                and 0 <= current_col < cols
                and matrix[current_row][current_col] == 1
            ):
                matrix[current_row][current_col] = 2
                _deque.append((current_row, current_col, time + 1))

    if any(1 in row for row in matrix):
        return -1
    return total_time if visited else 0


if __name__ == "__main__":
    matrix = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(rotten_oranges(matrix))



def rotten_oranges(matrix):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    rows, cols = len(matrix), len(matrix[0])
    visited = set()

    def dfs(row, col, time):
        visited.add((row, col))
        for x, y in zip(dx, dy):
            current_row, current_col = row + x, col + y
            if (
                0 <= current_row < rows
                and 0 <= current_col < cols
                and (current_row, current_col) not in visited
                and matrix[current_row][current_col] == 1
            ):
                matrix[current_row][current_col] = 2
                dfs(current_row, current_col, time + 1)

    for row in range(rows):
        for column in range(cols):
            if matrix[row][column] == 2:
                dfs(row, column, 0)

    if any(1 in row for row in matrix):
        return -1
    return max(visited, key=lambda x: x[2])[2]

if __name__ == "__main__":
    matrix = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(rotten_oranges(matrix))

