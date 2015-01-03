import MySQLdb
import csv
import traceback
import networkx as nx
import numpy

def pagerank(G, alpha=0.85, personalization=None,
             max_iter=100, tol=1.0e-10, nstart=None, weight='weight',
             dangling=None):
    """Return the PageRank of the nodes in the graph.
    G : graph
      A NetworkX graph.  Undirected graphs will be converted to a directed
      graph with two directed edges for each undirected edge.
    alpha : float, optional
      Damping parameter for PageRank, default=0.85.
    personalization: dict, optional
      The "personalization vector" consisting of a dictionary with a
      key for every graph node and nonzero personalization value for each node.
      By default, a uniform distribution is used.
    max_iter : integer, optional
      Maximum number of iterations in power method eigenvalue solver.
    tol : float, optional
      Error tolerance used to check convergence in power method solver.
    nstart : dictionary, optional
      Starting value of PageRank iteration for each node.
    weight : key, optional
      Edge data key to use as weight.  If None weights are set to 1.
    dangling: dict, optional
      The outedges to be assigned to any "dangling" nodes, i.e., nodes without
      any outedges. The dict key is the node the outedge points to and the dict
      value is the weight of that outedge. By default, dangling nodes are given
      outedges according to the personalization vector (uniform if not
      specified). This must be selected to result in an irreducible transition
      matrix (see notes under google_matrix). It may be common to have the
      dangling dict to be the same as the personalization dict.
    """
    if len(G) == 0:
        return {}

    if not G.is_directed():
        D = G.to_directed()
    else:
        D = G

    # Create a copy in (right) stochastic form
    W = nx.stochastic_graph(D, weight=weight)
    N = W.number_of_nodes()

    # Choose fixed starting vector if not given
    x = dict.fromkeys(W, 1.0 / N)
    
    p = dict.fromkeys(W, 1.0 / N)
    
    dangling_weights = p
    
    dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0]

    # power iteration: make up to max_iter iterations
    for _ in range(max_iter):
        # print('here')
        xlast = x
        x = dict.fromkeys(xlast.keys(), 0)
        danglesum = alpha * sum(xlast[n] for n in dangling_nodes)
        # print(danglesum)
        for n in x:
            # this matrix multiply looks odd because it is
            # doing a left multiply x^T=xlast^T*W
            for nbr in W[n]:
                x[nbr] += alpha * xlast[n] * W[n][nbr][weight]
            x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * p[n]
        # check convergence, l1 norm
        # err = sum([abs(x[n] - xlast[n]) for n in x])
        # if err < N*tol:
            # return x
    return x
    raise nx.NetworkXError('pagerank: power iteration failed to converge '
                        'in %d iterations.' % max_iter)




# csvwrite = csv.writer(open('final_author_degreecent.csv','w',newline=''))
coauthread = csv.reader(open('final_author_coauthor.csv','r'))
graphedges = []
count =0
for row in coauthread:
	count+=1
	if(count > 10):
		break
	graphedges.append((int(row[0]),int(row[1]),int(row[2])))
# print(len(graphedges))
G=nx.Graph()
print("fetched data")
G.add_weighted_edges_from(graphedges)
print("added edges")
print(len(G.edges()))
print(len(G.nodes()))
del graphedges[:]
centrality = pagerank(G)
# centrality = nx.degree_centrality(G)
# centrality=dict((n,d) for n,d in G.degree_iter())

print("centrality calculated")
for node in centrality:
	print(str(node)+','+str(centrality[node]))
	# csvwrite.writerow([node,centrality[node]])
