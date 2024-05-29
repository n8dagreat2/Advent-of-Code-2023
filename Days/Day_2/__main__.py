import re
import sys

sys.path.append("..")
from input_extract import input_extract

"""
--- Day 2: Cube Conundrum ---

### Part 1 ###

You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

### Part 2 ###

The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
    Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
    Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
    Game 4 required at least 14 red, 3 green, and 15 blue cubes.
    Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""

# CONSTANTS
# GAME_REGEX = r"\w+\s+(\d+):"
SUB_GAME_REGEX = r"\d+\s+(?:red|green|blue)"
GAME_CONSTRAINTS = {"red": 12, "blue": 14, "green": 13}
CUBE_MAX = sum(GAME_CONSTRAINTS.values())


def get_sub_game_data(game_input: str):
    """
    Splits each sub game into usable data (total number of each color cube) in order to determine certain conditions.
    Part 1
        If any one of the sub games is determined to be invalid, the entire game is invalid (temp["is_valid"] = False)
    Part 2
        Get all the minimum number of cubes per game and save it (temp["min_cubes"]:dict)
    """
    temp = {}
    temp["is_valid"] = True
    temp["min_cubes"] = {"red": 0, "green": 0, "blue": 0}
    i = 0  # sub game tracker
    for sub_game in game_input.split(";"):
        split_in = re.findall(SUB_GAME_REGEX, sub_game)  # Get each subgame in a list
        temp[f"sub_game{i}"] = {}
        for x in split_in:
            total, color = x.split()  # Get usable data into two variables
            temp[f"sub_game{i}"][color] = int(total)
            # Part 1 Condition Checking
            if int(total) > GAME_CONSTRAINTS[color]:
                # total number of the current color cube is greater than the total number of that color cube available
                temp[f"sub_game{i}"]["is_valid"] = False
                temp["is_valid"] = False  # Current game is invalid
            else:
                temp[f"sub_game{i}"]["is_valid"] = True
            # Part 2 Data Collection
            if int(total) > temp["min_cubes"][color]:
                temp["min_cubes"][color] = int(total)

        i += 1
    return temp


def day2_1(input_lines: list):
    """
    Objective:
        Take input data (input_lines:list), which is comprised of each individual line from input.txt as an index in the list,
        and returns the list of all game ids that are valid (total:list).
    Constants Used:
        SUB_GAME_REGEX - regex used to get the subgame data into an iterable list
        GAME_CONSTRAINTS - list used to determine if a subgame has more colored cubes than the total number of each color cube available
    """
    total = []
    game_dict = {}  # Put all games into a dictionary for more data processing if needed
    for line in input_lines:
        game = line.strip().split(":")
        game_id = int(game[0].split()[1])
        sub_game = game[1]
        sub_game_dict = get_sub_game_data(sub_game)
        game_dict[game_id] = sub_game_dict
        if sub_game_dict["is_valid"]:
            total.append(game_id)
    return total


def day2_2(input_lines: list):
    """
    Objective:
        Take input data (input_lines:list), which is comprised of each individual line from input.txt as an index in the list,
        and returns the list of each game id cube minimum totals multiplied together (total:list).
    Constants Used:
        SUB_GAME_REGEX - regex used to get the subgame data into an iterable list
    """
    total = []
    game_dict = {}  # Put all games into a dictionary for more data processing if needed
    for line in input_lines:
        game = line.strip().split(":")
        game_id = int(game[0].split()[1])
        sub_game = game[1]
        sub_game_dict = get_sub_game_data(sub_game)
        game_dict[game_id] = sub_game_dict
        # Multiply each min cube together
        prod = 1
        for x in sub_game_dict["min_cubes"].values():
            prod *= x
        total.append(prod)
    return total


if __name__ == "__main__":
    input_lines = input_extract("input.txt")
    total1 = day2_1(input_lines)
    total2 = day2_2(input_lines)
    print(25 * "*")
    print("*\t  DAY 2\t\t*")
    print(25 * "*")
    print(3 * "#" + " Part 1 " + 3 * "#" + "\n")
    print(f"The sum of all valid games for Part 1 of Day 2 is: {sum(total1)}\n")
    print(3 * "#" + " Part 1 " + 3 * "#" + "\n")
    print(
        f"The sum of all minimum cubes total products for Part 2 of Day 2 is: {sum(total2)}"
    )
