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

    if para.profile == 'static':
        # Static equilibrium profiles for temperature and density
        cs.rho = ncp.ones_like(grid.Z_mesh)

        if para.dim == 2:
            cs.ux = 1e-2*ncp.sin(grid.X_mesh)*ncp.sin(grid.Z_mesh) 
            cs.uz = - 1e-2*ncp.cos(grid.X_mesh)*ncp.sin(grid.Z_mesh)   
            pass

        elif para.dim == 1:
            cs.uz = - 1e-2*ncp.sin(grid.Z_mesh)
            pass

        pass

    elif para.profile == 'continue':
        # Continue previous run from some time, put it in para.tinit
        if para.dim == 2:
            with h5py.File(para.output_dir + "fields/2D_%.2f.h5" %(grid.tinit), "r") as f:
                # List all groups
                # print("Keys: %s" % f.keys())
                
                data_rho = list(f.keys())[1]
                data_ux = list(f.keys())[2]
                data_uz = list(f.keys())[3]

                # Get the data
                cs.rho = ncp.array(f[data_rho])
                cs.ux = ncp.array(f[data_ux])
                cs.uz = ncp.array(f[data_uz])
                pass
        pass

    pass


