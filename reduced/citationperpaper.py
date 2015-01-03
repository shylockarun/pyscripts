import MySQLdb
import csv
import traceback

csvwriter= csv.writer(open('final_author_percitation.csv','w',newline=''))
csvread = csv.reader(open('final_author.csv','r'))

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()
authorlist = {}
backuplist = {}
for i in range(0,1232542):
	authorlist[i] = [-40000,-40000]

for row in csvread:
	authorlist[int(row[0])] = [0,0]
	backuplist[int(row[0])] = [int(row[1]),int(row[2])] #all author and coauthor count

# authorlist = {}
citationlist = {} #paper citation count
s= "select paper_id,author_id from paper_author"
s2 = "select dest_id,count(*) FROM paper_ref group by dest_id"

try:
	cursor.execute(s2)
	result = cursor.fetchall()
	for row in result:
		citationlist[int(row[0])] = int(row[1])
except:
	print("failure")
	print(s2)
	exit()
k=0
# print((citationlist.keys()))
try:
	cursor.execute(s)
	result = cursor.fetchall()
	for row in result:
		if int(row[0]) in citationlist.keys():
			authorlist[int(row[1])][0] += 1
			authorlist[int(row[1])][1] += citationlist[int(row[0])]
			k+=1
except:
	print("failure")
	print(s)
	traceback.print_exc()
	exit()
print(k)
count = 0
for i in range(0,1232542):
	if authorlist[i][0] <= 0 :
		continue
	else:
		csvwriter.writerow([i,backuplist[i][0],backuplist[i][1],authorlist[i][0],authorlist[i][1],authorlist[i][1]/authorlist[i][0]])
		count+=1

print(count)