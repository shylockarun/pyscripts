import MySQLdb
import traceback

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()

sql = "select paper_id,author_id from paper_author"
paper_list = {}
s = []
ref_list = []
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
    	try:
    		paper_list[row[0]].append(row[1])
    	except KeyError:
    		paper_list[row[0]]=[]
    		paper_list[row[0]].append(row[1])
    		continue
except:
	print ("EXIT")
	traceback.print_exc()
	exit()
print("SQL1 complete")
print(len(paper_list))

sql = "select src_id,dest_id from paper_ref"
results = []
try:
    cursor.execute(sql)
    results = cursor.fetchall()
except:
	traceback.print_exc()
	print ("EXIT")
	exit()
print("SQL2 complete")
print(len(results))
key = -1
for row in results:
	if key ==-8:
		break;
	for auth in paper_list[row[0]]:
		try:
			for auth2 in paper_list[row[1]]:
				s.append("insert into citation_order values('%d','%d')" % (auth,auth2))	
				print(str(row[0])+"->"+str(row[1])+" => "+str(auth)+"->"+str(auth2))
		except KeyError:
			paper_list[row[1]]=[]
			paper_list[row[1]].append(key)
			s.append("insert into citation_order values('%d','%d')" % (auth,key))	
			key -=1
			continue
print (len(s))
print(str(key))
exit()
try:
	for sq in s:
		cursor.execute(sq)
	# db.commit()
except:
	print ("failure")
	print (sq)
	exit()
print("SQL3 complete")

try:
	db.commit()
except:
	print ("failure")
	traceback.print_exc()
	exit()
	db.rollback()	
db.close()