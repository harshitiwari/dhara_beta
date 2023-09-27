import numpy as np

device = "CPU"            # Use Target to set device as CPU or GPU                                        
device_rank = 5           # Set GPU device rank     
 
output_dir = 'output/run1/'     # Output directory

dim = 2                   # Dimension of system, 1, 2            
order = 1                 # Order of accuracy for forward and backward differences, 1, 2
eps = 1e-20

# NS: No-slip, FS: Free-slip, PD: Periodic
boundary_u_x = 'PD'       # Boundary condtions for velocity in horizontal or x-direction
boundary_u_z = 'PD'       # Boundary condtions for velocity in veritical or z-direction   

profile = 'static'        # Initial profiles; static: equilibrium profiles, continue: continue some run at time placed in tinit

Scheme = 'EULER'            # Time integration scheme, EULER

# ----------------------------- Grid parameters ---------------------------- #

tinit = 0                 # Initial time
tfinal = 1000             # Final time
dt = 1e-3                 # Single time step

dt_far = 1e-3             # dt after transient state
t_far = 0                 # Time after transient state

Lz = 2*np.pi              # Length of box in z-direction

Nz = 128                  # Number of grid points in z-direction
Nx = 128                  # Number of grid points in x-direction

# -------------------------------------------------------------------------- #

# --------------------------- Control parameters --------------------------- #

A = 1                     # Aspect ratio in x-direction
C = 0.001                 # Pressure equation constant
gamma = 1.3               # gamma = C_p/C_v 
Re = 1e3                  # Reynolds number

# -------------------------------------------------------------------------- #

# ---------------------------- Saving parameters --------------------------- #

# Keep N_fs in multiple of 2
N_fs = 8                  # Number of uniform z-surfaces for flux calculation 
 
t_f = 5                   # Field files saving time
t_p = 1e-2                # Energies and other parameters printing time

# -------------------------------------------------------------------------- #