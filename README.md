# dhara_beta
## Beta version of DHARA Compressible Flow Solver

- This is a sequential Python code which solves fully compressible equations for polytropic fluid in 2D Cartesian box. 
- This is GPU enabled. 

### Steps to run the code:
1. Go to `para.py` file for changing the parameters. 
  - To make it run on GPU, put GPU for `device` and its rank. 
  - Make a output directory where you want to store the fields and give its path to `output_dir`. 
  - You can change the time advance scheme from `Scheme`.
  - Put the grid parameters and control parameters.
2. To start the solver run `main.py` using Python. You can save the output in a text file using one of the following commands:
  - `python3 main.py > output\output.txt`
  - `nohup python3 main.py &> output\output.txt &`
