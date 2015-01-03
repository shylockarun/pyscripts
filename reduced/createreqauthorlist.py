import MySQLdb
import csv

csvwriter= csv.writer(open('final_author.csv','w',newline=''))
csvread = csv.reader(open('nosingle_author.csv','r'))

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()
authorlist = {}
countlist = {}
for i in range(0,1232542):
	authorlist[i] = -20000
	countlist[i] = -20000
for row in csvread:
	authorlist[int(row[0])] = 0
	countlist[int(row[0])]=0

s= "select A,B,count from coauthor_weighted"

try:
	cursor.execute(s)
	result = cursor.fetchall()
	for row in result:
		authorlist[int(row[1])]+=int(row[2])
		authorlist[int(row[0])]+=int(row[2])
		countlist[int(row[1])]+=1
		countlist[int(row[0])]+=1
		# csvwriters[paperlist[row[0]]].writerow([row[0],row[1]])
except:
	print("failure")
	print(s)
	exit()

count = 0
for i in range(0,1232542):
	if authorlist[i] <2 :
		continue
	else:
		csvwriter.writerow([i,countlist[i],authorlist[i]])
		count+=1

print(count)