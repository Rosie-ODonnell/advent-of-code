from input import input
from test_input import test_input

def check_for_bad_rows(number_of_safe_reports, reports):
    for row in reports:

        if row == sorted(row) or row == sorted(row, reverse=True):
            differences = [abs(current-following) for current, following in zip(row[:-1], row[1:])]

            if all([num in [1,2,3] for num in differences]):


                # // need to enter recursion - need to loop again but this time remove one item in list
                number_of_safe_reports += 1

    return number_of_safe_reports

def check_number_of_safe_reports(reports):
    number_of_safe_reports = 0

    number_of_safe_reports = check_for_bad_rows(number_of_safe_reports, reports)
            
    return number_of_safe_reports  
        


structured_input = [[int(num) for num in line.split()] for line in input.strip().split('\n')]
print(check_number_of_safe_reports(structured_input))



# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.


 













#  if row[0] > row[1]:
#             row.reverse()

#         for index in range(1, len(row)):
#             number_of_bad_levels = 0

#             if row[index] <= row[index -1]:
#                 number_of_bad_levels += 1

#             if abs(row[index] - row[index-1]) == 0 or abs(row[index]-row[index-1]) > 3:
#                 print(row, abs(row[index] - row[index-1]))
#                 number_of_bad_levels += 1


#             if number_of_bad_levels >= 1:
#                 print(number_of_bad_levels, "number_of_bad_levels")   
#                 number_of_unsafe_reports += 1
        