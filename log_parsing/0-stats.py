#!/usr/bin/python3
"""
0-stats module
Reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code
"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints accumulated metrics: total file size and
    counts of valid status codes in ascending order.

    Args:
        total_size (int): The sum of all file sizes.
        status_codes (dict): Dictionary of status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_codes = {code: 0 for code in valid_codes}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    total_size += int(parts[-1])
                except (ValueError, IndexError):
                    pass

                try:
                    code = parts[-2]
                    if code in status_codes:
                        status_codes[code] += 1
                except (ValueError, IndexError):
                    pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        if line_count % 10 != 0:
            print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
