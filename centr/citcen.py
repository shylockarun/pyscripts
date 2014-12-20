import MySQLdb
import networkx as nx
import igraph as ig
import MySQLdb.cursors
import traceback
import json
# import pickle
# from numpy import *
from datetime import datetime
# import generators

def ResultIter(cursor, arraysize=100):
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for result in results:
            yield result

db = MySQLdb.connect("localhost","root","arun","btp",cursorclass=MySQLdb.cursors.DictCursor )
cursor = db.cursor()

sql = "select src,dest,weight from citation_weighted "
paper_list = []
s = []
results= []
print("sql")
print(str(datetime.now()))
G=nx.DiGraph()
count =0 
fout=open('pop.txt','w')
try:
    cursor.execute(sql)
    # results = cursor.fetchall()
    result = cursor.fetchmany(1000)
    while result:
        for row in result:
            fout.write(str(row['src'])+","+str(row['dest'])+","+str(row['weight']))
            paper_list=[(row['src'],row['dest'],row['weight'])]
            G.add_weighted_edges_from(paper_list)
        print (G.number_of_nodes())
        print ("count"+str(count))
        count+=1
        result = cursor.fetchmany(1000)

    # for row in ResultIter(cursor):
    #     # count+=1
    #     # print ("Results"+str(count))
    #     # for row in results:
    #     paper_list=[(row['src'],row['dest'],row['weight'])]
    #     G.add_weighted_edges_from(paper_list)
    #     print (G.number_of_nodes())
    #     # del paper_list[:]
    # print ("Rows Fetched")
    # for row in results:
    #     paper_list.append((row['src'],row['dest'],row['weight']))
    #     if len(paper_list) >=1000000:
    #         G.add_weighted_edges_from(paper_list)
    #         del paper_list[:]
    # G.add_weighted_edges_from(paper_list)
    # del results[:]
except Exception as e:
    print ("EXIT")
    print (e)
    traceback.print_exc()
    exit()

print ("add_weighted_edges_from")
print(str(datetime.now()))

###########################
del paper_list[:]
print ("centrality")
print(str(datetime.now()))
centrality=nx.eigenvector_centrality(G)
print ("FILE DUMP")
print(str(datetime.now()))
with open('citation.txt', 'w') as f:
    for node in centrality:
        f.write(str(node)+","+str(centrality[node])+"\n")
print("EXIT")
print(str(datetime.now()))
exit()