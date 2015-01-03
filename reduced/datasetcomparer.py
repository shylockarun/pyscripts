import csv
import matplotlib.pyplot as plt


csvread = csv.reader(open('final_author_coauthor.csv','r'))
csvread2 = csv.reader(open('final_author_percitation_bk.csv','r'))

paperlist = {}
paperlist2 = {}

for row in csvread: 
	paperlist[int(row[0])] = int(row[2])
	paperlist[int(row[1])] = int(row[2])

for row in csvread2: 
	paperlist2[int(row[0])] = int(row[2])

key1 = paperlist.keys()
key2 = paperlist2.keys()

print(len(key1))
print(len(key2))
diff = list(set(key2)-set(key1))

print (len(diff))
plot = []
for key in diff:
	plot.append(key)

plt.plot(plot,'b.')
# plt.hist(plot,bins=6)
plt.show()
