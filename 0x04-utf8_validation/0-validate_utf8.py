#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Helper function to check if a number has the correct format of leading bits
    def checkLeadingBits(num, count):
        mask = 1 << (count - 1)
        return (num & mask) == mask

    # Iterate through the data
    i = 0
    while i < len(data):
        # Get the number of bytes for the current character
        num_bytes = 0
        mask = 1 << 7
        while mask & data[i]:
            num_bytes += 1
            mask >>= 1

        # Check the validity of the number of bytes
        if num_bytes == 1 or num_bytes > 4:
            return False

        # Check the following bytes
        for j in range(1, num_bytes):
            i += 1
            if i >= len(data) or not checkLeadingBits(data[i], 2):
                return False

        i += 1

    return True
