import numpy as np
import GraphParams
import TrackingPPR
import time

class Streamer:

    X = None
    TRACKING_PPR = None
    GRAPH_PARAMS = None

    def start(self):
        while True:
            no_of_inputs = int(raw_input("no of modifications: "))

            # no_of_inputs = '0'

            # if no_of_inputs == 's':
            #     break

            # if no_of_inputs == 'x':
            #     print self.X
            #     continue

            for i in range(0, int(no_of_inputs)):
                input_type = raw_input("a for add, r for remove: ")
                if input_type == 'a':
                    e_or_n = raw_input("edge(e) or node(n) :")
                    if e_or_n == 'e':
                        vertex_1,vertex_2 = int(raw_input("edge :").split(" "))
                        self.GRAPH_PARAMS.add_edge(vertex_1, vertex_2)
                    elif e_or_n == 'n':
                        vertex_1 = int(raw_input("vertex 1: "))
                        self.GRAPH_PARAMS.add_node(vertex_1)
                        self.X.append(1/vertex_1)
                elif input_type == 'r':
                    self.GRAPH_PARAMS.remove_edge(vertex_1, vertex_2)

            if self.GRAPH_PARAMS.is_recompute_params_required():
                print "changing"
                self.GRAPH_PARAMS.compute_params()
                self.compute_x()

            # print self.GRAPH_PARAMS.get_p()
            print "X = ", self.X
            # todo temp
            break

    def __init__(self, graph_params):
        self.TRACKING_PPR = TrackingPPR.TrackingPPR()
        self.GRAPH_PARAMS = graph_params
        self.X = np.zeros((graph_params.get_n(), 1), dtype=np.double)
        self.X.fill(1/np.double(graph_params.get_n()))
        self.compute_x()

    def compute_x(self):
        print "compute_x:start= ", time.clock()
        self.X = self.TRACKING_PPR.gauss_south_well(self.X, self.GRAPH_PARAMS.get_p())
        print "compute_x:end= ", time.clock()


# for testing
if __name__ == '__main__':
    noOfEdges = int(raw_input())
    am = np.zeros((noOfEdges, noOfEdges))
    # for i in xrange(noOfEdges):
    #     vals = str(raw_input()).split(" ")
    #     for j in xrange(len(vals)):
    #         am[i][j] = int(vals[j])
    gp = GraphParams.GraphParams(am)
    st = Streamer(gp)

# st.start()