"""
Usage: python total.py num1 num2 ...
"""

import sys


count = len(sys.argv)


total = 0.0
num_values = count - 1  # excludes the script name


while count > 1:
    count -= 1
    total += float(sys.argv[count])


if num_values > 0:
    average = total / num_values
    print("Total is", total)
    print("Average is", average)
else:
    print("no arguments were provided")
