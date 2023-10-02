import numpy as np

device = "CPU"            # Use Target to set device as CPU or GPU                                        
device_rank = 5           # Set GPU device rank     
 
output_dir = 'output/run1/'     # Output directory

Scheme = 'EULER'          # Time integration scheme, EULER

# ----------------------------- Grid parameters ---------------------------- #

tinit = 0                 # Initial time
tfinal = 100              # Final time
dt = 1e-3                 # Single time step

Lz = 2*np.pi              # Length of box in z-direction

Nz = 128                  # Number of grid points in z-direction
Nx = 128                  # Number of grid points in x-direction

# -------------------------------------------------------------------------- #

# --------------------------- Control parameters --------------------------- #

A = 1                     # Aspect ratio in x-direction
C = 0.001                 # Pressure equation constant
gamma = 1.3               # gamma = C_p/C_v 

# -------------------------------------------------------------------------- #

# ---------------------------- Saving parameters --------------------------- #

# Keep N_fs in multiple of 2
N_fs = 8                  # Number of uniform z-surfaces for flux calculation 
 
t_f = 5                   # Field files saving time
t_p = 1e-3                # Energies and other parameters printing time

# -------------------------------------------------------------------------- #