import csv
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
            paper_list[int(row[0])].append(row[1])
        except KeyError:
            paper_list[int(row[0])]=[]
            paper_list[int(row[0])].append(row[1])
            continue
except:
    print ("EXIT")
    traceback.print_exc()
    exit()
print("SQL1 complete")
print(len(paper_list))

# paper_list = []
coauthors = []
key = -1
for i in range(0,16):
    csvread = csv.reader(open('refs/paper_ref_'+str(i)+'.csv','r'))
    csvwriter = csv.writer(open('refs/cit_author_'+str(i)+'.csv','w',newline=''))
    for row in csvread:
        for auth in paper_list[int(row[0])]:
            try:
                for auth2 in paper_list[int(row[1])]:
                    csvwriter.writerow([auth,auth2])
                    # s.append("insert into citation_order values('%d','%d')" % (auth,auth2))   
                    # print(str(row[0])+"->"+str(row[1])+" => "+str(auth)+"->"+str(auth2))
            except KeyError:
                paper_list[int(row[1])]=[]
                paper_list[int(row[1])].append(key)
                csvwriter.writerow([auth,key])
                # s.append("insert into citation_order values('%d','%d')" % (auth,key)) 
                key -=1
                continue