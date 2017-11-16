from OboInputTaker import *
import numpy as np

# for facebook 58234 for 30000 edges

batchSize = int(raw_input())
initialEdges = int(raw_input())
noOfEdges = int(raw_input())
am = np.zeros((noOfEdges, noOfEdges))
for i in xrange(noOfEdges):
    vals = str(raw_input()).split(" ")
    for j in xrange(len(vals)):
        am[i][j] = int(vals[j])
it = OboInputTaker(am, initialEdges, batchSize)
input_taker = it

break_flag = False

xx = input_taker.get_init()

while True:
    no_of_inputs = input_taker.get_input_no()
    output = ""
    output += str(no_of_inputs) + "\n"

    i = 0
    while i < no_of_inputs:

        # form v 1 OR e 2 3
        query_original = input_taker.get_input()
        query = query_original.split(" ")

        input_type = query[0]

        if input_type == 'e':
            i += 1
            output += query_original + "\n"

        elif input_type == 'n':
            i += 1
            output += query_original + "\n"

        elif input_type == 'x':
            i += 1
            output += query_original + "\n"
            break_flag = True
            break

    print output,

    if break_flag:
        break
