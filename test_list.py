import sys
import csv

# Annotation File Input1
reference = sys.argv[1]
# TandemCluster List Input
tclust = sys.argv[2]

r = open(reference, 'r')
t = open(tclust, 'r')

# Annotation File Processing (Achieve Column 1 and Column 2 (Gene Num + Gene Name)
rcsv = csv.reader(r, delimiter='\t')
ref_new = open('RefID.redundant', 'w+')

for i in rcsv:
  if len(i) >= 12:
    if type(i[12]) is not 'str':
      gene_num = i[1]
      gene_ID = i[12].strip() or '.'
      ref_new.write("%s\t%s\n" % (gene_num, gene_ID))
ref_new.close()

#Removing Duplicates in procRefID
lines_seen = set()
outfile = open("RefID.nonredundant", "w+")
for line in open("RefID.redundant", "r"):
  if line not in lines_seen:
    outfile.write(line)
    lines_seen.add(line)
outfile.close()

#Reference List Function
RefList = [line.strip().split('\t') for line in open("RefID.nonredundant", "r")]

#Cluster List Function
TandClustList = [i.strip().split(',') for i in t]

#To compare the  list (tandem clusters) to the dictionary (reference) line by line (Matching Function)
###
#Resulting Output
matchedRefClust = open('TandemClustID.txt', 'w+')

number = 0

for elemT in TandClustList:
  for elemR in RefList:
    if elemT[0] == elemR[0]:
      number += 1
      geneid = elemR[1]
      genenum = elemR[0]
      tandem = '\t'.join(elemT)
      matchedRefClust.write("ALY_TD_Cluster_%s\t%s\t%s\n" % (number, geneid, tandem))

# known geneIDs
mrc = [line.strip().split('\t') for line in open('TandemClustID.txt', 'r')]
known = []
for g in mrc:
  print(g)

# original cluster
all = []
for i in TandClustList:
  if i[0] != mrc:
print(all)

# output unknown clusters
unknown = []
for i in tcl:
  if i not in known[0]:
    unknown.append(i)

# adding unknown lines into TandemClustID file of interest.
with open('TandemClustID.txt', 'a') as tf:
  for i in unknown:
    number += 1
    tandem = '\t'.join(i)
    blank = "."
    tf.write("ALY_TD_Cluster_%s\t%s\t%s\n" % (number, blank, tandem))
    print("ALY_TD_Cluster_%s\t%s\t%s\n" % (number, blank, tandem))


