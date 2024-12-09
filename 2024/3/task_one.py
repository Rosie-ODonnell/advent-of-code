import re
from input import input

def find_mull_instructions(scrambled_instructions: str):
    multiply_regex = 'mul\(\d{1,3},\d{1,3}\)'
    mul_statements = re.findall(multiply_regex, scrambled_instructions)
    total = 0

    for statement in mul_statements:
        splitted = statement.replace("mul(","").replace(")","").split(",")
        total += int(splitted[0]) * int(splitted[1])

    return total

print(find_mull_instructions(input))

