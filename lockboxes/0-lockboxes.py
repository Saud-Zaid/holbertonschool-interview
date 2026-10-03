#!/usr/bin/python3
"""
0-lockboxes module
Defines a method that determines if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists of keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    opened = {0}
    keys = [0]

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and key not in opened:
                opened.add(key)
                if len(opened) == n:
                    return True
                keys.append(key)

    return len(opened) == n
