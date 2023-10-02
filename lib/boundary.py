import grid
import compressible as cs

import sys
sys.path.append("..")

import para

def imposeBC_u():
    # Boundary condition for velocity fields
    cs.ux[0,:] = cs.ux[-1,:]
    cs.uz[0,:] = cs.uz[-1,:]
    
    cs.ux[:,0] = cs.ux[:,-1] 
    cs.uz[:,0] = cs.uz[:,-1]    
    pass

def imposeBC_rho():
    # Boundary condition for density
    cs.rho[0,:] = cs.rho[-1,:]   
    cs.rho[:,0] = cs.rho[:,-1] 
    pass

def boundary():
    imposeBC_rho()
    imposeBC_u()
    pass