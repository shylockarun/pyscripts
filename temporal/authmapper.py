import MySQLdb
import traceback
import csv

paper_list = []
coauthors = []
for i in range(0,16):
    csvread = csv.reader(open('auths/paper_author_'+str(i)+'.csv','r'))
    csvwriter = csv.writer(open('auths/co_author_'+str(i)+'.csv','w',newline=''))
    del paper_list[:]
    del coauthors[:]
    author_list = []
    for row in csvread:
        paper_list.append([row[0],row[1]])

    save = 0
    for paper in paper_list:
        if paper[0] != save:
            save = paper[0]
            del author_list[:]

        for author in author_list:
            coauthors.append([author,paper[1]])
        
        author_list.append(paper[1])
    
    for coauthor in coauthors:
        csvwriter.writerow([coauthor[0],coauthor[1]])


