import numpy as np

def GetElectric( phi, L,t ):
     # Calculate electric field from potential
     J = phi.shape[0]
     dx = L/J
     phi_ctrl = np.loadtxt('phi' + '{:5f}'.format(t) + '.txt')
     eps_phi = np.max(np.abs(phi_ctrl - phi))

     circ1_ctrl = np.loadtxt('circ1_' + '{:5f}'.format(t) + '.txt')
     circ1 = np.roll(phi, 1)
     circ2 = np.roll(phi, -1)
     eps_circ1 = np.max(np.abs(circ1_ctrl - circ1))
     circ2_ctrl = np.loadtxt('circ2_' + '{:5f}'.format(t) + '.txt')
     eps_circ2 = np.max(np.abs(circ2_ctrl - circ2))
     E = (circ1-circ2)/(2*dx)
     E_ctrl = np.loadtxt('E_' + '{:5f}'.format(t) + '.txt')
     eps_E = np.max(np.abs(E_ctrl - E))
     return E
