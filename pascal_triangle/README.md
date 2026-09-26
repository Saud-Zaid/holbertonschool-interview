# Pascal's Triangle

## Description
This project contains an implementation of Pascal's Triangle algorithm in Python.

## Requirements
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the `pycodestyle` style (version 2.8.*)
- All your modules and functions should have documentation
- All your files must be executable

## Tasks

### 0. Pascal's Triangle
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of `n`:
- Returns an empty list if `n <= 0`
- You can assume `n` will be always an integer

#### Usage Example

```python
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
