import re
from input import input
from test_input import test_input

def find_mull_instructions(scrambled_instructions: str):
    scrambled_instructions_starts_with_mul = scrambled_instructions.startswith("mul(")
    all_statements_starting_with_mul = scrambled_instructions.split("mul(")

    if not scrambled_instructions_starts_with_mul:
        del all_statements_starting_with_mul[0]

    final_total = 0

    for index,statement in enumerate(all_statements_starting_with_mul):
        pattern = '[\d]{1,3},[\d]{1,3}\)'
        match = re.search(pattern, statement)
        if match:
            splitted = match.group(0).split(",")
            multiplication = int(splitted[0]) * int(splitted[1][:-1])
            final_total += multiplication


    return final_total


print(find_mull_instructions(input))

