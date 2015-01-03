import MySQLdb
import csv

csvwriter= csv.writer(open('final_author_coauthor.csv','w',newline=''))
csvread = csv.reader(open('final_author_percitation_bk.csv','r'))

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()
authorlist = []
authorslist = {}
# countlist = {}
# for i in range(0,1232542):
	# authorlist[i] = -20000
	# countlist[i] = -20000/
for row in csvread:
	authorslist[int(row[0])] = 0
	# countlist[int(row[0])]=0

authorlist = set(authorslist.keys())

s= "select A,B,count from coauthor_weighted"
try:
	cursor.execute(s)
	result = cursor.fetchall()
	for row in result:
		if int(row[1]) in authorlist and int(row[0]) in authorlist:
			authorslist[int(row[0])] = 1
			authorslist[int(row[1])] = 1
			csvwriter.writerow([int(row[0]),int(row[1]),int(row[2])])
		# authorlist[int(row[1])]+=int(row[2])
		# authorlist[int(row[0])]+=int(row[2])
		# countlist[int(row[1])]+=1
		# countlist[int(row[0])]+=1
		# csvwriters[paperlist[row[0]]].writerow([row[0],row[1]])
except:
	print("failure")
	print(s)
	exit()

count = 0
for i in authorslist:
	if authorslist[i] == 0 :
		print( i)
