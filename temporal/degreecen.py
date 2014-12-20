import networkx as nx
import traceback
import json
from numpy import *
from datetime import datetime
import csv

i=0
paper_list = []
authorlist = []
for i in range(0,16):
	del paper_list[:]
	csvread = csv.reader(open('coauth_weighted/co_author_'+str(i)+'.csv','r'))
	csvwrite = csv.writer(open('coauth_degree/co_author_'+str(i)+'.csv','w',newline=''))
	for row in csvread:
		paper_list.append((int(row[0]),int(row[1]),int(row[2])))
	G=nx.Graph()
	G.add_weighted_edges_from(paper_list)
	# centrality=nx.degree_centrality(G)
	centrality=dict((n,d) for n,d in G.degree_iter())
	for node in centrality:
		csvwrite.writerow([node,centrality[node]])
	print("EXIT")
	print(str(datetime.now()))

del authorlist[:]
for i in range(0,16):
	del paper_list[:]
	csvread = csv.reader(open('citation_weighted/cit_author_'+str(i)+'.csv','r'))
	csvwrite = csv.writer(open('citation_degree/cit_author_'+str(i)+'.csv','w',newline=''))
	for row in csvread:
		paper_list.append((int(row[0]),int(row[1]),int(row[2])))
	G=nx.DiGraph()
	G.add_weighted_edges_from(paper_list)
	# centrality=nx.indegree_centrality(G)
	centrality=dict((n,d) for n,d in G.in_degree_iter())
	for node in centrality:
		csvwrite.writerow([node,centrality[node]])
	print("EXIT")
	print(str(datetime.now()))