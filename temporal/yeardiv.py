import MySQLdb
import re
import string
import csv

csvwriters = []
csvwritersref = []
for i in range(0,16):
	csvwriters.append(csv.writer(open('auths/paper_author_'+str(i)+'.csv','w',newline='')))
	csvwritersref.append(csv.writer(open('refs/paper_ref_'+str(i)+'.csv','w',newline='')))


db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()
paperlist = {}
s = "select id, year from paper"
try:
	cursor.execute(s)
	result = cursor.fetchall()
	for row in result:
		year = row[1]
		if year <= 1998:
			paperlist[row[0]] = 0
		else: 
			paperlist[row[0]] = year-1998 
	# db.commit()
except:
	print( "failure")
	print( sql)
	exit()

s= "select paper_id,author_id from paper_author"

try:
	cursor.execute(s)
	result = cursor.fetchall()
	for row in result: 
		csvwriters[paperlist[row[0]]].writerow([row[0],row[1]])
except:
	print( "failure")
	print( sql)
	exit()


s= "select src_id,dest_id from paper_ref"

try:
	cursor.execute(s)
	result = cursor.fetchall()
	for row in result: 
		csvwritersref[paperlist[row[0]]].writerow([row[0],row[1]])
except:
	print( "failure")
	print( sql)
	exit()

# try:
# 	db.commit()
# except:
# 	print( "failure")
# 	exit()
# 	db.rollback()	
db.close()