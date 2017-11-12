import numpy as np
from Log import *


class GraphParams:

    TAG = "GraphParams"

    P = None
    ADJACENCY_MATRIX = None
    N = None

    RECOMPUTE_PARAMS_REQUIRED = None

    def __init__(self, adjacency_matrix):
        self.ADJACENCY_MATRIX = adjacency_matrix[:]
        self.compute_params()

    def compute_params(self):
        self.N = len(self.ADJACENCY_MATRIX)
        self.compute_p()
        self.RECOMPUTE_PARAMS_REQUIRED = False

    def compute_p(self):

        Log.d(self.TAG, "compute_p: start")

        # calculating out degree
        out_degree = np.zeros(self.N, dtype=int)
        for j in range(0, self.N):
            for i in range(0, self.N):
                out_degree[i] += self.ADJACENCY_MATRIX[i][j]

        Log.i(self.TAG, "compute_p: \nout_degree="+str(out_degree))

        # computing P matrix
        self.P = np.zeros((self.N, self.N), dtype=np.double)
        for i in range(0, self.N):
            for j in range(0, self.N):
                if self.ADJACENCY_MATRIX[j][i] != 0:
                    self.P[i][j] = 1/np.double(out_degree[j])
                else:
                    self.P[i][j] = 0

        Log.i(self.TAG, "compute_p: \nself.P="+str(self.P))

        Log.d(self.TAG, "compute_p: end")

    # NOTE : not tested
    @DeprecationWarning
    def update_p(self, vertices):

        Log.d("update_p", "start")

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

        Log.d("update_p", "end")

    def add_node(self, vertex_new):

        Log.d(self.TAG, "add_node: start")

        if self.N == vertex_new:

            # incrementing N
            self.N += 1

            # updating self.P
            p_new = np.zeros((self.N, self.N), dtype=np.double)

            for i in xrange(self.N-1):
                p_new[i] = np.append(self.P[i], [0], axis=0)

            self.P = p_new

            # updating self.ADJACENCY_LIST
            # as self.ADJACENCY_LIST is [], we can append
            for i in xrange(0, self.N-1):
                self.ADJACENCY_MATRIX[i].append(0)

            # self.ADJACENCY_MATRIX is a [[]]
            self.ADJACENCY_MATRIX.append([0]*self.N)

            Log.i(self.TAG, "add_node: N=" + str(self.N))
            Log.i(self.TAG, "add_node: \nP="+str(self.P))
            Log.i(self.TAG, "add_node: \nAM="+str(self.ADJACENCY_MATRIX))
            return True
        else:
            Log.e(self.TAG, "add_node: invalid operation")
            return False

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 < self.N and vertex_2 < self.N:
            if self.ADJACENCY_MATRIX[vertex_1][vertex_2] == 0:
                self.ADJACENCY_MATRIX[vertex_1][vertex_2] = 1
                self.RECOMPUTE_PARAMS_REQUIRED = True
            Log.i(self.TAG, "add_edge: N=" + str(self.N))
            Log.i(self.TAG, "add_edge: \nP=" + str(self.P))
            Log.i(self.TAG, "add_edge: \nAM=" + str(self.ADJACENCY_MATRIX))
            return True
        else:
            Log.e(self.TAG, "add_edge: invalid operation")
            return False

    def remove_edge(self, vertex_1, vertex_2):
        if vertex_1 < self.N and vertex_2 < self.N:
            if self.ADJACENCY_MATRIX[vertex_1][vertex_2] != 0:
                self.ADJACENCY_MATRIX[vertex_1][vertex_2] = 0
                self.RECOMPUTE_PARAMS_REQUIRED = True
            return True
        else:
            Log.e(self.TAG, "remove_edge: invalid operation")
            return False

    def is_recompute_params_required(self):
        return self.RECOMPUTE_PARAMS_REQUIRED

    def get_p(self):
        return self.P

    def get_n(self):
        return self.N

    def get_adjacency_matrix(self):
        return self.ADJACENCY_MATRIX


# for testing
if __name__ == '__main__':
    am = [[0, 1, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 0, 1, 0]]
    gp = GraphParams(am)
    gp.add_node(3)
    gp.add_edge(0, 3)
    gp.add_edge(2, 3)
    gp.add_edge(1, 3)
    gp.add_edge(3, 2)
    gp.add_edge(3, 0)
    gp.compute_params()