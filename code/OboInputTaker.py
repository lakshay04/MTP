from collections import deque

class OboInputTaker:
    ADJACENCY_MATRIX = None
    NEW_NODE_FLAG = True
    CUR_N = None
    N = None
    Q = deque([])

    def __init__(self, adjacency_matrix):
        self.ADJACENCY_MATRIX = adjacency_matrix
        self.N = len(adjacency_matrix)
        self.CUR_N = 1
        self.Q.append((0, 1))
        self.Q.append((1, 1))
        self.Q.append((1, 0))

    def get_init(self):
        return [[self.ADJACENCY_MATRIX[0][0]]]

    def get_input_no(self):
        return 1

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
                        return self.get_input()
            else:
                deque.popleft(self.Q)
                self.Q.append((r, c + 1))

                if self.ADJACENCY_MATRIX[r][c] == 1:
                    return_str = "e "+str(r)+" "+str(c)
                    return return_str
                else:
                    return self.get_input()
        elif r == c:
            deque.popleft(self.Q)

            self.Q.append((r, c + 1))
            self.Q.append((r + 1, c + 1))
            self.Q.append((r + 1, c))

            if self.ADJACENCY_MATRIX[r][c] == 1:
                return_str = "e " + str(r) + " " + str(c)
                return return_str
            else:
                return self.get_input()
        else:
            if c == 0:
                self.NEW_NODE_FLAG = True

            deque.popleft(self.Q)

            self.Q.append((r + 1, c))

            if self.ADJACENCY_MATRIX[r][c] == 1:
                return_str = "e " + str(r) + " " + str(c)
                return return_str
            else:
                return self.get_input()


# for testing
if __name__ == '__main__':
    obj = OboInputTaker([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    print obj.get_init()
    while True:
        inp = obj.get_input()

        print inp

        if inp == "x":
            break