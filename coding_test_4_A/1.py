def diagonal_traverse_str(strArr):
    # Convert the string representation of list to an actual list of lists
    # Using list comprehension and map function
    matrix = [list(map(int, row.strip("[]").split(","))) for row in strArr]

    if not matrix or not matrix[0]:
        return ""

    rows, cols = len(matrix), len(matrix[0])
    result = []
    row, col = 0, 0

    for _ in range(rows * cols):
        result.append(str(matrix[row][col]))
        if (row + col) % 2 == 0:
            if col == cols - 1:
                row += 1
            elif row == 0:
                col += 1
            else:
                row -= 1
                col += 1
        else:
            if row == rows - 1:
                col += 1
            elif col == 0:
                row += 1
            else:
                row += 1
                col -= 1

    return ", ".join(result)
