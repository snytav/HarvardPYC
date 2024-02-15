import numpy as np
from accum import accumarray

def GetDensity(r, L, J):
    dx = L / J

    js = np.floor(r / dx) + 1
    # js_ctrl = np.loadtxt('js.txt')
    # eps = np.max(np.abs(js-js_ctrl))

    ys = r / dx - (js - 1)
    ys_ctrl = np.loadtxt('ys.txt')
    # eps1 = np.max(np.abs(ys-ys_ctrl))

    js_plus_1 = np.mod(js, J) + 1
    js_plus_1_ctrl = np.loadtxt('js_plus_1.txt')
#    eps2 = np.max(np.abs(js_plus_1_ctrl - js_plus_1))

   # n1 = accumarray(js, (1 - ys) / dx, [J, 1]);
    n1_ctrl = np.loadtxt('n2_m.txt')
    ys_dx_ctrl = np.loadtxt('ys_dx.txt')
  # eps_ys = np.max(np.abs(ys_dx_ctrl - ys/dx))
    n1 = accumarray(js.astype(int)-1, ys/ dx)
    n1 = np.roll(n1, 1)
    #TODO^ make circular shift for n1
    eps3 = np.max(np.abs(n1_ctrl - n1))

    n21 = accumarray(js.astype(int)-1, (1 - ys) / dx)
    n22 = accumarray(js_plus_1.astype(int)-1, ys / dx)
    # n22 = np.roll(n22, 1)
    # n21 = np.roll(n21, 1)
    n2 = n21 + n22
    n2_ctrl= np.loadtxt('ne.txt')
    eps4 = np.max(np.abs(n2_ctrl - n2))


    return n2