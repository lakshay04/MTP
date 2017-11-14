from OboInputTaker import *
import numpy as np

noOfEdges = int(raw_input())
am = np.zeros((noOfEdges, noOfEdges))
for i in xrange(noOfEdges):
    vals = str(raw_input()).split(" ")
    for j in xrange(len(vals)):
        am[i][j] = int(vals[j])
it = OboInputTaker(am, 74187)
input_taker = it

break_flag = False

xx = input_taker.get_init()

while True:
    no_of_inputs = input_taker.get_input_no()
    output = ""
    output += str(no_of_inputs) + "\n"
    worth_it = False

    i = 0
    while i < no_of_inputs:

        # form v 1 OR e 2 3
        query_original = input_taker.get_input()
        query = query_original.split(" ")

        input_type = query[0]

        if input_type == 'e':
            worth_it = True
            output += query_original + "\n"

        elif input_type == 'n':
            worth_it = True
            output += query_original + "\n"

        elif input_type == 'x':
            worth_it = True
            output += query_original + "\n"
            break_flag = True

        i += 1

    if worth_it:
        print output,

    if break_flag:
        break
