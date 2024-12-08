import re
from input import input
from test_input import test_input

def find_mull_instructions(scrambled_instructions: str):
    multiply_regex = 'mul\(\d{1,3},\d{1,3}\)'

    matches = re.findall(multiply_regex, scrambled_instructions)
    total = 0

    for match in matches:
        splitted = match.replace("mul(","").split(",")
        multiplication = int(splitted[0]) * int(splitted[1][:-1])
        total += multiplication

    return total



print(find_mull_instructions(input))

