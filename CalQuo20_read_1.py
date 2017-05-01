# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:43:28 2017

@author: Liliana
"""


##=========================================================================
## CALQUO 2.0                -- MASTER-FILE --
##
##  Fritzsche Laboratory                                          June 2016
##
##=========================================================================

# Copyright (c) 2016 Fritzsche Laboratory
# 
# Permission is hereby granted, free of charge, to any person obtaining a 
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# CalQuo reads 8-bit files from the reference folder and then 
# identifies features at a distinct reference frame. Response funcitons are
# calculated from the first until last frame. Output is presented in RAWDATA.

# Note, feature and analysis parameters need to edited in the function
# CalQuo_parameters.m. Also, the framenumber for all files needs to be the
# same.

 


import Tkinter as tk
import tkFileDialog as filedialog
import os
import pylab as plt
import numpy as np
import glob
import time


# Function to clear all variables at the beginning
def clear_all():
    """Clears all the variables from the workspace of the spyder application."""
    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue
        if 'func' in str(globals()[var]): continue
        if 'module' in str(globals()[var]): continue

        del globals()[var]
if __name__ == "__main__":
    clear_all()
    
    
##=========================================================================
# Import functions
from CalQuo20_parameters_1 import CalQuo_parameters

import sys  
sys.path.append("./FUNCTIONS/CalcResFunc") 
from findcells import findcells


##=========================================================================
# Set main directory
root = tk.Tk()
root.withdraw()
Maindatapath = filedialog.askdirectory() 

if Maindatapath == 0:
    raise ValueError('No Main data directory is selected')
os.chdir(Maindatapath)

# Find tif-files in Maindatapath
for file in os.listdir("./"):
    if file.endswith(".tif"):
        fileList = glob.glob("*.tif")

    
##=========================================================================
# Load parameter file
PARAMETERS = CalQuo_parameters()
        

##=========================================================================
## RUN CALCULATIONS
##=========================================================================


tic = time.time() 

for k in range(0,len(fileList)):
    findcells(fileList[k], PARAMETERS)

toc = time.time()
print 'Time =', toc - tic



