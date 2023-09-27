import sys
import time 
sys.path.append("lib")
import para as para
import compressible as cs
from fns import time_advance_euler
from boundary import boundary
sys.path.append("input")
from init_fields import init_fields

ti = time.time()                    # Initial time

init_fields()                       # Initiating initial field profiles at initial time
boundary()                          # Boundary condition for initial field profiles                

if para.Scheme == 'EULER':
    time_advance_euler()            # Time advance steps using Euler method
    pass

tf = time.time()                    # Final time

print('# Total time of simulation = ', tf-ti)        # Time taken to run the code


