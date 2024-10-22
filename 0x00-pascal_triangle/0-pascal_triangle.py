#!/usr/bin/python3
"""
    Pascal's Triangle Generation Module
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle (as a list of lists).
    Returns an empty list if 'n' is less than or equal to 0.
    """
    # Check if the input number is valid
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Loop to build each subsequent row
    for _ in range(1, n):
        previous_row = triangle[-1]
        current_row = [1]  # Each row starts with 1

        # Calculate the values in between the 1s
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])

        current_row.append(1)  # End the row with 1
        triangle.append(current_row)

    return triangle
