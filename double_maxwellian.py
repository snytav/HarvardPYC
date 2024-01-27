import numpy as np

def double_maxwellian(N,vb):
    v1 = np.random.normal(-1,vb-1,N/2)
    v2 = np.random.normalnormrnd(1,vb, N/2)
    v = np.concatenate((v1, v2))

    return v
