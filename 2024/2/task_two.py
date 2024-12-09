from input import input
from test_input import test_input

# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.

from input import input

def check_number_of_safe_reports(reports):
    number_of_safe_reports = 0

    for row in reports:

        if row == sorted(row) or row == sorted(row, reverse=True):
            
            differences = [abs(current-following) for current, following in zip(row[:-1], row[1:])]

            if all([num in [1,2,3] for num in differences]):
                number_of_safe_reports += 1
        
    return number_of_safe_reports    


structured_input = [[int(num) for num in line.split()] for line in input.strip().split('\n')]
print(check_number_of_safe_reports(structured_input))












# if row[0] > row[1]:
#         row.reverse()
    
#     number_of_safe_levels = 1

#     for index in range(0, len(row)): 
#         if row[index] > row[index -1]:
#             if not abs(row[index] - row[index-1]) == 0 and not abs(row[index]-row[index-1]) > 3:
#                 number_of_safe_levels += 1

#         if number_of_safe_levels == len(row):
#             number_of_safe_reports += 1
