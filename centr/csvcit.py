import MySQLdb
import networkx as nx
import igraph as ig
import MySQLdb.cursors
import traceback
import json
import csv
# import pickle
# from numpy import *
from datetime import datetime
# import generators

fin = open('citation_weighted.csv')
reader= csv.reader(fin)
count = 0
paper_list = []
G=nx.DiGraph()
for row in reader:
    # fout.write(str(row['src'])+","+str(row['dest'])+","+str(row['weight']))
    paper_list.append((int(row[0]),int(row[1]),int(row[2])))
    if count<5:
    	print (paper_list)
    elif count%1000000==0:
    	print (count)	
    count+=1

# print (G.number_of_nodes())
print ("count"+str(count))
# count+=1
# result = cursor.fetchmany(1000)

print ("add_weighted_edges_from")
G.add_weighted_edges_from(paper_list)

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