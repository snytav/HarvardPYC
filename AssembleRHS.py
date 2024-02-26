import numpy as np
from GetDensity import GetDensity

def AssembleRHS( solution_coeffs, L, J,N,t ):
    r = solution_coeffs[0:N]
    v = solution_coeffs[N:2*N]
    r = r + L*(r<0) - L*(r>L)
    #  Calculate electron number density
    ne = GetDensity( r, L, J,t )
    # Solve Poisson equation
    n0 = N/L
    rho = ne/n0 - 1
    from Poisson1D import Poisson1D
    phi = Poisson1D( rho, L)
    # Calculate electric field
    from electric import GetElectric
    E = GetElectric( phi, L,t )
    E_ctrl = np.loadtxt('E_' + '{:5f}'.format(t) + '.txt')
    eps_E = np.max(np.abs(E-E_ctrl))
    # equations of motion
    dx = L/J
    js = np.floor(r/dx).astype(int)
    js_ctrl = np.loadtxt('js_Eint_' + '{:5f}'.format(t) + '.txt')
    eps_js = np.max(np.abs(js+np.ones_like(js) - js_ctrl))
    ys = r/dx - js
    ys_ctrl = np.loadtxt('ys_Eint_' + '{:5f}'.format(t) + '.txt')
    eps_ys = np.max(np.abs(ys-ys_ctrl))
   # jsE_ctrl = np.loadtxt('js_E_int_' + '{:5f}'.format(t) + '.txt')
    js_plus_1_ctrl = np.loadtxt('js_plus_1_E_int_' + '{:5f}'.format(t) + '.txt')
    js_plus_1 = np.mod(js+1,J).astype(int)
   # diff_js = np.max(np.abs(js+1-jsE_ctrl))
    diff_js_plus_1 = np.max(np.abs(js_plus_1 + 1 - js_plus_1_ctrl))
    Efield = E[js]*(1-ys) + E[js_plus_1]
    Efield1_ctrl = np.loadtxt('Efield1_' + '{:5f}'.format(t) + '.txt')
    Efield2_ctrl = np.loadtxt('Efield2_' + '{:5f}'.format(t) + '.txt')
    eps_E1 = np.max(np.abs(E[js]*(1-ys)-Efield1_ctrl))
    eps_E2 = np.max(np.abs(E[js_plus_1]-Efield1_ctrl))
    Efield_ctrl = np.loadtxt('Efield_' + '{:5f}'.format(t) + '.txt')
    eps_E_long = np.max(np.abs(Efield_ctrl - Efield))
    rdot = v
    vdot = -Efield
    RHS = np.concatenate((rdot, vdot))
    RHS_ctrl = np.loadtxt('RHS_' + '{:5f}'.format(t) + '.txt')
    eps_RHS  = np.max(np.abs(RHS_ctrl - RHS))
    return RHS

