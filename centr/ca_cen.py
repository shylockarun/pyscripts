import MySQLdb

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()

sql = "select A,B from coauthor"
paper_list = []
s = []
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
    	if row[0] < row[1]:
        	s.append("insert into coauthor_order values('%d','%d')" % (row[0],row[1]))	
        else:
        	s.append("insert into coauthor_order values('%d','%d')" % (row[1],row[0]))	
except:
	print "EXIT"
	exit()

print len(s)
try:
	for sq in s:
		cursor.execute(sq)
	# db.commit()
except:
	print "failure"
	print sq
	exit()

try:
	db.commit()
except:
	print "failure"
	exit()
	db.rollback()	
db.close()