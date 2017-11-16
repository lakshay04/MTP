from collections import deque


class OboInputTaker:
    ADJACENCY_MATRIX = None
    NEW_NODE_FLAG = True
    CUR_N = None
    N = None
    Q = None
    INITIAL_EDGES = None
    BATCH_SIZE = None

#74187
    def __init__(self, adjacency_matrix, initial_edges, batch_size=1):
        self.ADJACENCY_MATRIX = adjacency_matrix
        self.N = len(adjacency_matrix)
        self.CUR_N = 1
        self.INITIAL_EDGES = initial_edges
        self.BATCH_SIZE = batch_size
        self.reset()

    def reset(self):
        self.Q = deque([])
        self.Q.append((0, 1))
        self.Q.append((1, 1))
        self.Q.append((1, 0))

    def get_init(self):
        init_am = self.get_appropriate_init_am()
        return init_am

    def get_input_no(self):
        return self.BATCH_SIZE

    def get_input(self):
        curv = self.Q[0]
        r = curv[0]
        c = curv[1]

        if r == self.N or c == self.N:
            return "x"

        if r < c:
            if r == 0:
                if self.NEW_NODE_FLAG:
                    self.CUR_N += 1
                    self.NEW_NODE_FLAG = False
                    return "n "+str(self.CUR_N-1)
                else:
                    deque.popleft(self.Q)
                    self.Q.append((r, c + 1))

                    if self.ADJACENCY_MATRIX[r][c] == 1:
                        return_str = "e " + str(r) + " " + str(c)
                        return return_str
                    else:
                        return "r"
            else:
                deque.popleft(self.Q)
                self.Q.append((r, c + 1))

                if self.ADJACENCY_MATRIX[r][c] == 1:
                    return_str = "e "+str(r)+" "+str(c)
                    return return_str
                else:
                    return "r"
        elif r == c:
            deque.popleft(self.Q)

            self.Q.append((r, c + 1))
            self.Q.append((r + 1, c + 1))
            self.Q.append((r + 1, c))

            if self.ADJACENCY_MATRIX[r][c] == 1:
                return_str = "e " + str(r) + " " + str(c)
                return return_str
            else:
                return "r"
        else:
            if c == 0:
                self.NEW_NODE_FLAG = True

            deque.popleft(self.Q)

            self.Q.append((r + 1, c))

            if self.ADJACENCY_MATRIX[r][c] == 1:
                return_str = "e " + str(r) + " " + str(c)
                return return_str
            else:
                return "r"

    def get_appropriate_init_am(self):
        edges_count = 0

        while True:
            query = self.get_input().split(" ")
            input_type = query[0]

            if input_type == 'e':
                edges_count += 1
            elif input_type == 'x':
                break

            if edges_count == self.INITIAL_EDGES:
                maxv = max(int(query[1]), int(query[2]))
                return [[self.ADJACENCY_MATRIX[row][col] for col in xrange(maxv + 1)]
                        for row in xrange(maxv + 1)]

        return [[self.ADJACENCY_MATRIX[0][0]]]


# for testing
if __name__ == '__main__':
    obj = OboInputTaker([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 1)
    print obj.get_init()
    while True:
        inp = obj.get_input()

        print inp

        if inp == "x":
            break