import numpy as np
import time


class GraphParams:

    P = None
    ADJACENCY_MATRIX = None
    N = None

    RECOMPUTE_PARAMS_REQUIRED = None

    def __init__(self, adjacency_matrix):
        self.ADJACENCY_MATRIX = adjacency_matrix[:]
        self.N = len(self.ADJACENCY_MATRIX)
        self.compute_params()
        self.RECOMPUTE_PARAMS_REQUIRED = False

    def compute_params(self):
        self.N = len(self.ADJACENCY_MATRIX)
        self.compute_p()
        self.RECOMPUTE_PARAMS_REQUIRED = False

    def compute_p(self):

        print "compute_p:start= ", time.clock()

        # calculating out degree
        out_degree = np.zeros(self.N, dtype=int)
        for j in range(0, self.N):
            for i in range(0, self.N):
                out_degree[i] += self.ADJACENCY_MATRIX[i][j]

        # computing P matrix
        self.P = np.zeros((self.N, self.N), dtype=np.double)
        for i in range(0, self.N):
            for j in range(0, self.N):
                if self.ADJACENCY_MATRIX[j][i] != 0:
                    self.P[i][j] = 1/np.double(out_degree[j])
                else:
                    self.P[i][j] = 0

        print "compute_p:end= ", time.clock()

    def update_p(self, vertices):

        out_degree = np.zeros(self.N)

        for j in vertices:
            for i in xrange(self.N):
                out_degree[j] += self.ADJACENCY_MATRIX[j][i]

        for j in vertices:
            for i in xrange(self.N):
                pass
            if self.ADJACENCY_MATRIX[j][i] != 0:
                self.P[i][j] = 1/np.double(out_degree[j])
            else:
                self.P[i][j] = 0

    def add_node(self, vertex_1):
        if self.len(ADJACENCY_MATRIX[0]) <= vertex_1:
            for i in range(0,vertex_1-1):
                self.ADJACENCY_MATRIX[i].append(0)
                self.P[i].append(0)
            r=np.zeros(vertex_1,dtype=np.double)
            s=np.zeros(vertex_1,dtype=int)
            self.ADJACENCY_MATRIX.append(s)
            self.P.append(r)
            self.RECOMPUTE_PARAMS_REQUIRED = True

    def add_edge(self, vertex_1, vertex_2):
        if self.ADJACENCY_MATRIX[vertex_1][vertex_2] == 0:
            self.ADJACENCY_MATRIX[vertex_1][vertex_2] = 1
            self.RECOMPUTE_PARAMS_REQUIRED = True

    def remove_edge(self, vertex_1, vertex_2):
        if self.ADJACENCY_MATRIX[vertex_1][vertex_2] != 0:
            self.ADJACENCY_MATRIX[vertex_1][vertex_2] = 0
            self.RECOMPUTE_PARAMS_REQUIRED = True

    def is_recompute_params_required(self):
        return self.RECOMPUTE_PARAMS_REQUIRED

    def get_p(self):
        return self.P

    def get_n(self):
        return self.N

    def get_adjacency_matrix(self):
        return self.ADJACENCY_MATRIX