# Rotate 2D Matrix

## Description
This project implements an in-place algorithm in Python to rotate an `n x n` 2D matrix 90 degrees clockwise.

## Requirements
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the `PEP 8` style (version 1.7.x)
- All your files must be executable
- All your modules and functions should have documentation

## Tasks

### 0. Rotate 2D Matrix
Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.

- Prototype: `def rotate_2d_matrix(matrix):`
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

#### Usage Example

```python
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test  - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
```
