from grid import ncp,copy
import grid
from derivative import *
import h5py

# Setting arrays initially in the memory

if para.dim == 2:
    # Velocity vector components
    ux = ncp.zeros([grid.Nx+1,grid.Nz+1])
    uz = ncp.zeros([grid.Nx+1,grid.Nz+1])

    # Scalar fields
    rho = ncp.zeros([grid.Nx+1,grid.Nz+1])
    T = ncp.zeros([grid.Nx+1,grid.Nz+1])

    # Conserved variables
    Q = ncp.zeros([3,grid.Nx+1,grid.Nz+1])
    F = ncp.zeros([3,grid.Nx+1,grid.Nz+1])
    
    temp = ncp.zeros([grid.Nx+1,grid.Nz+1])
    pass

elif para.dim == 1:
    # Velocity
    uz = ncp.zeros([grid.Nz+1])

    # Scalar fields
    rho = ncp.zeros([grid.Nz+1])
    T = ncp.zeros([grid.Nz+1])

    # Conserved variables
    Q = ncp.zeros([2,grid.Nz+1])
    F = ncp.zeros([2,grid.Nz+1])

    temp = ncp.zeros([grid.Nz+1])
    pass


def update_conserved():
    # Put the primitive variables inside Q's
    if para.dim == 2:
        Q[0] = copy(rho)
        Q[1] = rho*ux
        Q[2] = rho*uz
        pass
    elif para.dim == 1:
        Q[0] = copy(rho)
        Q[1] = rho*uz
        pass
    pass

def compute_convective_flux_x():
    # Convective flux terms in x-direction
    F[0] = rho*ux
    F[1] = rho*ux**2 + para.C*rho**para.gamma
    F[2] = rho*ux*uz
    pass

def compute_convective_flux_z():
    # Convective flux terms in z-direction
    if para.dim == 2:
        F[0] = rho*uz
        F[1] = rho*ux*uz
        F[2] = rho*uz**2 + para.C*rho**para.gamma
        pass
    elif para.dim == 1:
        F[0] = rho*uz
        F[1] = rho*uz**2 + para.C*rho**para.gamma
        pass
    pass

def compute_viscous_flux_x():
    # Viscous flux terms in x-direction

    # Computing tau_xx terms
    temp = copy(dfx(ux))
    F[1] -= (4/3)*para.Re*temp                                                              

    temp = copy(dfz(uz))
    F[1] += (2/3)*para.Re*temp                                                             

    # Computing tau_xz terms
    temp = copy(dfz(ux))
    F[2] -= para.Re*temp                                                            
    
    temp = copy(dfx(uz))
    F[2] -= para.Re*temp                                                             
    pass

def compute_viscous_flux_z():
    # Viscous flux terms in z-direction
    
    if para.dim == 2:
        # Computing tau_zz terms
        temp = copy(dfx(ux))
        F[2] += (2/3)*para.Re*temp                                         
            
        temp = copy(dfz(uz))
        F[2] -= (4/3)*para.Re*temp                                       

        # Computing tau_xz terms
        temp = copy(dfz(ux))
        F[1] -= para.Re*temp                                          

        temp = copy(dfx(uz))
        F[1] -= para.Re*temp                                     
        pass

    elif para.dim == 1:
        # Computing tau_zz terms
        temp = copy(dfz(uz))        
        F[1] -= (4/3)*para.Re*temp                                       
        pass

def flux_derivative_x():
    # Derivatives of total flux terms in x-direction
    F[0] = copy(dfx(F[0]))
    F[1] = copy(dfx(F[1]))
    F[2] = copy(dfx(F[2]))
    pass

def flux_derivative_z():
    # Derivatives of total flux terms in z-direction
    if para.dim == 2:
        F[0] = copy(dfz(F[0]))
        F[1] = copy(dfz(F[1]))
        F[2] = copy(dfz(F[2]))
        pass
    elif para.dim == 1:
        F[0] = copy(dfz(F[0]))
        F[1] = copy(dfz(F[1]))
        pass
    pass


