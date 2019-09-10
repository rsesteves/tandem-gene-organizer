import sys
import pandas as pd

reference = sys.argv[1]

r = open(reference, 'r')

print("Processing reference geneIDs...")

rf = pd.read_table(r,sep='\t',skiprows=0,usecols=[1,12],skipinitialspace=True)

df = rf.to_dict()
print("rf")
print(rf.head())

print("df")
print(df)
### Figure out how to remove the left handside column, and replace the spaces with a tab.
