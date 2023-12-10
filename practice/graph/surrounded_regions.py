def surrounded_regions(matrix):
    deta_x = [-1, 0, +1, 0]
    delta_y = [0, +1, 0, -1]
    rows, cols = len(matrix), len(matrix[0])
    solution_matrix = [row.copy() for row in matrix]

    def dfs(row, col):
        if matrix[row][col] == "O":
            solution_matrix[row][col] = None
        for i in range(4):
            nrow, ncol = row + deta_x[i], col + delta_y[i]
            if 0 <= nrow < rows and 0 <= ncol < cols and matrix[nrow][ncol] == "O":
                dfs(nrow, ncol)

    for i in range(rows):
        for j in range(cols):
            if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and matrix[i][
                j
            ] == "O":
                dfs(i, j)

    for i in range(rows):
        for j in range(cols):
            if solution_matrix[i][j] == "O":
                solution_matrix[i][j] = "X"

    for i in range(rows):
        for j in range(cols):
            if solution_matrix[i][j] == None:
                solution_matrix[i][j] = "O"

    return solution_matrix


if __name__ == "__main__":
    mat = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    print(surrounded_regions(mat))
