#!/usr/bin/env python3
# Code find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
# https://github.com/sagarapatel/Classic-Algorithms/blob/master/collatz_conjecture.py
# IDE PyCharm
# Python 3.8 compatible

x = int(input("Please enter positive number "))
count = 0
while x != 1:
    if x % 2 == 0:
        x = x / 2
        count += 1
    else:
        x = (x * 3) + 1
        count += 1

print("It takes {} steps to reach 1".format(count))
