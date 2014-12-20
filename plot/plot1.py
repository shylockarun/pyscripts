import csv
import matplotlib.pyplot as plt
import math

# f = open('degree_citation.txt', 'r')
# f = open('coauthor_eigenvalues.txt', 'r')
f = open('degree_coauth_normal_10.txt', 'r')
# f2 = open('degree_coauth_normal.txt', 'r')
f2 = open('degree_citation_normal_10.txt', 'r')

csvreader = csv.reader(f)
csvreader2 = csv.reader(f2)
plotdict = {}

for row in range(1,1232542):
	plotdict[row]=[0,0]

for row in csvreader:
	plotdict[int(row[0])][0] = (float(row[1]))
for row in csvreader2:
	plotdict[int(row[0])][1] = (float(row[1]))

f.close()
f2.close()

deglist = []
evlist = []
for row in range(1,1232542):
	if plotdict[row][0]==0 or plotdict[row][1] == 0:
		continue
	# if plotdict[row][0]>=0.2 or plotdict[row][1] >= 0.1:
		# continue	
	else:
		deglist.append(plotdict[row][0])
		evlist.append(plotdict[row][1])

plt.plot(evlist,deglist,'o')
# plt.plot(deglist,'ro')
plt.show()

