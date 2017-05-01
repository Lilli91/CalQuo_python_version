from __future__ import division # Sets division to be float division
import feature2D
from PIL import Image
import tiff_file
import os
import numpy as np 
import matplotlib.pyplot as plt

def run(basepath, fname, fovn, numframes, featuresize, masscut=0, Imin=0, barI=None, barCc=None, barRg=None, IdivRg=None, field=2):  
    # This program should be used when you have determined the values of its
    # parameters using mpretrack_init. The calling sequence is
    # essentially the same. The features and found by calling feature2D (with
    # parameters other than feature size hardcoded).
    #
    # INPUTS:
    # basepath - The base path for the experiment. "fov#_times.mat" files
    #           should be there, and individual images should be in
    #           "fov#\fov#_####.tif"
    # fovn - ID# for the series of images (typically, one field of view)
    # featuresize - The size of the feature you want to find.
    # barrI - The minimum intensity you want to accept.
    # barrRg - The maximum Rg squared you want to accept.
    # barrCc - The maximum eccentricity you want to accept.
    # IdivRg - minimum ratio of Intensity/pixel to be accepted (integrated
    #           intensity / Rg squared of feature)
    # numframes - The number of images you have in your series
    # Imin - (optional) the minimum intensity for a pixel to be considered as a potential
    #           feature.
    # masscut - (optional) the masscut parameter for feature2D to remove false positives
    #           before rifining the position to speed up the code.
    # field - (optional) set to 0 or 1 if image is actually odd or even field of an interlaced 
    #           image. All the masks will then be constructed with a 2:1 aspect ratio. Otherwise 
    #           set to 2 for progressive scan cameras. Defaults to 2.
    #
    # Also, the program looks for the files "fov#_times.mat" for the "time"
    # variable and the images files "fov#\fov#_####.tif" from the basepath.
    #
    # OUTPUTS:
    #
    # Creates a file called "MT_featsize_#.npy" (# reperesents the featuresize input),
    # where it outputs the accepted features' MT matrix (from feature2D).
    #
    # MT matrix format:
    # 1 row per bead per frame, sorted by frame number then x position (roughly)
    # columns:
    # 1:2 - X and Y positions (in pixels)
    # 3   - Integrated intensity
    # 4   - Rg squared of feature
    # 5   - eccentricity
    # 6   - frame #
    # 7   - time of frame
    #
    # REVISION HISTORY
    # written by Paul Fournier and Vincent Pelletier (Maria Kilfoil's group),
    # latest revision 10/18/07
    # 10/26/07 Vincent -- commented out the Inv keyword, added a ratio of
    # Iint to Rg parameter
    # 12/21/07 Maria -- added optional field
    # Adapted for Python in June 2013
    
    path = os.path.join(basepath, 'fov' + str(fovn))
    pathout = path
    # if you would like to define a seperate pathout
    try:
        os.makedirs(pathout)
    except:
        pass
    
    times = np.load(os.path.join(path,"fov" + str(fovn) + "_times.npy"))
    strnam = os.path.join(basepath, fname)
    img_timeseries = tiff_file.imread(strnam)
    for x in xrange(1,numframes):
        img=img_timeseries[x,:,:]
       
        lnoise=1
        M = feature2D.feature2D(img,lnoise,featuresize,masscut,Imin,field);
        
        if len(M) != 0:
            if (x % 50) == 0: # prints the frame number every 50 timepoints
                print ('Frame ' + str(x))
            
            # The rejection process
            if barCc != None:
                X = (M[:,4] > barCc)
                M[X,:] = 0
            if barRg != None:
                X = (M[:,3] > barRg)
                M[X,:] = 0
            if barI != None:
                X = (M[:,2] < barI)
                M[X,:] = 0
            if IdivRg != None:
                X = (M[:,2]/M[:,3] < IdivRg)
                M[X,:] = 0
            
            M = M[(M[:,0] != 0).nonzero()[0],:]
            
            a = len(M[:,0])
            
            xv = np.array([x]*a)
            timev = np.array([times[x-1]]*a)
            
            M = np.hstack([M,(xv).reshape(len(xv),1),(timev).reshape(len(timev),1)])
            if x==1:
                MT = tuple(M)
                MT = np.array(M)
            else:
                MT = np.vstack([MT,M])
                
            print(str(a) + ' features kept.') 
            del img, M
    try:
        np.save(os.path.join(pathout,'MT_featsize_' +str(featuresize)),MT)
        return MT
    except:
        return None
     
#def test(basepath, fovn, frame, featuresize, masscut=0, Imin=0, barI=None, barRg=None, barCc=None, IdivRg=None, field=2):  
def test(basepath, fname, frame, featuresize, masscut=0, Imin=0, barI=None, barRg=None, barCc=None, IdivRg=None, field=2):  
    # This program should be used when you have determined the values of its
    # parameters using mpretrack_init. The calling sequence is
    # essentially the same. The features and found by calling feature2D (with
    # parameters other than feature size hardcoded).
    # INPUTS:
    print('')
    print('-----------TEST-----------')
    path = os.path.join(basepath, 'fov' + str(fovn))
    pathout = path
    # if you would like to define a seperate pathout
    try:
        os.makedirs(pathout)
    except:
        pass
    
    #strnam = os.path.join(path, "fov" + str(fovn) + "_%04d" %frame + '.tif')
    strnam = os.path.join(basepath, fname)
    #img = Image.open(strnam)
    #img = np.asarray(img)
    img_timeseries = tiff_file.imread(strnam)
    img=img_timeseries[frame,:,:]

    lnoise=1
    M = feature2D.feature2D(img,lnoise,featuresize,masscut,Imin,field);
    
    if len(M)==0:
        print('--------------------------')
        return None, None
    
    init = False
    Mrej = None
    
    # The rejection process
    if barI != None:
        X = (M[:,2] < barI)
        if init and len(X)>0:
            Mrej = np.vstack([Mrej,M[X,:]])
        elif len(X)>0:
            Mrej = M[X,:]
            init = True
        M[X,:] = 0
    if barRg != None:
        X = (M[:,3] > barRg)
        if init and len(X)>0:
            Mrej = np.vstack([Mrej,M[X,:]])
        elif len(X)>0:
            Mrej = M[X,:]
            init = True
        M[X,:] = 0
    if barCc != None:
        X = (M[:,4] > barCc)
        if init and len(X)>0:
            Mrej = np.vstack([Mrej,M[X,:]])
        elif len(X)>0:
            Mrej = M[X,:]
            init = True
        M[X,:] = 0
    if IdivRg != None:
        X = (M[:,2]/M[:,3] < IdivRg)
        if init and len(X)>0:
            Mrej = np.vstack([Mrej,M[X,:]])
        elif len(X)>0:
            Mrej = M[X,:]
            init = True
        M[X,:] = 0
    
    M = M[(M[:,0] != 0).nonzero()[0],:]
    
    implot=plt.imshow(img,'gray',interpolation='none')
    plt.axis('off');
    plt.plot(M[:,0],M[:,1],'go',markeredgecolor='g',markersize=2)
    if init:
        plt.plot(Mrej[:,0],Mrej[:,1],'ro',markeredgecolor='r',markersize=2)
    plt.show()
    
    MT = tuple(M)
    MT = np.array(M)
    
    a = len(M[:,0])   
    print(str(a) + ' features kept.') 
    if len(M) != 0:
        print('Minimum Intensity : ' + str(min(M[:,2])))
        print('Maximum Rg : ' + str(str(max(M[:,3]))))
        print('Maximum Eccentricity : ' + str(max(M[:,4])))
    print('--------------------------')

    return MT, Mrej