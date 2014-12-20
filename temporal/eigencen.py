import networkx as nx
import traceback
import json
from numpy import *
from datetime import datetime
import csv

i=0
paper_list = []
authorlist = []

def eigenvector_centrality_numpy(G):
    if len(G)==0:
        raise nx.NetworkXException(\
            "eigenvector_centrality_numpy(): empty graph.")

    A=nx.adj_matrix(G,nodelist=G.nodes())
    eigenvalues,eigenvectors=np.linalg.eig(A)
    # eigenvalue indices in reverse sorted order
    ind=eigenvalues.argsort()[::-1]
    # eigenvector of largest eigenvalue at ind[0], normalized
    largest=np.array(eigenvectors[:,ind[0]]).flatten()
    # norm=np.sign(largest.sum())*np.linalg.norm(largest)
    norm = 1
    centrality=dict(zip(G,largest/norm))
    return centrality


for i in range(0,16):
	del paper_list[:]
	csvread = csv.reader(open('coauth_weighted/co_author_'+str(i)+'.csv','r'))
	csvwrite = csv.writer(open('coauth_degree/co_author_'+str(i)+'.csv','w',newline=''))
	for row in csvread:
		paper_list.append((int(row[0]),int(row[1]),int(row[2])))
	G=nx.Graph()
	G.add_weighted_edges_from(paper_list)
	# centrality=nx.degree_centrality(G)
	# centrality=dict((n,d) for n,d in G.degree_iter())
	centrality = nx.eigenvector_centrality(G)

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
	# centrality=dict((n,d) for n,d in G.in_degree_iter())
	centrality = nx.eigenvector_centrality(G)

	for node in centrality:
		csvwrite.writerow([node,centrality[node]])
	print("EXIT")
	print(str(datetime.now()))