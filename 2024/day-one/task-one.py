def get_difference_between_numbers_in_lists(first_list: list, second_list: list):
    first_list.sort()
    second_list.sort()
    
    merged_lists = zip(first_list, second_list)

    count = 0

    for pair in list(merged_lists):
        count += abs(pair[1] - pair[0])

    return count
