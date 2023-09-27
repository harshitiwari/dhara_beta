import grid
import compressible as cs

import sys
sys.path.append("..")

import para

def imposeBC_u():
    # Boundary condition for velocity fields

    if para.dim == 2:     
        if para.boundary_u_x == 'PD' and para.boundary_u_z == 'PD':
            # Periodic boundary condition for velocity in x-direction and z-direction
            cs.ux[0,:] = cs.ux[-1,:]
            cs.uz[0,:] = cs.uz[-1,:]
            
            cs.ux[:,0] = cs.ux[:,-1] 
            cs.uz[:,0] = cs.uz[:,-1] 
            pass
        pass 

    elif para.dim == 1:
        if para.boundary_u_z == 'PD':
            # Periodic boundary condition for velocity
            cs.uz[0] = cs.uz[-1]
            pass
        pass
        
    pass

def imposeBC_rho():
    # Boundary condition for density

    if para.dim == 2:
        cs.rho[0,:] = cs.rho[-1,:]   
        cs.rho[:,0] = cs.rho[:,-1] 
        pass

    elif para.dim == 1: 
        cs.rho[0] = cs.rho[-1]
        pass

    pass

def boundary():
    imposeBC_rho()
    imposeBC_u()
    pass