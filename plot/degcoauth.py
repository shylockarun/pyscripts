import MySQLdb
import csv
from datetime import *
import traceback

db = MySQLdb.connect("localhost","root","arun","btp")
cursor = db.cursor()

sql = "select A,count(*),sum(count) from coauthor_weighted group by A order by count(*) limit 100000"
# maxdeg = 39384
sql2 = "select B,count(*),sum(count) from coauthor_weighted group by B order by count(*) limit 100000"
print("sql")
print(str(datetime.now()))
f = open('degree_coauth_10.txt', 'w',newline='')
f2 = open('degree_coauth_weight_10.txt', 'w',newline='')
f3 = open('degree_coauth_normal_10.txt', 'w',newline='')

csvwriter = csv.writer(f)
csvwriter2 = csv.writer(f2)
csvwriter3 = csv.writer(f3)
paper_list={}

for row in range(1,1232542):
	paper_list[row]=[0,0]
maxdeg = 1
maxwtsum = 1
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
    	paper_list[int(row[0])][0]=int(row[1])
    	paper_list[int(row[0])][1]=int(row[2])

    cursor.execute(sql2)
    results = cursor.fetchall()
    for row in results:
    	paper_list[int(row[0])][0]+=int(row[1])
    	paper_list[int(row[0])][1]+=int(row[2])
    	if paper_list[int(row[0])][0] > maxdeg:
    		maxdeg = paper_list[int(row[0])][0]
    	if paper_list[int(row[0])][1] > maxwtsum:
    		maxwtsum = paper_list[int(row[0])][1]
    
    # maxdeg = max(list(paper_list.values()))
    alpha = 0.5
    for row in range(1,1232542):
    	if paper_list[row][0]!=0:
    		csvwriter.writerow([row,paper_list[row][0]/maxdeg])
    		csvwriter2.writerow([row,paper_list[row][1]/maxwtsum])
    		csvwriter3.writerow([row,(1-alpha)*paper_list[row][0]/maxdeg+(alpha)*paper_list[row][1]/maxwtsum])

except Exception as e:
	print ("EXIT")
	print (e)
	traceback.print_exc()
	exit()

f.close()
f2.close()
f3.close()