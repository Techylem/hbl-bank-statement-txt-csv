#0 Done - Skip first 8 lines
#1- Find comma and delete it 
#2. Replace "-" with space
#3.  Use regex and remove extra spaces
#4. Replace "|" with ","
#5. add " and " around the figures with character `

import os
import pandas as pd
import re
import csv
# Read data using pandas
idf = pd.read_fwf("sample.txt",skiprows=9, header=None,index_col=0)
df = pd.DataFrame(idf)
#df[df.0.str.contains(r'|')]
df=df.replace('-', '', regex=True)
df=df.replace(',', '', regex=True)
df=df.replace(' ', '', regex=True)
df=df.replace('|', ',', regex=True)
#df = re.sub(r"-", "", df)
print(df)
#write back
df.to_csv('out.csv',mode='w')