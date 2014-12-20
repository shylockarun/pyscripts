import csv
import matplotlib.pyplot as plt
import math

cites = {}
coauths = {}
p=0.5
year = 0
for i in range(0,15):
	year= year+1
	csvread = csv.reader(open('citation_degree/cit_author_'+str(i)+'.csv','r'))
	for row in csvread:
		try:
			cites[int(row[0])] = cites[int(row[0])] + int(row[1])
		except KeyError:
			cites[int(row[0])] = int(row[1])
	
	csvread = csv.reader(open('coauth_degree/co_author_'+str(i)+'.csv','r'))
	for row in csvread:
		try:
			coauths[int(row[0])] = coauths[int(row[0])]*p + int(row[1])
		except KeyError:
			coauths[int(row[0])] = int(row[1])

xaxis = []
yaxis = []
count = 0
for key, value in coauths.items():
	try:
		if value <= 2 or cites[key] <= 2:
			raise Exception('spam', 'eggs')
		yaxis.append(cites[key])
		xaxis.append(value)
	except:
		pass
		# yaxis.append(0)
		# xaxis.append(value)
		# pass
		count+=1

print(count)
print (len(xaxis))
print (len(yaxis))
plt.plot(xaxis,yaxis,'o')
# plt.plot(deglist,'ro')
plt.show()
