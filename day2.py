"""
Day 2: Challenge 1

As you walk, the Elf shows you a small bag and some cubes which are 
either red, green, or blue. Each time you play this game, he will 
hide a secret number of cubes of each color in the bag, and your 
goal is to figure out information about the number of cubes.

The Elf would first like to know which games would have been possible if 
the bag contained only a certain number of each cube?
"""

from collections import defaultdict


# Open file
f = open("data/day2.txt")

# Build game dictionary
game_dict = defaultdict(list)

# Create nested dictionaries
for line in f.readlines():
    game_name, values = line.replace("\n", "").split(": ")

    # Split games
    for game in values.split("; "):
        # Create color: number dict
        color_counts = {}
        for pairs in game.split(", "):
            number, color = pairs.split(" ")
            color_counts[color] = int(number)

        # Append to main game_dict
        game_dict[game_name].append(color_counts)

# Input values
RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

# Sums
sum = 0
sum_power_of_minimuns = 0

# Checks all games
for game_name, rolls in game_dict.items():
    # Stores max for each game
    min_red = 0
    min_green = 0
    min_blue = 0

    # Check if this is a fail going through all
    # rolls for each game.
    failed = False
    for roll in rolls:
        min_red = max(min_red, roll.get("red", 0))
        min_green = max(min_green, roll.get("green", 0))
        min_blue = max(min_blue, roll.get("blue", 0))
        if (
            roll.get("red", 0) > RED_CUBES
            or roll.get("green", 0) > GREEN_CUBES
            or roll.get("blue", 0) > BLUE_CUBES
        ):
            failed = True

    # If this game was valid, then sum results
    sum_power_of_minimuns += min_blue * min_green * min_red
    if not failed:
        sum += int(game_name.split(" ")[1])

# Print results
print("This is not really a efficient way of solving this.")
print("Challenge 1: ", sum)
print("Challenge 2: ", sum_power_of_minimuns)
