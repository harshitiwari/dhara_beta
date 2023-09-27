from grid import ncp,copy
import grid
import compressible as cs
from derivative import *
import h5py
import math as math

import sys
sys.path.append("..")

import para

def simps1d(f,X):
    return ncp.sum((f[0:-2:2]+4*f[1:-1:2]+f[2::2])*(X[1]-X[0])/3)
    
def simps2d(f,X,Z):
    return simps1d(ncp.sum((f[:,0:-2:2]+4*f[:,1:-1:2]+f[:,2::2])*(grid.dz)/3,axis=1),X)
    
def total_mass():
    # Total mass
    if para.dim == 2:
        return simps2d(cs.rho,grid.X,grid.Z_mesh)
    
    elif para.dim == 1:
        return simps1d(cs.rho,grid.Z_mesh)
    
def total_kinetic_energy():
    # Total kinetic energy integral
    if para.dim == 2:
        return simps2d((cs.rho)*(1/2)*(cs.ux**2 + cs.uz**2),grid.X,grid.Z_mesh)
    
    elif para.dim == 1:
        return simps1d((cs.rho)*(1/2)*(cs.uz**2),grid.Z_mesh)

def total_internal_energy():
    # Total kinetic energy integral
    if para.dim == 2:
        return (grid.C/(para.gamma-1))*simps2d((cs.rho)**para.gamma,grid.X,grid.Z_mesh)
    
    elif para.dim == 1:
        return (grid.C/(para.gamma-1))*simps1d((cs.rho)**para.gamma,grid.Z_mesh)

def vrms():
    # V_rms volume average
    if para.dim == 2:
        return ncp.sqrt(simps2d((cs.ux**2 + cs.uz**2),grid.X,grid.Z_mesh))/(grid.Lx*para.Lz)
    
    elif para.dim == 1:
        return ncp.sqrt(simps1d((cs.uz**2),grid.Z_mesh))/para.Lz

def max_Mach_number():
    # Maximum Mach number
    if para.dim == 2:
        return ncp.max(ncp.sqrt((cs.ux**2+cs.uz**2)/(para.gamma*para.C*cs.rho**(para.gamma-1))))
    elif para.dim == 1:
        return ncp.max(ncp.sqrt((cs.uz**2)/(para.gamma*para.C*cs.rho**(para.gamma-1))))

def print_output(t):

    M_T = total_mass()
    Ke = total_kinetic_energy()
    Ie = total_internal_energy()
    V_rms = vrms()
    M = max_Mach_number()
    
    print(grid.dt_c, t, M_T, Ke, Ie, V_rms, M)

    if math.isnan(Ke):
        print ('# Try different parameters..Energy became infinity, code blew up at t = ', t)    
        sys.exit(1)

    pass

def save_fields(t):
    # Saving the fields

    parameters = ncp.array([para.gamma, para.C, para.dt])
    if para.dim == 2:
        hf1 = h5py.File(para.output_dir + "/fields/2D_%.2f.h5" % (t), 'w')
        if para.device == 'CPU':
            hf1.create_dataset('rho', data=cs.rho)
            hf1.create_dataset('ux', data=cs.ux)
            hf1.create_dataset('uz', data=cs.uz)
            hf1.create_dataset('parameters', data=parameters)
            hf1.close()
            pass
        else:
            hf1.create_dataset('rho', data=cs.rho.get())
            hf1.create_dataset('ux', data=cs.ux.get())
            hf1.create_dataset('uz', data=cs.uz.get())
            hf1.create_dataset('parameters', data=parameters.get())
            hf1.close()
            pass
        pass
    elif para.dim == 1:
        hf1 = h5py.File(para.output_dir + "/fields/1D_%.2f.h5" % (t), 'w')
        if para.device == 'CPU':
            hf1.create_dataset('rho', data=cs.rho )
            hf1.create_dataset('uz', data=cs.uz)
            hf1.create_dataset('parameters', data=parameters)
            hf1.close()
            pass
        else:
            hf1.create_dataset('rho', data=cs.rho.get())
            hf1.create_dataset('uz', data=cs.uz.get())
            hf1.create_dataset('parameters', data=parameters).get()
            hf1.close()
            pass
        pass
    pass