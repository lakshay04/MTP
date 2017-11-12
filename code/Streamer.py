import numpy as np
import GraphParams
import TrackingPPR
from Log import *
from OboInputTaker import *


class Streamer:

    X = None
    TRACKING_PPR = None
    GRAPH_PARAMS = None

    def __init__(self, graph_params):
        self.TRACKING_PPR = TrackingPPR.TrackingPPR()
        self.GRAPH_PARAMS = graph_params
        self.X = np.zeros((graph_params.get_n(), 1), dtype=np.double)
        self.X.fill(1/np.double(graph_params.get_n()))
        self.compute_x()

    def start(self, input_taker):
        break_flag = False

        while True:
            no_of_inputs = input_taker.get_input_no()

            for i in range(0, no_of_inputs):

                # form v 1 OR e 2 3
                query = input_taker.get_input().split(" ")

                Log.exc("start", "query=" + str(query))

                input_type = query[0]

                if input_type == 'e':

                    vertex_1 = int(query[1])
                    vertex_2 = int(query[2])

                    done = self.GRAPH_PARAMS.add_edge(vertex_1, vertex_2)
                    Log.d("start", "edge1: done or not = "+str(done))

                elif input_type == 'n':

                    vertex_new = int(query[1])
                    done = self.GRAPH_PARAMS.add_node(vertex_new)

                    if done:
                        self.X = np.array(np.append(self.X, [[1]], axis=0))
                    Log.d("start", "new vertex: done or not = "+str(done))

                elif input_type == 'x':
                    break_flag = True

                else:
                    Log.e("start", "invalid input query="+str(query))

            if self.GRAPH_PARAMS.is_recompute_params_required():
                self.GRAPH_PARAMS.compute_params()
                self.compute_x()

            Log.i("start", "X = \n"+str(self.X))

            if break_flag:
                break

    def compute_x(self):
        if len(self.X) == 1:
            return
        time1 = time.clock()
        self.X = self.TRACKING_PPR.gauss_south_well(self.X, self.GRAPH_PARAMS.get_p())
        time2 = time.clock()
        print str(time2 - time1)


# for testing
if __name__ == '__main__':
    noOfEdges = int(raw_input())
    am = np.zeros((noOfEdges, noOfEdges))
    for i in xrange(noOfEdges):
        vals = str(raw_input()).split(" ")
        for j in xrange(len(vals)):
            am[i][j] = int(vals[j])
    it = OboInputTaker(am)
    gp = GraphParams.GraphParams(it.get_init())
    st = Streamer(gp)
    st.start(it)
