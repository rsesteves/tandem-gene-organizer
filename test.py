import sys
import csv

# Annotation File Input1
reference = sys.argv[1]
# TandemCluster List Input
tclust = sys.argv[2]

r = open(reference, 'r')
t = open(tclust, 'r')

# Annotation File List
print("Reference geneIDs...\n")

rcsv = csv.reader(r, delimiter='\t')

for i in rcsv:
  colext = list(i[x] for x in [1,-1])

# Tandem Clust List
print("TandemCluster List Preview\n")

for i in t:
  tc = i.strip().split(',')
  print(tc)

# Matching Function
number = 0
for row in tc:
  for row1 in colext:
    for x in row:
      for y in row1:
	if y == x:
	  number += 1
          geneid = colext
          tandem = tc
          print("ALY_TD_Cluster_%s\t%s\t%s\n" % (number, geneid, tandem))
	  print(row)
	  print(row1)
print(colext)
