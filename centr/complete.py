import MySQLdb
import re
import string
f = open('publications.txt','rb')

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()

# sql = "insert into paper values (1,'hi')"
count = 0
paper = ""
index = ""
year = ""
cat = ""
author = []
ref = []
authorlist = []
authmap = {}
l=0
for line in f:
	if line.startswith('#@'):
		line = line.strip('\r\n')
		authorlist.extend(line.strip('#@').split(','))
print len(authorlist)
authorlist = list(set(authorlist))
print len(authorlist)
author_id = 0
sql_a = []
for auth in authorlist:
	author_id+=1
	authmap[auth] = author_id
	sql_a = "insert into author values('%d',\"%s\")" % (int(author_id),auth.replace("\"","\\\"").replace("\\\\","\\"))
	try:
		# l=l+1
		cursor.execute(sql_a)
			# db.commit()
	except:
		print "failure"
		print sql_a
		exit()
# print authmap
# exit()
# keyword
f.seek(0)
for line in f:
	if line.startswith('#*'):
		line = line.strip('\r\n')
		paper = line.strip("#*")
		del ref[:]
		del author[:]
	if line.startswith('#t'):
		line = line.strip('\r\n')
		year = line.strip('#t')
	if line.startswith('#c'):
		line = line.strip('\r\n')
		cat = line.strip('#c')
	if line.startswith('#@'):
		line = line.strip('\r\n')
		author = line.strip('#@').split(',')
	if line.startswith('#%'):
		line = line.strip('\r\n')
		line = line.strip('#%')
		if line.isspace() == False:
			ref.append(line)
	if line.startswith('#index'):
		line = line.strip('\r\n')
		index = line.strip("#index")
	if line.startswith('#!'):
		# index = line.strip("#index")
		sql = []
		sql.append("insert into paper values ('%d',\"%s\",\"%s\",'%d')" % (int(index),paper.replace("\"","\\\"").replace("\\\\","\\"),cat.replace("\"","\\\"").replace("\\\\","\\"),int(year)) )
		# print ref
		for auth in author:
			sql.append("insert into paper_author values('%d','%d')" % (int(index),authmap[auth]))
		for refer in ref:
			sql.append("insert into paper_ref values('%d','%d')" % (int(index),int(refer)))
		# print str(sql)
		try:
			for s in sql:
				cursor.execute(s)
			# db.commit()
		except:
			print "failure"
			print sql
			exit()
			# db.rollback()		
# exit()			
try:
	db.commit()
except:
	print "failure"
	exit()
	db.rollback()	
db.close()