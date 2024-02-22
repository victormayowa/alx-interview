#!/usr/bin/python3
'alx-interview 007'


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (List[List[int]]): The input matrix to rotate.

    Returns:
        None: The matrix is rotated in-place. No return value.

    Example:
        >>> matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
        >>> rotate_2d_matrix(matrix)
        >>> print(matrix)
        [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
