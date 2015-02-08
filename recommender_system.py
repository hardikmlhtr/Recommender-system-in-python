try:
    import numpy
except:
    print "This implementation requires the numpy module."
    exit(0)

'''
recommender_helper function takes parameters as original matrix, factor matrices U and V (initialized) and D: no. of feature vectors to consider
It is responsible for matrix factorisation using gradient descent method in which error between product of factors U and V and given matrix in minimized.
It return two vectors, U and V those are approximated factors of original matrix
'''
def recommender_helper(R, U, V, D):
    steps=5000									
    a=0.0002									
    b=0.02									
    V = V.T										

    for step in xrange(steps):
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(U[i,:],V[:,j])
                    for k in xrange(D):
                        U[i][k] = U[i][k] + a * (2 * eij * V[k][j] - b * U[i][k])
                        V[k][j] = V[k][j] + a * (2 * eij * U[i][k] - b * V[k][j])
        eR = numpy.dot(U,V)
        e = 0
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(U[i,:],V[:,j]), 2)
                    for k in xrange(D):
                        e = e + (b/2) * ( pow(U[i][k],2) + pow(V[k][j],2) )
        if e < 0.001:
            break
    return U, V.T

	
'''	
recommender function takes the parameter R, the original rating matrix with gaps as entry 0
ratings are in range(1,5). Original matrix's ith row consists of ratings given by ith user
Similarly jth column consists of ratings given to jth movie. So element Rij refer to the rating 
given to jth movie by ith user
'''
def recommender(R):
    R = numpy.array(R)

    N = len(R)
    M = len(R[0])
    D = 5


    U = numpy.random.rand(N,D)
    V = numpy.random.rand(M,D)

    nU, nV = recommender_helper(R, U, V, D)
    nR = numpy.dot(nU,nV.T) 
    print nR
