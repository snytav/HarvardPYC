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
    # equations of motion
    dx = L/J
    js = floor(r/dx)+1
    ys = r/dx - (js-1)
    js_plus_1 = mod(js,J)+1
    Efield = E[js]*(1-ys) + E[js_plus_1]
    rdot = v
    vdot = -Efield
    RHS = np.concatenate((rdot, vdot))
    return RHS

