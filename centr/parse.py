import MySQLdb
import re
f = open('publications.txt','rb')

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()

# sql = "insert into paper values (1,'hi')"
count = 0
paper = ""
index = ""
year = ""
cat = ""
# keyword
for line in f:
	if line.startswith('#*'):
		paper = line.strip("#*")
	if line.startswith('#t'):
		year = line.strip('#t')
	if line.startswith('#c'):
		cat = line.strip('#c')

	if line.startswith('#index'):
		index = line.strip("#index")
		sql = "insert into paper values ('%d',\"%s\",\"%s\",'%d')" % (int(index),paper.replace("\"","\\\"").replace("\\\\","\\"),cat.replace("\"","\\\"").replace("\\\\","\\"),int(year)) 
		try:
			cursor.execute(sql)
			# db.commit()
		except:
			print "failure"
			print sql
			exit()
			# db.rollback()		
			
try:
	db.commit()
except:
	print "failure"
	# exit()
	db.rollback()	
db.close()