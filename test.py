# -*- coding: utf-8 -*-
"""
Created on Tue May  2 13:58:41 2017

@author: Huw
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler
from matplotlib.pyplot import quiver

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

mpl.rc('figure',  figsize=(10, 6))
import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience

from skimage import io

#import jpype
#
#import pims
#import trackpy as tp
#import trackpy.predict

import time

path = 'C:/Users/Liliana/Desktop/Studio/PhD OXFORD 2016/Dominic Waithe/CalQuo/Data/calcium_test_29_9V/1G4 P18, biotin, HLA-9V.tif';

imagefull = io.imread(path)


# file read in in the format TZXY
# swap to XYZT
image_volume = np.swapaxes(imagefull,0,1)
image_volume = np.swapaxes(image_volume,1,2)


print (image_volume.shape)

plt.imshow(image_volume[:,:,1])
plt.xlabel ('X')
plt.ylabel ('Y')
plt.title ('First image of image series')

#define the size of the image volume + time-lapse
nX = image_volume.shape[0]
nY = image_volume.shape[1]
nT = image_volume.shape[2]

# plot the animated stack or time-lapse
fig = plt.figure()
#animate a certain slice in time
#ims = []
#i=1
#for j in range(nT):
#    im = plt.imshow(image_volume[:,:,1,j], cmap='viridis', animated=True)
#    ims.append([im])
    
#animate a certain frame in Z
ims = []
i=1
for j in range(nT):
    im = plt.imshow(image_volume[:,:,j], cmap='viridis', animated=True)
    ims.append([im])
    
# display the animation
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,repeat_delay=0)
plt.show()
