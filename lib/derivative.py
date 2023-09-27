from grid import ncp,copy
import grid

import sys
sys.path.append("..")

import para

def dfx(f):
    # Central difference of array 'f' w.r.t. x
    if para.boundary_u_x == 'PD':
        # For peridoic f
        grid.temp_dx[1:-1,:] = (f[2:,:] - f[:-2,:])/(2*grid.dx)
        # Boundary terms when f is periodic in x
        grid.temp_dx[0,:] = (f[1,:] - f[-2,:])/(2*grid.dx)
        grid.temp_dx[-1,:] = copy(grid.temp_dx[0,:])
        pass
    return grid.temp_dx

def dfz(f):
    
    # Central difference of array 'f' w.r.t. z
    if para.dim == 2:
        if para.boundary_u_z == 'PD':
            # For peridoic f
            grid.temp_dz[:,1:-1] = (f[:,2:] - f[:,:-2])/(2*grid.dz)
            # Boundary terms when f is periodic in z
            grid.temp_dz[:,0] = (f[:,1] - f[:,-2])/(2*grid.dz)
            grid.temp_dz[:,-1] = copy(grid.temp_dz[:,0])
            pass
        pass
    elif para.dim == 1:
        if para.boundary_u_z == 'PD':
            # For peridoic f
            grid.temp_dz[1:-1] = (f[2:] - f[:-2])/(2*grid.dz)
            # Boundary terms when f is periodic in z
            grid.temp_dz[0] = (f[1] - f[-2])/(2*grid.dz)
            grid.temp_dz[-1] = copy(grid.temp_dz[0])    
            pass
        pass
    return grid.temp_dz