import MySQLdb
import re
import string
import traceback
# f = open('publications.txt','rb')

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()
sql = "select paper_id,author_id from paper_author order by paper_id"
paper_list = []
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        paper_list.append([row[0],row[1]])
    # db.commit()
except Exception as e:
    print "failed OMG!"
    print e
    # db.rollback()
author_list = []
coauthors = []
save = 0

for paper in paper_list:
	if paper[0] != save:
		save = paper[0]
		del author_list[:]

	for author in author_list:
		coauthors.append([author,paper[1]])
	
	author_list.append(paper[1])

for coauthor in coauthors:
	sql_a = "insert into coauthor values(%d,%d)" % (coauthor[0],coauthor[1])
	try:
		# l=l+1
		cursor.execute(sql_a)
			# db.commit()
	except Exception as e:
		print "failure"
		print sql_a
		print e
		traceback.print_exc()
		exit()
try:
	db.commit()
except:
	print "failure"
	exit()
	db.rollback()	
db.close()
