from collections import deque


def find_nearest_one(mat):
    visited = set()
    distance_matrix = [row for row in mat]
    rows, cols = len(mat), len(mat[0])
    _deque = deque()

    delta_x = [-1, 0, +1, 0]
    delta_y = [0, +1, 0, -1]

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                visited.add((i, j))
                _deque.append((i, j, 0))
                distance_matrix[i][j] = 0

    while _deque:
        current_row, current_col, distance = _deque.popleft()
        distance_matrix[current_row][current_col] = distance
        for i in range(4):
            nrow, ncol = current_row + delta_x[i], current_col + delta_y[i]
            if 0 <= nrow < rows and 0 <= ncol < cols and (nrow, ncol) not in visited:
                _deque.append((nrow, ncol, distance + 1))
                visited.add((nrow, ncol))

    return distance_matrix


if __name__ == "__main__":
    mat = [[0, 0, 0], [0, 1, 0], [1, 0, 1]]
    print(find_nearest_one(mat))
