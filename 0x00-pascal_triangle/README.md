# Pascal's Triangle

## Overview

This project implements Pascal's Triangle in Python. The program takes an integer `n` as input and returns the first `n` levels of Pascal's Triangle. Each row of Pascal's Triangle represents the coefficients of the binomial expansion, and it is constructed by summing adjacent elements from the previous row.

## Files

- `0-pascal_triangle.py`: Contains the `pascal_triangle()` function that generates Pascal's Triangle up to `n` levels.
- `0-main.py`: Test script to run the function and display the results.

## Function

### `pascal_triangle(n)`
- **Parameters**: 
  - `n` (integer): The number of rows to generate.
  
- **Returns**: 
  - A list of lists of integers representing Pascal's Triangle up to `n` levels. If `n` is less than or equal to 0, the function returns an empty list.

- **How it works**:
  1. The first row is initialized as `[1]`.
  2. For each subsequent row, it starts and ends with 1, while the intermediate values are the sum of the two adjacent elements from the previous row.
  3. This process is repeated until `n` rows are generated.

## Usage

To run the function and test it, use the `0-main.py` file:

```bash
./0-main.py
