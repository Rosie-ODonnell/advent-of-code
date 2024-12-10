import re

def find_xmas():
    with open("/Users/rosie/Documents/Code/advent-of-code/2024/4/test_input.txt") as word_search:
        word_search_grid = [[letters for letters in line] for line in word_search.read().strip().split('\n')]
    
    xmas_count = 0

    for row in word_search_grid:
        xmas_count += check_forwards_and_backwards(row)

    # need to loop through each array comparing indexes
    # have separate funciton for each direction - check_forwards_and_backwards, check_up_and_down, check_diagonal, check_backwards
    return xmas_count


def check_forwards_and_backwards(row):
    return len(re.findall('XMAS', ''.join(row))+re.findall('XMAS', ''.join(row[::-1])))


print(find_xmas())