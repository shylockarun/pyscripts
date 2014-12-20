# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import iterparse, XMLParser
# from htmlentitydefs import name2codepoint
import MySQLdb

db = MySQLdb.connect("localhost","root","arun","btp" )
cursor = db.cursor()
sql = "select id,title,keyword from paper"
paper_list = []
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        paper_list.append([row[0],row[1].strip('\r\n'),row[2].strip('\r\n')])
    # db.commit()
except Exception as e:
    print "failed OMG!"
    print e
    # db.rollback()
db.close()
# print paper_list
print "LOG : DATABASE FETCH COMPLETE"
f = open('dblp.xml','rb')
fout = open('out.txt','wb')
count = 0
found = False  
article  = False
useless = False
store = []
titleno = 0
for line in f:

    if "<article" in line:
        article = True
        useless = False
        found = False
        store = []
        store.append(line)
        # print line
        continue
    if useless:
        continue
        # print line
    if "</article" in line:
        store.append(line)
        # print line
        for item in store:
            fout.write("%s" % item)
        article = False
        found = False
        useless = False

    if article and not found:
        if "<title" in line:
            count =0 
            for paper in paper_list:
                if paper[1] in line:
                    found = True
                    if titleno % 10000 == 0:
                        print titleno
                    titleno+=1
                    store.append('<index>'+str(paper[0])+'</index>\r\n')
                    store.append('<keyword>'+str(paper[2])+'</keyword>\r\n')
                    paper_list.pop(count)
                    break
                count+=1
            if not found:
                useless = True
        else:
            store.append(line)
    if article and found:
        store.append(line)   

fout.close()
f.close()             
        # print "yo"  
    # elif found == 1000:
        # if count < 10:
            # print line
        # else:
            # exit()
        # count+=1
	# if "OQL[C++]: Extending C++ with an Object Query Capab" in line:
            # print line

# parser = ET.XMLParser()
# parser.parser.UseForeignDTD(True)
# parser.entity.update((x, unichr(i)) for x, i in name2codepoint.iteritems())
# etree = ET.ElementTree()


# for event, article in ET.iterparse('dblp.xml', events = ('end', ),parser=parser):
# 	if article.tag == 'article':
# 	    for title in article.findall('title'):
# 	        print 'Title: {}'.format(title.txt)
# 	    for author in article.findall('author'):
# 	        print 'Author name: {}'.format(author.text)
# 	    for journal in article.findall('journal'):
# 	        print 'journal'
    	# article.clear()

    	# print article.find('url')
    	# print article.find('title')
    	# # print article
    	# for child in article:
    	# 	# print child.tag
    	# 	if child.tag == 'cite':
    	# 		print yo