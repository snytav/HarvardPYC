import numpy as np

def GetDensity(r, L, J):
    dx = L / J

    js = np.floor(r / dx) + 1
    js_ctrl = np.loadtxt('js.txt')
    eps = np.max(np.abs(js-js_ctrl))

    ys = r / dx - (js - 1)
    ys_ctrl = np.loadtxt('ys.txt')
    eps1 = np.max(np.abs(ys-ys_ctrl))

    js_plus_1 = np.mod(js, J) + 1
    js_plus_1_ctrl = np.loadtxt('js_plus_1.txt')
    eps2 = np.max(np.abs(js_plus_1_ctrl - js_plus_1))


    return 0