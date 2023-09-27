import sys
sys.path.append("..")
from para import *

if device == 'CPU':
    import numpy as ncp
    from numpy import copy
    
else:
    import cupy as ncp
    from cupy import copy

    dev = ncp.cuda.Device(device_rank)
    dev.use()

# ----------------------------- Time variables ----------------------------- #

dt_c = dt                                           # Courant time step
t = ncp.arange(tinit,tfinal+dt,dt_c)                # Time axis

Nf = int((tfinal-tinit)/t_f)                        # Number of field saving times
t_f_step = ncp.linspace(tinit,tfinal,Nf+1)          # Field saving times

Np = int((tfinal-tinit)/t_p)                        # Number of energies and other parameters printing saving times
t_p_step = ncp.linspace(tinit,tfinal,Np+1)          # Energies and other parameters printing saving times
    
# -------------------------------------------------------------------------- #

# ----------------------------- Grid variables ----------------------------- #

if dim == 2:
    Lx = A                                          # Length of box in x-direction

    dx = Lx/Nx                                      # Length between two consecutive grid points in x-direction
    dz = Lz/Nz                                      # Length between two consecutive grid points in z-direction         

    X = ncp.arange(0,Nx+1)*dx                       # Array consisting of points in x-direction
    Z = ncp.arange(0,Nz+1)*dz                       # Array consisting of points in z-direction
    
    X_mesh, Z_mesh = ncp.meshgrid(X, Z,indexing = 'ij')       # Meshgrids

    temp_dx = ncp.zeros_like(X_mesh)                # Temporary array for derivatives calcualtion and other purposes
    temp_dz = ncp.zeros_like(Z_mesh)                # Temporary array for derivatives calcualtion and other purposes
    pass

elif dim == 1:
    dz = Lz/Nz                                      # Length between two consecutive grid points in z-direction         
    Z_mesh = ncp.arange(0,Nz+1)*dz                  # Array consisting of points in z-direction
    temp_dz = ncp.zeros_like(Z_mesh)                # Temporary array for z-derivative
    pass

# -------------------------------------------------------------------------- #

# Printing parameters in output
print('# dim =', dim,', boundary_u_x =', boundary_u_x,', boundary_u_z =', boundary_u_z, ', Scheme =', Scheme)
print('\n# Nz =', Nz,', Nx =', Nx,', dt =', dt,', A =', A, ', gamma =', gamma,', C =', C)
print('\n \n# The following columns contains in order: dt, t, Total mass, Total kinetic energy, Total internal energy, Volume average V_rms, Maximum Mach number\n')