# Things that have been done:
# 0. Skip first 9 rows
# 1. Replace commas with `
# 2. Replace "-" with space
# 3. Use regex and remove extra spaces
# 4. Replace "|" with ","
# 5. add " and " around the figures with character `
# 6. replace ` with ,
# 7. Join cells at the end and make a final csv
# 8. Account information added at the top
# 9. Minor bugs fixed

import re
import numpy as np

# Adding account info back as this was skipped earlier
def add_account_info(temp):
    file_handler = open("sample.txt", "r", encoding='utf8')
    temp_str = file_handler.readlines()[0:8]
    for var in reversed(temp_str):
        temp.insert(0, var)
    return temp

# Deleting/ Skipping repeated account info between two pages
def test(temp_x, temp_rows, skip_rows=10):
    # Start: Code for skipping {skip_rows} after every 'Continue on next Page' encountered!
    if 'Continue on next page' in temp_x:
        return True, temp_rows+1
    if 0 < temp_rows < skip_rows:
        temp_rows += 1
        return True, temp_rows
    if temp_rows == skip_rows:
        temp_rows = 0
        return True, temp_rows
    # End: Code for skipping {skip_rows} after every 'Continue on next Page' encountered!
    return False, 0

# Merging cells
def join_cells(input_str):
    str3 = []
    # Start: Code for generating a final string with joined cells
    concatenated_str = ""
    for i, temp in reversed(list(enumerate(input_str))):
        if ',' in temp:
            my_list = list(temp.split(','))
            if len(my_list[6]) > 1:
                my_list[3] += concatenated_str
                temp_str = ""
                for string in my_list:
                    temp_str += string + ','
                str3.insert(0, temp_str)
                concatenated_str = ""
            else:
                concatenated_str = my_list[3] + ' ' + concatenated_str
        else:
            str3.insert(0, temp)
    # End: Code for generating a final string with joined cells
    return str3


file = open("sample.txt", "r", encoding='utf8')
read_file = file.readlines()[9:]
file.close()
rows, allowed_work, working_str, final_str = 0, True, [], []
for line in read_file:
    allowed_work, rows = test(line, rows)
    if allowed_work:
        continue
    line = re.sub("-", '', line)
    line = re.sub(',', '', line)
    line = re.sub('  ', '', line)
    line = line.replace('|', ',')
    line = re.sub('\n', '', line)
    line = re.sub('  ', '', line)
    working_str.append(line)
final_str = join_cells(working_str)
final_str = add_account_info(final_str)
np.savetxt("output.csv", final_str, delimiter=", ", fmt='% s')
