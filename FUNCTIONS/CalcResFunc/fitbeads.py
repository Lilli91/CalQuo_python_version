# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:37:28 2017

@author: Liliana
"""

##=========================================================================
## CALQUO 2.0               
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

import numpy as np
from bpass import bpass

def fit_beads_corr(im, pixel_thresh,feature_threshmax,Lambda,feature_size):
    print('\n\n')
    print('%%================================%%\n') 
    print('Finding Features... \n')
    print('%%================================%%\n') 
    print('\n\n') 
        
    
    ##=========================================================================
    # Pre-filter image
    
    #PROBLE HERE!!! VALUES OF S ARE DIFFERENT FROM MATLAB
    s = bpass(im,Lambda,feature_size/2)
#    for i in range(0,20):
#        for j in range(0,20):
#            print (s[i,j]) #VALUES ARE NOT THE SAME OF MATLAB!!!

                    
    ##=========================================================================
    # Set image bit depth here:
        
#    h=float(s)
#    print (h)
#    h=sum(np.histogram(float(s),256),2)
#    h=np.cumsum(h)
#    h=h/max(h)
#    intmin = 1 + sum(h <  pixel_thresh)
        

    return s
    