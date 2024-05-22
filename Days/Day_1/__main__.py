import re
import sys

sys.path.append("..")
from input_extract import input_extract

"""
--- Day 1: Trebuchet?! ---

### Part 1
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

### Part 2

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

# CONSTANTS
NUM_REGEX = r"\d"
NUM_REGEX_2 = r"oneight|threeight|fiveight|nineight|twone|sevenine|eightwo|eighthree|one|two|three|four|five|six|seven|eight|nine|\d"
NUM_TABLE = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "oneight": ["1", "8"],
    "threeight": ["3", "8"],
    "fiveight": ["5", "8"],
    "nineight": ["9", "8"],
    "twone": ["2", "1"],
    "sevenine": ["7", "9"],
    "eightwo": ["8", "2"],
    "eighthree": ["8", "3"],
}


def day1_1(input_lines: list):
    """
    Objective:
        Take input data (input_lines:list), which is comprised of each individual line from input.txt as an index in the list,
        and returns the list of all calibration values (total).
    Constants Used:
        NUM_REGEX - regex used to get all numeric values from a value in the input_lines list
    """
    total = []
    for line in input_lines:
        found_nums = re.findall(NUM_REGEX, line)
        first_digit = found_nums[0]
        second_digit = found_nums[-1]
        actual_num = int(first_digit + second_digit)
        total.append(actual_num)
    return total


def day1_2(input_lines: list):
    """
    Objective:
        Take input data (input_lines:list), which is comprised of each individual line from input.txt as an index in the list,
        and returns the list of all calibration values (total).
    Constants Used:
        NUM_REGEX_2 - regex used to get all numeric and literal values from a value in the input_lines list
        NUM_TABLE - map literal values to their numeric counterparts
    """
    total = []
    for line in input_lines:
        found_nums = re.findall(NUM_REGEX_2, line)
        first_digit = (
            found_nums[0]
            if found_nums[0].isnumeric()
            else str(NUM_TABLE[found_nums[0]][0])
        )
        if found_nums[-1].isnumeric():
            second_digit = found_nums[-1]
        elif len(NUM_TABLE[found_nums[-1]]) > 1:
            second_digit = str(NUM_TABLE[found_nums[-1]][1])
        else:
            second_digit = str(NUM_TABLE[found_nums[-1]])
        actual_num = int(first_digit + second_digit)
        total.append(actual_num)
    return total


if __name__ == "__main__":
    input_lines = input_extract("input.txt")
    total1 = day1_1(input_lines)
    total2 = day1_2(input_lines)
    print(25 * "*")
    print("*\t  DAY 1\t\t*")
    print(25 * "*")
    print(3 * "#" + " Part 1 " + 3 * "#" + "\n")
    print(f"The sum of all calibration values for Part 1 of Day 1 is: {sum(total1)}\n")
    print(3 * "#" + " Part 1 " + 3 * "#" + "\n")
    print(f"The sum of all calibration values for Part 2 of Day 1 is: {sum(total2)}")
