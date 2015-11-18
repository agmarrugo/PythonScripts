#! /usr/local/bin/python
# -*- coding: utf-8 -*-
"""
A script for processing whitelinesLink images
Created on Wed Sep 23 08:31:23 2015

@author: Andres Marrugo - andresmarrugo.net
"""
from __future__ import print_function
import numpy as np
from PIL import Image
import matplotlib.pylab as plt
from skimage.filters import threshold_otsu
from skimage.io import imread
from scipy import ndimage
import argparse


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("input",
	help="path to the input image file")
# ap.add_argument("output",
	# help="path to the input image file")
ap.add_argument("-o", "--output",
	help="path to the output image file")
args = vars(ap.parse_args())

if not(args['output']):
	args['output'] = args['input'].split('.')[0] + ".pdf"

# Read RGB image
# im = plt.array(Image.open(args['input']))
im = imread(args['input'])
height, width, channels = im.shape

# Read image as grayscale 
im_gray = plt.array(Image.open(args['input']).convert('L'))

# The masking works better if we first blur the gray scale image
im_gray = ndimage.gaussian_filter(im_gray, 3)

# Compute threshold using Otsu's method
thresh = threshold_otsu(im_gray)

# Compute mask - a fixed threshold of about 158 should also work.
mask = im_gray < thresh

# Create a white rgb image
rgb_image = np.ones((height,width,3), np.uint8)*255

# index with mask to assign only the pixels of interest
rgb_image[mask,0] = im[mask,0]
rgb_image[mask,1] = im[mask,1]
rgb_image[mask,2] = im[mask,2]

resultImage = Image.fromarray(rgb_image)
resultImage.save(args['output'],"PDF",Quality = 100)
print('Output saved at',args['output'])
