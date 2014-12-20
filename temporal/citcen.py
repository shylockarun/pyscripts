# import MySQLdb
import networkx as nx
import igraph as ig
# import MySQLdb.cursors
import traceback
import json
import pickle
from numpy import *
from datetime import datetime
import csv

# db = MySQLdb.connect("localhost","root","arun","btp",cursorclass=MySQLdb.cursors.DictCursor )
# cursor = db.cursor()

# sql = "select A,B,count as weight from coauthor_weighted "
# paper_list = []
# s = []
# results= []
# print("sql")
# print(str(datetime.now()))

# try:
    # cursor.execute(sql)
    # graph = ig.Graph.DictList(vertices=None, edges=cursor, edge_foreign_keys=('A', 'B'))
    # results = cursor.fetchall()
    # for row in results:
    	# paper_list.append((row['A'],row['B'],row['weight']))
# except Exception as e:
	# print ("EXIT")
	# print (e)
	# traceback.print_exc()
	# exit()
i=0
paper_list = []
for i in range(0,16):
	del paper_list[:]
	csvread = csv.reader(open('citation_weighted/cit_author_'+str(i)+'.csv','r'))
	csvwrite = csv.writer(open('citation_eigen/cit_author_'+str(i)+'.csv','w',newline=''))
	for row in csvread:
		paper_list.append((int(row[0]),int(row[1]),int(row[2])))

	# for row in paper_list:
		# if row[0] > row[1]:
			# print ("failed")
			# exit()
		# print(str(row))
	print ("add_weighted_edges_from")
	print(str(datetime.now()))

	###########################
	G=nx.DiGraph()
	G.add_weighted_edges_from(paper_list)
	# nx.write_weighted_edgelist(G,path="yo.txt")
	# print (paper_list)
	# exit()
	print ("centrality")
	print(str(datetime.now()))
	centrality=nx.eigenvector_centrality(G)
	print ("FILE DUMP")
	print(str(datetime.now()))
	# pickle.dump( centrality, open( "save.p", "wb" ) )
	# with open('file.txt', 'w') as f:
	for node in centrality:
		# f.write(str(node)+","+str(centrality[node])+"\n")
		csvwrite.writerow([node,centrality[node]])
	# 	for k, v in centrality:
	# 	    f.write(str(k)+","+str(v)+"\n")
	print("EXIT")
	print(str(datetime.now()))
# exit()
###########################
# print (graph.ecount())
# print (graph.vcount())

# el = graph.vs['name']
# deg = graph.degree()
# deg= graph.evcent()
# fout = open('coauthev.txt','w')
# for e, d in zip(el, deg):
    # fout.write(str(e)+","+str(d)+"\n")
# fout.close()
