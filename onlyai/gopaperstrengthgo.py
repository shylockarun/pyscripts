import csv
from collections import Counter
import networkx as nx

csvwrite = csv.writer(open('paper_strength.csv','w',newline=''))
csvread = csv.reader(open('paper_ref.csv','r'))

graphedges= []
for row in csvread:
	graphedges.append((int(row[0]),int(row[1])))

C = Counter(graphedges)

realgraphedges = []
for k in C:
	l,m = k
	realgraphedges.append((l,m,C[k]))

G= nx.Graph()

G.add_weighted_edges_from(realgraphedges)

centrality = nx.degree_centrality(G)

for node in centrality:
	csvwrite.writerow([node,centrality[node]])




