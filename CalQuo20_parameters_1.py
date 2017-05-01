# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:16:24 2017

@author: Liliana
"""



def CalQuo_parameters():
    # Please edit parameters

    # CalQuo can read multiple files at different bit-numbers, pixel-sizes,
    # and framenumbers. 
    # Note, CalQuoAnalysis cannot process Files of different frame numbers yet.


    ## =========================================================================
    # Parameters software control

    # Define dictionary for the parameters
    PARAMETERS = {}
    
    # Define construct name: (default=name)

    PARAMETERS['dictname'] = "name"
            
    #Define framerate (default=0.5)
    PARAMETERS['framerate'] = 0.82
            
    # Define reference frame for feature identification (default=NumberImages)
    PARAMETERS['lastframenumber'] = 900
            
    ## =========================================================================
    # Parameters Profile control
            
    # Choose automated or manual frequency radius selection (auto 1 and manual 0)
    PARAMETERS['autoindex'] = 0
    
    # Determine the step-size in phase-diagram for automated frequency selection and radius computation
    PARAMETERS['Sensitivity'] = 0.001

    # Set Trigger radius for manual analysis
    PARAMETERS['Trigger_radius'] = 0.36
        
    # Choose normalisation of all data to ionomycin frame
    PARAMETERS['ionorm'] = 0

    # Define ionomycin frame for total global normalisation
    PARAMETERS['ioframe'] = 964

    # Compute minimum Treshhold for peak detection (default = 0.001)
    PARAMETERS['minTreshPeak'] = 0.002


    ## =========================================================================
    # Parameters feature recognition

    # Define expected feature size in pixel (default=15)
    PARAMETERS['feature_size'] = 6 #15

    # Define feature max size (default=20)
    PARAMETERS['subregion_size'] = 11 #19

    # Exclude 10% darkest cells: set threshmin=0.1 (default=0.1)
    PARAMETERS['feature_threshmin'] = 0.9 #15

    # Exclude 10% brightest cells: set threshmax=0.1 (default=0.1)
    PARAMETERS['feature_threshmax'] = 0.2


    ## =========================================================================
    # Parameters Distance Regularized Level Set for Image Segmentation

    # Feature detection in mode 1 or mode 0 (default=0)
    PARAMETERS['mode'] = 1

    # Defne minimal polygon radius size in pixel (default=5)
    PARAMETERS['iter_inner'] = 5
          
    # Defne maximal polygon radius size in pixel (default=20)
    PARAMETERS['iter_outer'] = 20
    
    return PARAMETERS