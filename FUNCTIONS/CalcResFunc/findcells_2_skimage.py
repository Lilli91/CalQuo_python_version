# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:16:32 2017

@author: Liliana
"""
import pylab as plt
import numpy as np
from fitbeads import fit_beads_corr

def findcells(TIFfile, PARAMETERS):
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
    
    
    ##========================================================================= 
    # Find cells and calculate intensities  
    ##=========================================================================    
    
    #NOT USING ATM
    # Bioformats read in tif
    # See https://pypi.python.org/pypi/python-bioformats

    #import javabridge as jv
    #import bioformats as bf
    #from xml.etree import ElementTree as et
    
    
    ## ---- Libraries ----
    import numpy as np
    import skimage
    from skimage import io
    import os #ask the current path
    import sys
    from skimage.util import img_as_float, img_as_ubyte
    from scipy import ndimage as ndi

    from cycler import cycle
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from cycler import cycler
    from matplotlib.pyplot import quiver
    
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.animation as animation
    
    mpl.rc('figure', figsize=(10, 6))
    import pandas as pd
    from pandas import DataFrame, Series  # for convenience

    ##=========================================================================
    # Read tif file
    im = io.imread(TIFfile).astype(np.uint8)
    
    # file read in in the format TZXY
    # swap to XYZT
    image_volume = np.swapaxes(im,0,1)
    image_volume = np.swapaxes(image_volume,1,2)
    
    #print (image_volume.shape)

    plt.imshow(image_volume[:,:,2])
    plt.xlabel ('X')
    plt.ylabel ('Y')
    plt.title ('First image of image series')

    
    #define the size of the image volume + time-lapse
    nX = image_volume.shape[0]
    nY = image_volume.shape[1]
    nT = image_volume.shape[2]
    
#    # plot the animated stack or time-lapse
#    fig = plt.figure()
#    #animate a certain slice in time
#    #ims = []
#    #i=1
#    #for j in range(nT):
#    #    im = plt.imshow(image_volume[:,:,1,j], cmap='viridis', animated=True)
#    #    ims.append([im])
#    
#    #animate a certain frame in Z
#    ims = []
#    i=1
#    for j in range(nT):
#        im = plt.imshow(image_volume[:,:,j], cmap='viridis', animated=True)
#        ims.append([im])
#        
#    # display the animation
#    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,repeat_delay=0)
#    plt.show()
#

    FinalImage = image_volume
    FinalImageOut = FinalImage 
    
    #print (image_volume[:,:,70]) #OK VALUES ARE THE SAME
    ##=========================================================================




    ##========================================================================= 
    # Find each cell using fitbeads.py and define a subregion around each cell
    
    Lambda=1;#should always be 1, length scale of poisson noise
    
    #PROBLEM HERE WITH VALUES
    r = fit_beads_corr(FinalImage[:,:,999],PARAMETERS['feature_threshmin'],PARAMETERS['feature_threshmax'],Lambda,PARAMETERS['feature_size'])
    
    ##========================================================================= 


    return 


    #Single colour loading

    
    
    #returnbioformats.load_image 
    
    
