import sys
import csv

# Annotation File Input1
reference = sys.argv[1]
# TandemCluster List Input
tclust = sys.argv[2]

r = open(reference, 'r')
t = open(tclust, 'r')

# Annotation File Processing
rcsv = csv.reader(r, delimiter='\t')
reference = open('output.txt', 'w+')

try:
  for i in rcsv:
    gene_name = i[1]
    gene_num = i[12]
    # print ("%s\t%s" % (geneID, gene))
    reference.write("%s\t%s\n" % (gene_name, gene_num))
except IndexError:
  pass

#Reference (list)
RefList = [line.strip().split('\t') for line in open ("output.txt", "r")]

#Cluster (list)
TandClustList = [i.strip().split(',') for i in t]

#To compare the  list (tandem clusters) to the dictionary (reference) line by line (Matching Function)
###
#Resulting Output
matchedRefClust = open('output.final.txt', 'w+')

number = 0
for elemC in TandClustList:
  for elemR in RefList:
    if elemR[0] == elemC[0]:
      print(elemC[0]),
      print(elemR[0]),
      print(elemR[1])
      number += 1
      geneid = elemR[1]
      genenum = elemR[0]
      tandem = '\t'.join(elemC)
      matchedRefClust.write("ALY_TD_Cluster_%s\t%s\t%s\n" % (number, geneid, tandem))
