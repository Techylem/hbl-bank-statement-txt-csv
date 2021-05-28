#0 Done - Skip first 8 lines
#1- Find comma and delete it 
#2. Replace "-" with space
#3.  Use regex and remove extra spaces
#4. Replace "|" with ","
#5. add " and " around the figures with character `

import os
import re
import csv
import numpy as np
# def convert(lst): 
#     return (lst.split('|')) 
# Read data using pandas
f=open("sample.txt","r", encoding='utf8')
#f=f.read()
str1=f.readlines()[9:]
#print(str1)
# idf = pd.read_fwf("sample.txt",skiprows=9, header=None,index_col=0)
# df = pd.DataFrame(idf)
#df[df.0.str.contains(r'|')]
str2=[]
for x in str1:
    x=re.sub("-", '',x)
    x=re.sub(',', '',x)
    x=re.sub('  ', '',x)
    x=x.replace('|', ',')
    x=re.sub('\n', '',x)
    # x=re.sub('||', '',x)
    # x=re.sub('|||', ',',x)
    print(x)
    str2.append(x)
#df = re.sub(r"-", "", df)
print(str2)
#write back
# using the savetxt 
# from the numpy module
np.savetxt("output.csv", 
           str2,
           delimiter =", ", 
           fmt ='% s')
#str2.to_csv('out.csv',mode='w')