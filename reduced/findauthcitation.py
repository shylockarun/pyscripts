import MySQLdb
import csv

csvwriter= csv.writer(open('final_author_citation.csv','w',newline=''))
csvread = csv.reader(open('final_author.csv','r'))

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()
authorlist = {}
backuplist = {}
for i in range(0,1232542):
	authorlist[i] = -40000

for row in csvread:
	authorlist[int(row[0])] = 0
	backuplist[int(row[0])] = [int(row[1]),int(row[2])]

s= "select dest,count from citation_count"

try:
	cursor.execute(s)
	result = cursor.fetchall()
	for row in result:
		authorlist[int(row[0])]+=int(row[1])
except:
	print("failure")
	print(s)
	exit()

count = 0
for i in range(0,1232542):
	if authorlist[i] <= 0 :
		continue
	else:
		csvwriter.writerow([i,backuplist[i][0],backuplist[i][1],authorlist[i]])
		count+=1

print(count)