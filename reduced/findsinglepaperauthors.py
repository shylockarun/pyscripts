import MySQLdb
import csv

csvwriter= csv.writer(open('nosingle_author.csv','w',newline=''))

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()
authorlist = {}

for i in range(0,1232542):
	authorlist[i] = 0

s= "select paper_id,author_id from paper_author"

try:
	cursor.execute(s)
	result = cursor.fetchall()
	for row in result:
		authorlist[int(row[1])]+=1
except:
	print("failure")
	print(s)
	exit()

count = 0
for i in range(0,1232542):
	if authorlist[i] <2 :
		continue
	else:
		csvwriter.writerow([i,authorlist[i]])
		count+=1

print(count)