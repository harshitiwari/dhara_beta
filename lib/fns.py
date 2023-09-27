from grid import ncp,copy
import grid
import compressible as cs
from derivative import *
from boundary import *
from saving import print_output, save_fields
import h5py

import sys
sys.path.append("..")

import para

def update_primitive():
    # Update the primitive variables using Q's

    if para.dim == 2:
        cs.rho = copy(cs.Q[0])
        imposeBC_rho()

        cs.ux = cs.Q[1]/cs.rho
        cs.uz = cs.Q[2]/cs.rho
        imposeBC_u()
        pass

    elif para.dim == 1:
        cs.rho = copy(cs.Q[0])
        imposeBC_rho()

        cs.uz = cs.Q[1]/cs.rho
        imposeBC_u()
        pass

    pass

def CFL_condition():
    if para.dim == 2:
        dt_C = 0.5/ncp.max(ncp.abs(cs.ux)/grid.dx + ncp.abs(cs.uz)/grid.dz)
        pass
    elif para.dim == 1:
        dt_C = 0.5/ncp.max(ncp.abs(cs.uz)/grid.dz)
        pass
    grid.dt_c = min(para.dt,dt_C)
    pass

def time_advance_single_step(dt):
    # Q for single time step dt

    if para.dim == 2:
        cs.compute_convective_flux_x()
        # cs.compute_viscous_flux_x()
        cs.flux_derivative_x()

        cs.Q -= dt*(cs.F)

        cs.compute_convective_flux_z()
        # cs.compute_viscous_flux_z()
        cs.flux_derivative_z()

        cs.Q -= dt*(cs.F)
        pass
    
    elif para.dim == 1:
        cs.compute_convective_flux_z()
        # cs.compute_viscous_flux_z()
        cs.flux_derivative_z()

        cs.Q += -dt*(cs.F)
        pass

    pass

def time_advance_euler():
    # Time advance using Euler method, 1st order

    t = para.tinit
    j,k = 0,0

    while t <= para.tfinal+para.dt:
        if ((grid.t_p_step[j]-t)/para.dt) <= para.dt:
            print_output(t)
            j=j+1
            pass
        if ((grid.t_f_step[k]-t)/para.dt) <= para.dt:
            save_fields(t)
            k=k+1
            pass
        
        CFL_condition()

        cs.update_conserved()
        time_advance_single_step(grid.dt_c)
        update_primitive()

        t = t+grid.dt_c

        if t >= (para.t_far):
            para.dt = para.dt_far
            pass

        pass
    pass
