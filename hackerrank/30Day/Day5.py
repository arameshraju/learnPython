#!/bin/python3

import math
import os
import random
import re
import sys

# Task
# Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.
#
# Input Format
#
# A single integer, .
#
# Constraints
#
# Output Format
#
# Print  lines of output; each line  (where ) contains the  of  in the form:
# n x i = result.

if __name__ == '__main__':
    n = int(input())

    for i in range(1,11):
        print(str(n) + " x " + str(i) + " = " + str(i*n) )
