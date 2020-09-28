#!/usr/bin/env python3
# Program to sort using Bubble sort method:
# Compare the number with previous number if its smaller swap places.
# https://github.com/sagarapatel/Classic-Algorithms/blob/master/sorting.py
# IDE PyCharm
# Python 3.8 compatible

import random


def bubblesort(lst):
    n = len(lst)
    for i in range(n - 1):
        check_sort = True
        for j in range(n - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap the numbers in list
                check_sort = False
        if check_sort:
            break  # Break if no more sorting required
    return lst


lst = random.sample(range(0, 100), 7)  # Generate seven random numbers list between 0 and 100
print(lst)
print(bubblesort(lst))
