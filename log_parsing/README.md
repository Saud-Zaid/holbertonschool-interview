# Log Parsing

## Description
This project contains a Python script `0-stats.py` that reads `stdin` line by line and computes metrics in real time:
- **Total file size**: Accumulated sum of `<file size>` from valid log lines.
- **Number of lines by status code**: Counts of occurrences for valid HTTP status codes (`200`, `301`, `400`, `401`, `403`, `404`, `405`, `500`), printed in ascending numerical order.

Statistics are printed:
- After every 10 lines processed.
- Upon receiving a keyboard interruption (`CTRL + C`).

## Requirements
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the `PEP 8` style (version 1.7.x)
- All your files must be executable
- All your modules and functions should have documentation

## Tasks

### 0. Log parsing
Write a script that reads stdin line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
  - `File size: <total size>`
  - `<status code>: <number>` (in ascending order, only if code appeared and is an integer)

#### Usage Example

```bash
alexa@ubuntu:~/log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
...
```
