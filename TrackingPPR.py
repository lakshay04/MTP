import numpy as np


class TrackingPPR:

    DAMPING_FACTOR = 0.85
    EPSILON = 0.001

    def __init__(self):
        pass

    def gauss_south_well(self, x, p):
        n = len(x)
        b = np.empty((n, 1), dtype=np.double)
        b.fill(1 / np.double(n))

        # calculating r from xnew - x
        r = (1 - self.DAMPING_FACTOR)*b - np.dot((np.identity(n) - self.DAMPING_FACTOR * p), x)

        while True:
            # index of max r
            i = np.argmax(r)

            if r[i] < self.EPSILON:
                return x

            ei = np.zeros((n, 1))
            ei[i][0] = 1

            # updating r and x
            x = x + r[i]*ei
            r = r - r[i]*ei + np.dot(self.DAMPING_FACTOR * r[i] * p, ei)

    def tracking_ppr(self, xinit, p):
        return self.gauss_south_well(xinit, p)


# for testing
if __name__ == '__main__':
    x = np.ones((4, 1), dtype=np.double)
    x.fill(1/np.double(4))
    p = np.array([[0, 0, 0.5, 0.5], [0.33, 0, 0, 0], [0.33, 0, 0, 0.5], [0.33, 1, 0.5, 0]],
                 dtype=np.double)

    tppr = TrackingPPR()
    x = tppr.gauss_south_well(x, p)
    print x
