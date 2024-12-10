def find_xmas():
    with open("/Users/rosie/Documents/Code/advent-of-code/2024/4/test_input.txt") as word_search:
        word_search_grid = [[letters for letters in line] for line in word_search.read().strip().split('\n')]


    # need to loop through each array comparing indexes
    # have separate funciton for each direction - check_forwards_and_backwards, check_up_and_down, check_diagonal, check_backwards

    print(word_search_grid, "grid")




print(find_xmas())