class RawInputTaker:

    ADJACENCY_MATRIX = None

    def __init__(self, adjacency_matrix):
        self.ADJACENCY_MATRIX = adjacency_matrix

    def get_init(self):
        return self.ADJACENCY_MATRIX

    def get_input_no(self):
        return raw_input()

    def get_input(self):
        return raw_input()
