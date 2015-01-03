import csv
import math
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
import math
from collections import Counter 

def eigenvector(G,alpha=0.85, max_iter=100, tol=1.0e-6, nstart=None,
                           weight='weight'):
    from math import sqrt

    x = dict([(n,1.0/len(G)) for n in G])
    # normalize starting vector
    s = 1.0/sum(x.values())
    for k in x: 
      x[k] *= s
    nnodes = G.number_of_nodes()
    for i in range(max_iter):
      xlast = x
      x = dict.fromkeys(xlast, 0)
      for n in x:
        for nbr in G[n]:
          x[n] += alpha*xlast[nbr]*G[n][nbr].get(weight,1)/len(G[nbr])
            # x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
        x[n]+=(1-alpha)/len(G)
      # check convergence
      err = sum([abs(x[n]-xlast[n]) for n in x])
      if err < nnodes*tol:
        return x
    raise nx.NetworkXError("""eigenvector_centrality(): power iteration failed to converge in %d iterations."""%(i+1))


citread = csv.reader(open('citation.csv','r'))
coauthread = csv.reader(open('coauthor.csv','r'))
paperread = csv.reader(open('paper_strength.csv','r'))

parsedcit = ((int(row[0]),int(row[1]),int(row[2])) for row in citread)
parsedcoauth = ((int(row[0]),int(row[1]),int(row[2]),int(row[3])) for row in coauthread)
parsedpaper = dict((int(row[0]),float(row[1])) for row in paperread)

graphedges = ([] for x in range(0,16))
graphedges = list(graphedges)
authlist = ([[],[],[],[]] for x in range(0,43579))
authlist = list(authlist)


for i in range(1,43579):
  for j in range(0,16):
    authlist[i][0].append(0)  
    authlist[i][1].append(0)  
    authlist[i][2].append(0)  
    authlist[i][3].append(0)  
edgelist = []
for k,l,m in parsedcit:
  if m <= 1998:
    m = 0
  else:
    m = m - 1998
  authlist[l][0][m] += 1 
  edgelist.append((k,l))
  # authlist[l][0][0] += 1 

edgelist2 = []
for k,l,m,n in parsedcoauth:
  if m <= 1998:
    m = 0
  else:
    m = m - 1998
  # authlist[l][1][m] += 1 
  authlist[l][1][0] += 1 
  authlist[k][1][0] += 1 
  # authlist[k][1][m] += 1
  try:
    edgelist2.append((k,l,parsedpaper[n]))
  except KeyError:
    edgelist2.append((k,l,float(1.0e-08)))


dummylist = {}
for k,l,m in edgelist2:
  dummylist[(k,l)] = 0

for k,l,m in edgelist2:
  dummylist[(k,l)] += m

realedgelist2 = []
for row in dummylist:
  k,l  = row
  realedgelist2.append((k,l,dummylist[row]))

# C= Counter(edgelist2)
# realedgelist2 = []
# for row in C:
  # k,l = row
  # realedgelist2.append((k,l,C[row]))
# print(realedgelist2)

C2= Counter(edgelist)
realedgelist = []
for row in C2:
  k,l = row
  realedgelist.append((k,l,C2[row]))
# print(realedgelist)

# exit()
G=nx.Graph()
G.add_weighted_edges_from(realedgelist2)
centrality = nx.pagerank(G)
centrality2 = nx.degree_centrality(G)
# G2=nx.DiGraph()
# G2.add_edges_from(edgelist)
# centrality2 = nx.eigenvector_centrality(G2)
# G3 = nx.DiGraph()

list1 = []
list2 = []
for i in range(1,43579):
  if i in centrality.keys() and i in centrality2.keys():
    list1.append(centrality[i])
    list2.append(centrality2[i])

plt.plot(list1,list2,'b.')
plt.show()

exit()

color = 100000
colors =[]
for i in range(0,7):
  for j in range(0,10):
    color+=10
    colors.append(color)

colors = []
rangelimit = int(43579)
for i in range(1,rangelimit):
  color= '#'+str(hex(math.floor((i*(16777215 - 1048567))/rangelimit + 1048567))).strip('0x')
  while len(color) < 7:
    color = color +'0'

  colors.append(color)


exit()



timelessen = 1
G = nx.Graph()
for i in range(0,16):
  # G=nx.Graph()
  G.add_edges_from(graphedges[i])
  # print(len(G.nodes()))
  # print(len(G.edges()))
  # centrality = nx.eigenvector_centrality(G)
  centrality = eigenvector(G)
  for node in centrality:
    if i > 0:
      authlist[node][2][i] = centrality[node]
      # authlist[node][3][i] = centrality[node] - authlist[node][2][i-1]
      # authlist[node][2][i] = authlist[node][2][i-1]+centrality[node]
    else:
      authlist[node][2][i] = centrality[node]
  centrality=dict((n,d) for n,d in G.degree_iter())
  for node in centrality:
    authlist[node][3][i] = centrality[node]

rejectlist = []
nocoauthlist = []
small = []
for i in range(1,rangelimit):
  flag=True
  noco =True
  toosmall = False
  for j in range(0,16):
    if authlist[i][0][j]!=0: 
      flag=False
    if authlist[i][1][j]!=0: 
      noco=False
  if authlist[i][3][15]<4:
    toosmall = True
  if(flag):
    rejectlist.append(i)
  if(noco):
    nocoauthlist.append(i)
  if toosmall:
    small.append(i)

print(len(rejectlist)) #25050
print(len(nocoauthlist)) #2040
print(len(small)) # 4 29748
i=21123





plt.subplot(221)
# for i in range(1,rangelimit):
plt.plot(authlist[i][0],color=colors[i-1])
plt.subplot(222)
# for i in range(1,rangelimit):
plt.plot(authlist[i][1],color=colors[i-1])
plt.subplot(223)
# for i in range(1,rangelimit):
plt.plot(authlist[i][2],color=colors[i-1])
plt.subplot(224)
# for i in range(1,rangelimit):
plt.plot(authlist[i][3],color=colors[i-1])

plt.show()  
