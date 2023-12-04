"""
Day 1: Challenge 1

The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that 
the Elves now need to recover. On each line, the calibration value 
can be found by combining the first digit and the last digit (in 
that order) to form a single two-digit number.
"""

import re

# Open file
f = open("data/day1-1.txt")

# Store sum
sum = 0

# Go through lines
for line in f.readlines():
    numbers = re.findall(r"(\d)", line)
    sum += int(numbers[0] + numbers[-1])

print("Final result: ", sum)