from test_input import test_input
from input import input

def filter_out_non_increasing_or_decreasing_levels(x):

    if x == sorted(x) or x == sorted(x, reverse=True):
        if len(x) == len(set(x)):
            return True
    else:
        return False


def check_number_of_safe_reports(reports):
    number_of_safe_reports = 0
    filtered_reports = list(filter(filter_out_non_increasing_or_decreasing_levels, reports))
    for row in filtered_reports:
        differences = [abs(j-i) for i, j in zip(row[:-1], row[1:])]
        if all([num in [1,2,3] for num in differences]):

            number_of_safe_reports += 1
        


    return number_of_safe_reports    



structured_input = [[int(num) for num in line.split()] for line in input.strip().split('\n')]
print(check_number_of_safe_reports(structured_input))


