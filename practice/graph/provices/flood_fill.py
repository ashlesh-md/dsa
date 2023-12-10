def flood_fill(matrix):
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    number_of_rows = len(matrix)
    number_of_cols = len(matrix[0])

    def dfs(row, column):
        if matrix[row][column] == 2:
            matrix[row][column] = 3

        for x in dx:
            for y in dy:
                current_row = row + x
                current_col = column + y

                if (
                    0 <= current_row < number_of_rows
                    and 0 <= current_col < number_of_cols
                    and matrix[current_row][current_col] == 2
                ):
                    dfs(current_row, current_col)

    dfs(0, 0)

    return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [2, 2, 0], [2, 2, 2]]
    print(flood_fill(matrix))
