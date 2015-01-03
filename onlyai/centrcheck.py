import networkx as nx


def pagerank(G, alpha=0.85, personalization=None,
             max_iter=100, tol=1.0e-10, nstart=None, weight='weight',
             dangling=None):
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
        print('here')
        print()
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
        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < N*tol:
            return x
    return x
    raise nx.NetworkXError('pagerank: power iteration failed to converge '
                        'in %d iterations.' % max_iter)

def eigenvector_centrality(G,alpha,beta, max_iter=100, tol=1.0e-6, nstart=None,
                           weight='weight'):
    from math import sqrt
    if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
        raise nx.NetworkXException("Not defined for multigraphs.")

    if len(G) == 0:
        raise nx.NetworkXException("Empty graph.")

    if nstart is None:
        # choose starting vector with entries of 1/len(G)
        x = dict([(n,1.0/len(G)) for n in G])
    else:
        x = nstart
    # normalize starting vector
    s = 1.0/sum(x.values())
    for k in x: 
        x[k] *= s
    nnodes = G.number_of_nodes()
    # make up to max_iter iterations
    for i in range(max_iter):
        # print("here")
        # print(x)
        xlast = x
        x = dict.fromkeys(xlast, 0)
        # visitedx = dict.fromkeys(xlast, 0)
        # do the multiplication y^T = x^T A
        
        for n in x:
            # count= 0
            for nbr in G[n]:
              # count = len(G[nbr])
              # if visitedx[nbr] == 0:
              # x[n]+=xlast[nbr]*G[n][nbr].get(weight,1)/count
              x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
            # x[n] = (x[n])*alpha
            # visitedx[n] = 1
            # print(x)
        # normalize vector
        # for n in x:
        #   if x[n] == 0:
        #     x[n] = xlast[n]
        # try:
        #     s = 1.0/sqrt(sum(v**2 for v in x.values()))
        # # this should never be zero?
        # except ZeroDivisionError:
            # s = 1.0
        # for n in x:
            # x[n] *= s
        # check convergence
        err = sum([abs(x[n]-xlast[n]) for n in x])
        print (err)
        if err < nnodes*tol:
            return x

    raise nx.NetworkXError("""eigenvector_centrality():
power iteration failed to converge in %d iterations."""%(i+1))


def eigenvector(G, max_iter=100, tol=1.0e-6, nstart=None,
                           weight='weight'):
    from math import sqrt
    if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
        raise nx.NetworkXException("Not defined for multigraphs.")

    if len(G) == 0:
        raise nx.NetworkXException("Empty graph.")

    if nstart is None:
        # choose starting vector with entries of 1/len(G)
        x = dict([(n,1.0/len(G)) for n in G])
    else:
        x = nstart
    # normalize starting vector
    s = 1.0/sum(x.values())
    for k in x: 
        x[k] *= s
    nnodes = G.number_of_nodes()
    # make up to max_iter iterations
    for i in range(max_iter):
        print(x)
        xlast = x
        x = dict.fromkeys(xlast, 0)
        
        for n in x:
            for nbr in G[n]:
              x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
        # normalize vector
        try:
          s= 1.0/(sum(v for v in x.values()))
          s = 1.0/sqrt(sum(v**2 for v in x.values()))
        # this should never be zero?
        except ZeroDivisionError:
            s = 1.0
        for n in x:
            x[n] *= s
        # check convergence
        err = sum([abs(x[n]-xlast[n]) for n in x])
        print (err)
        if err < nnodes*tol:
            return x

    raise nx.NetworkXError("""eigenvector_centrality():
power iteration failed to converge in %d iterations."""%(i+1))


edgelist = [(1,2),(2,3),(2,4),(4,5),(4,7),(5,6),(4,8),(8,6)]
edgelist = [(1,2),(2,3),(3,4),(4,5),(3,6),(3,5),(6,5)]
# edgelist = [(1,2),(2,3),(3,4),(4,5)]
G = nx.Graph();
G.add_edges_from(edgelist)
centrality = eigenvector(G)
centrality2 = nx.eigenvector_centrality(G)
print(centrality2)
print(centrality)

