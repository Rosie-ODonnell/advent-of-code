def find_frequency_of_item(first_list: list, second_list: list):
    second_list_item_count = {}
    frequency_count = 0

    for item in second_list:
        if second_list_item_count.get(item):
            second_list_item_count[item] +=1
        else:
            second_list_item_count[item] = 1

    for item in first_list:
        if count := second_list_item_count.get(item):
            frequency_count += (item * count)
        
    return frequency_count

    

list_one = []
list_two = []

print(find_frequency_of_item(list_one, list_two))