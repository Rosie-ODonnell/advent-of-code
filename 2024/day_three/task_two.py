import re

def find_mull_instructions(scrambled_instructions: str):
    multiply_regex = 'mul\(\d{1,3},\d{1,3}\)'
    without_donts =  re.sub(r'don\'t\(\)[\s\S]*?(do\(\)|$)', '', scrambled_instructions)

    mul_statements = re.findall(multiply_regex, without_donts)
    total = 0

    for statement in mul_statements:
        splitted = statement.replace("mul(","").replace(")","").split(",")
        total += int(splitted[0]) * int(splitted[1])

    return total

instructions = open("/Users/rosie/Documents/Code/advent-of-code/2024/day_three/input.txt").read()

print(find_mull_instructions(instructions))

# original regex that didn't work - without_donts = re.sub(r"don't\(\)(.*?)(?:do\(\)|$)", "", scrambled_instructions)
#