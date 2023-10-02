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
    cs.rho = copy(cs.Q[0])
    imposeBC_rho()

    cs.ux = cs.Q[1]/cs.rho
    cs.uz = cs.Q[2]/cs.rho
    imposeBC_u()
    pass

def time_advance_single_step(dt):
    # Q for single time step dt
    cs.compute_convective_flux_x()
    cs.flux_derivative_x()

    cs.Q -= dt*(cs.F)

    cs.compute_convective_flux_z()
    cs.flux_derivative_z()

    cs.Q -= dt*(cs.F)
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
        
        cs.update_conserved()
        time_advance_single_step(para.dt)
        update_primitive()

        t = t+para.dt
        pass
    pass
