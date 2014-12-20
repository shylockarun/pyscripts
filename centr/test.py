import MySQLdb
import networkx as nx
import igraph as ig
import MySQLdb.cursors
import traceback
import json
from numpy import *
from datetime import datetime

paper_list = [(1,2,2),(1,3,3),(1,4,3),(1,5,3),(1,6,4),(1,7,3),(1,8,2)]
G=nx.Graph()
G.add_weighted_edges_from(paper_list)
# nx.write_weighted_edgelist(G,path="yo.txt")
# print (paper_list)
# exit()
print ("centrality")
print(str(datetime.now()))
centrality=nx.eigenvector_centrality(G)
print ("FILE DUMP")
print(str(datetime.now()))
with open('file.txt', 'w') as f:
	f.write(json.dumps(centrality))
print("EXIT")
print(str(datetime.now()))
exit()