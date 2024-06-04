#!/usr/bin/python3

''' This module contains the function makeChange() '''


def makeChange(coins, total):
    ''' Returns the minimum number of coins needed to make change '''

    if total <= 0:
        return 0

    memo = [0]
    for i in range(1, total + 1):
        memo.append(total + 1)

    for i in range(1, len(memo)):
        for coin in coins:
            if coin <= i:
                memo[i] = min(memo[i - coin] + 1, memo[i])
    if memo[total] > total:
        return -1

    return memo[total]
