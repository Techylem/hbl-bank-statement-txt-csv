# 0 Done - Skip first 8 lines
# 1- Find comma and delete it
# 2. Replace "-" with space
# 3.  Use regex and remove extra spaces
# 4. Replace "|" with ","
# 5. add " and " around the figures with character `

import os
import re
import csv
import numpy as np


def test(temp_x, temp_rows, skip_rows=9):
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


# def convert(lst):
#     return (lst.split('|'))
# Read data using pandas
f = open("sample.txt", "r", encoding='utf8')
# f=f.read()
str1 = f.readlines()[9:]
# print(str1)
# idf = pd.read_fwf("sample.txt", skiprows=9, header=None,index_col=0)
# df = pd.DataFrame(idf)
# df[df.0.str.contains(r'|')]
rows, do_stuff, str2 = 0, True, []
for x in str1:
    do_stuff, rows = test(x, rows)
    if do_stuff:
        continue
    x = re.sub("-", '', x)
    x = re.sub(',', '', x)
    x = re.sub('  ', '', x)
    x = x.replace('|', ',')
    x = re.sub('\n', '', x)
    print(x, end='\n')
    str2.append(x)
# df = re.sub(r"-", "", df)
# print(str2)
# write back
# using the save txt
# from the numpy module
np.savetxt("output.csv", str2, delimiter=", ", fmt='% s')
