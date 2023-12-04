"""
Day 1: Challenge 2

On each line, the calibration value can be found by combining 
the first digit and the last digit (in that order) to form a 
single two-digit number.

Your calculation isn't quite right. It looks like some of the 
digits are actually spelled out with letters: one, two, three, 
four, five, six, seven, eight, and nine also count as valid 
"digits".
"""

import re

# Open file
f = open("data/day1-2.txt")

# Map strings to numbers
data_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# Store sum
sum = 0

# Go through lines
for line in f.readlines():
    numbers = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    sum += int(
        data_map.get(numbers[0], numbers[0])
        + data_map.get(numbers[-1], numbers[-1])
    )

print("Final result: ", sum)