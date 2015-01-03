import csv
import itertools
from copy import deepcopy
from collections import defaultdict
csvread = csv.reader(open('paper_author.csv','r'))
csvwrite = csv.writer(open('coauthor.csv','w',newline=''))

parsed = ((int(row[0]),int(row[1]),int(row[2])) for row in csvread)

paperdict = defaultdict(list)
yeardict = {}
for k,v,m in parsed:
	yeardict[k] = m
	paperdict[k].append(v)

# print(str(paperdict.items()))
# print(str(yeardict))
for k,v in paperdict.items():
	p = list((list(x) for x in itertools.combinations(v,2)))
	for l in p:
		l.append(yeardict[k])
		l.append(k)
		csvwrite.writerow(l)

csvwrite = csv.writer(open('citation.csv','w',newline=''))
csvread = csv.reader(open('paper_ref.csv','r'))

# del parsed[:]
parsedagain = ((int(row[0]),int(row[1]),int(row[2])) for row in csvread)
# paperdict.clear()
yeardict.clear()
# print("here")
citdict = defaultdict(list)
yeardict = {}
for k,v,m in parsedagain:
	# print (k,v,m)
	yeardict[k] = m
	citdict[k].append(v)
	# print("here")

# 907571,908507,2001
# 907571,50,2001
# 907571,51,2001
# 908507,97,1997
# 908507,98,1997
# dic = deepcopy(paperdict)

for k,v in citdict.items():
	for dest in v:
		l = paperdict[k]
		m = paperdict[dest]
		for i in l:
			for j in m:
				# if k == 907571 and dest == 908507:
					# print(i)
					# print(j)
					# print(yeardict[k])
				csvwrite.writerow([i,j,yeardict[k],k])
	# p = list((list(x) for x in itertools.combinations(v,2)))
	# for l in p:
		# l.append(yeardict[k])
		# csvwrite.writerow(l)
