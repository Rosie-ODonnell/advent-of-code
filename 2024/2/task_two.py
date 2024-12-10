from input import input
from test_input import test_input
from input import input


def row_is_safe(row): 
    if row == sorted(row) or row == sorted(row, reverse=True):
            differences = [abs(current-following) for current, following in zip(row[:-1], row[1:])]
            if all([num in [1,2,3] for num in differences]):
                return True
    
    return False


def check_number_of_safe_reports(reports):
    number_of_safe_reports = 0

    for row in reports:
        if row_is_safe(row):
            number_of_safe_reports += 1
        else:
            for index in range(len(row)):
                row_without_index = row[:index]+row[index+1:]
                if row_is_safe(row_without_index):
                    number_of_safe_reports += 1
                    break
                    
        
    return number_of_safe_reports    


structured_input = [[int(num) for num in line.split()] for line in input.strip().split('\n')]
print(check_number_of_safe_reports(structured_input))


