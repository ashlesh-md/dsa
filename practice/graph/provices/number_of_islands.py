def number_of_islands(matrix):
    visited = set()
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    dx = [-1, 0, +1]
    dy = [-1, 0, +1]

    def dfs(row, column):
        visited.add((row, column))
        for delta_i in dx:
            for delta_j in dy:
                current_row = row + delta_i
                current_column = column + delta_j
                if (
                    0 <= current_row < number_of_rows
                    and 0 <= current_column < number_of_columns
                    and matrix[current_row][current_column] == 1
                    and (current_row, current_column) not in visited
                ):
                    dfs(current_row, current_column)

    count = 0
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if (row, column) not in visited and matrix[row][column] == 1:
                count += 1
                dfs(row, column)

    print(visited)
    return count


if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 1],
    ]
    print(number_of_islands(matrix))
