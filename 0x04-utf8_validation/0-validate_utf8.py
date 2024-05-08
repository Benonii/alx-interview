#!/usr/bin/python3

"""
Contains the function validUTF8()
"""


def validUTF8(data):
    ''' Make sure data is utf-8 encoded(encodable) by using bitwise operations
    '''

    def calculate_bytes(num):
        ''' calculates how many bytes are used to represent a character in
            utf-8 '''
        mask = 0b10000000

        bytes = 0
        while num & mask:
            mask >>= 1
            bytes += 1
        return bytes

    i = 0
    while i < len(data):
        bytes = calculate_bytes(data[i])
        k = i + bytes - (bytes != 0)

        if bytes > 4 or bytes == 1 or k >= len(data):
            return False
 
        for j in range(1, bytes):
            ''' if calculate_bytes() returns 1, the number in binary
                starts with '10', making it a continuation bit '''
            i += 1
            is_continuation_bit = calculate_bytes(data[i])
            if is_continuation_bit != 1:
                return False
    return True
