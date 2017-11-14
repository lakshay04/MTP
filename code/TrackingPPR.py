import numpy as np
from Log import *


class TrackingPPR:

    DAMPING_FACTOR = 0.85
    EPSILON = 0.0001

    def __init__(self):
        pass

    def gauss_south_well(self, x, p):
        iteration = 0
        n = len(x)
        b = np.empty((n, 1), dtype=np.double)
        b.fill(1 / np.double(n))

        # calculating r from xnew - x
        r = (1 - self.DAMPING_FACTOR)*b - np.dot((np.identity(n) - self.DAMPING_FACTOR * p), x)

        Log.i("gauss_south_well", "r="+str(r))

        while True:
            iteration += 1
            # index of max r
            i = np.argmax([abs(v) for v in r])

            if abs(r[i]) < self.EPSILON:
                return x, iteration

            ei = np.zeros((n, 1))
            ei[i][0] = 1

            # updating r and x
            x = x + r[i]*ei
            r = r - r[i]*ei + np.dot(self.DAMPING_FACTOR * r[i] * p, ei)

            # Log.i("gauss_south_well", "x="+str(x))

    def tracking_ppr(self, xinit, p):
        return self.gauss_south_well(xinit, p)


# for testing
if __name__ == '__main__':
    x = np.ones((4, 1), dtype=np.double)
    x.fill(1/np.double(4))
    p = np.array([
        [0, 0, 0.5, 0], [0.33, 0, 0, 0], [0.33, 0, 0, 0], [0.33, 1, 0.5, 0]],
                 dtype=np.double)

    # p = np.array([
    #     [0, 0, 0.5, 0, 0, 0, 0, 0],
    #     [0.33, 0, 0, 0.5, 0, 0, 0, 0],
    #     [0.33, 0, 0, 0, 0, 0, 0, 0],
    #     [0.33, 0.5, 0.5, 0, 0, 0, 0, 0],
    #     [0, 0.5, 0, 0, 0, 0.5, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 1, 0.5],
    #     [0, 0, 0, 0.5, 1, 0, 0, 0.5],
    #     [0, 0, 0, 0, 0, 0.5, 0, 0]],
    #     dtype=np.double)

    tppr = TrackingPPR()
    x = tppr.gauss_south_well(x, p)
    print x
