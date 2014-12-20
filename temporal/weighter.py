import csv
from collections import Counter
paperlist = []
for i in range(0,16):
    csvread = csv.reader(open('coauth/co_author_'+str(i)+'.csv','r'))
    csvwrite = csv.writer(open('coauth_weighted/co_author_'+str(i)+'.csv','w',newline=''))
    del paperlist[:]
    for row in csvread:
        # print (row[0])
        # print (row[1])
        # print (row[0]+','+row[1])
        if int(row[0])<int(row[1]):
            # print("lhlkhkh")
            paperlist.append(row[0]+','+row[1])
        else:
            # print ("yo")
            paperlist.append(row[1]+','+row[0])

    print (len(paperlist))
    papers = Counter(paperlist)

    print (len(papers))
    paperlist = list(set(paperlist))
    print (len(paperlist))
    # print(str(papers))
    for paper in papers:
        t = paper.split(',')
        count = papers[paper]
        csvwrite.writerow([t[0],t[1],count])