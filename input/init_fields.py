import h5py
import sys
sys.path.append("..")
import para
sys.path.append("../lib")
from grid import ncp,copy
import grid
import compressible as cs

# Initial field profiles 
def init_fields():
    cs.rho = ncp.ones_like(grid.Z_mesh)
    cs.ux = 1e-2*ncp.sin(grid.X_mesh)*ncp.sin(grid.Z_mesh) 
    cs.uz = - 1e-2*ncp.cos(grid.X_mesh)*ncp.sin(grid.Z_mesh)   
    pass


