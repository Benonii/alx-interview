#!/usr/bin/python3
"""
Main file for testing
"""

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(4, [11, 30, 1, 7])))
