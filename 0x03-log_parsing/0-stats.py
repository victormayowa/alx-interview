#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""

import sys


def print_metrics(total_size, status_codes):
    """
    Prints the computed metrics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """
    Main function to compute and print metrics.
    """
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0,
                    '405': 0, '500': 0}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parts = line.split()
            if len(parts) >= 9:
                status_code = parts[-2]
                file_size = parts[-1]
                if status_code in status_codes:
                    total_size += int(file_size)
                    status_codes[status_code] += 1

            if i % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_metrics(total_size, status_codes)


if __name__ == "__main__":
    main()
