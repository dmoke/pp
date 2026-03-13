# Kata: Rotate Matrix
# Rotates a matrix clockwise or counter-clockwise by 90 degrees.
# Handles both square and rectangular matrices.

import math


def rotate(matrix, direction):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        if direction == "clockwise":
            return [list(row) for row in zip(*matrix[::-1])]
        elif direction == "counter-clockwise":
            return [list(row) for row in zip(*matrix)][::-1]

    size = rows
    result = [row[:] for row in matrix]
    cycles = math.ceil(size / 2)

    for c in range(cycles):
        elementsNumber = size - 2 * c - 1

        for e in range(elementsNumber):
            top = matrix[c][c + e]

            if direction == "clockwise":
                result[c][c + e] = matrix[size - 1 - c - e][c]
                result[size - 1 - c - e][c] = matrix[size - 1 - c][size - 1 - c - e]
                result[size - 1 - c][size - 1 - c - e] = matrix[c + e][size - 1 - c]
                result[c + e][size - 1 - c] = top

            elif direction == "counter-clockwise":
                result[c][c + e] = matrix[c + e][size - 1 - c]
                result[c + e][size - 1 - c] = matrix[size - 1 - c][size - 1 - c - e]
                result[size - 1 - c][size - 1 - c - e] = matrix[size - 1 - c - e][c]
                result[size - 1 - c - e][c] = top

    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def main():
    for row in rotate(matrix, "clockwise"):
        print(f"{row}\n")


if __name__ == "__main__":
    main()
