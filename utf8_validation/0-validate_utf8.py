#!/usr/bin/python3
"""
0-validate_utf8 module
Defines a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): Data represented by a list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    for num in data:
        byte = num & 0xFF

        if n_bytes > 0:
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1
        else:
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            else:
                return False

    return n_bytes == 0
