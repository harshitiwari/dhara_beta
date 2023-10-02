from grid import ncp,copy
import grid

import sys
sys.path.append("..")

import para

def dfx(f):
    # Central difference of array 'f' w.r.t. x
    # For peridoic f
    grid.temp_dx[1:-1,:] = (f[2:,:] - f[:-2,:])/(2*grid.dx)
    # Boundary terms when f is periodic in x
    grid.temp_dx[0,:] = (f[1,:] - f[-2,:])/(2*grid.dx)
    grid.temp_dx[-1,:] = copy(grid.temp_dx[0,:])
    return grid.temp_dx

def dfz(f):
    # Central difference of array 'f' w.r.t. z
    # For peridoic f
    grid.temp_dz[:,1:-1] = (f[:,2:] - f[:,:-2])/(2*grid.dz)
    # Boundary terms when f is periodic in z
    grid.temp_dz[:,0] = (f[:,1] - f[:,-2])/(2*grid.dz)
    grid.temp_dz[:,-1] = copy(grid.temp_dz[:,0])   
    return grid.temp_dz