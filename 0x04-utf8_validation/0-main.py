#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data)) # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data)) # True

data = [229, 65, 127, 256]
print(validUTF8(data)) # False

data = [192, 128, 65]
print(validUTF8(data)) # False

data = [128]
print(validUTF8(data)) # False

data = [226, 130]
print(validUTF8(data)) # False


data = [128, 65]
print(validUTF8(data)) # False

data = [240, 159, 152, 138] # True
print(validUTF8(data)) #


data = [0] # True
print(validUTF8(data))

data = [240, 159, 159, 159]
print(validUTF8(data)) # True #

data = [120]
print(validUTF8(data)) # True

data = [195, 191]
print(validUTF8(data)) # True #
