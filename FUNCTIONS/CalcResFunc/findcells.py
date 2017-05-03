# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:16:32 2017

@author: Liliana
"""
import pylab as plt
import numpy as np


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
    
    
    # Bioformats read in tif
    # See https://pypi.python.org/pypi/python-bioformats
    
    import javabridge as jv
    import bioformats as bf
    from xml.etree import ElementTree as et
    import os
    import numpy as np
    
    jv.start_vm(class_path=bf.JARS)
    path = 'C:\Users\Liliana\Desktop\Studio\PhD OXFORD 2016\Dominic Waithe\CalQuo\Data\calcium_test_29_9V'
    os.chdir(path)
#    md = bf.get_omexml_metadata(TIFfile)
#    mdroot = et.fromstring(md.encode('utf-8'))
    
    
    
    rdr = jv.JClassWrapper('loci.formats.in.OMETiffReader')()
    rdr.setOriginalMetadataPopulated(True)
    clsOMEXMLService = jv.JClassWrapper('loci.formats.services.OMEXMLService')
    serviceFactory = jv.JClassWrapper('loci.common.services.ServiceFactory')()
    service = serviceFactory.getInstance(clsOMEXMLService.klass)
    metadata = service.createOMEXMLMetadata()
    rdr.setMetadataStore(metadata)
    rdr.setId(path)
    root = metadata.getRoot()
    first_image = root.getImage(0)
    pixels = first_image.getPixels()
    # The plane data isn't in the planes, it's in the tiff data
    for idx in range(pixels.sizeOfTiffDataList()):
        tiffData = pixels.getTiffData(idx)
        c = tiffData.getFirstC().getValue().intValue()
        t = tiffData.getFirstT().getValue().intValue()
        print "TiffData: c=%d, t=%d" % (c, t)
        
    
    
    
#    print mdroot   
#    print(mdroot[0].tag, mdroot[0].attrib)
  
    #im = bf.OMEXML(md)
    
    
    
    
    
    #THIS IS WORKING BUT IMAGE OUTPUT IS ZEROS
#    im = np.zeros((520,558,999), 'uint8')
#    for i in range(700,720):
#        im[:,:,i] = bf.load_image(TIFfile, c=None, z=0, t=i)  #should read as input name file and not path!!
#    #Does not read the time!!! only one frame!!!  --> for loop
#    
#    plt.imshow(im[:,:,705])
#    print im[:,:,705]
#    return im
    
    #Single colour loading

    
    
    #returnbioformats.load_image 
    
    
