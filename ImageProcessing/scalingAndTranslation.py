# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:14:58 2018

@author: kenyon
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

logo = cv2.imread('opencv_logo.jpg')
width,height = logo.shape[:2]

#scalling
#Preferable interpolation methods are cv2.INTER_AREA for shrinking
#cv2.INTER_CUBIC (slow) and cv2.INTER_LINEAR(default) for zooming
re_logo = cv2.resize(logo,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
plt.imshow(re_logo, cmap = 'Accent', interpolation = 'bicubic')


#Translation
#trainslation is the shifting of object's lacation
#translation matrix M = [[1,0,tx],[0,1,ty]]
#where tx means the shifting in x axis and ty controls the y'shifting
#3th argument in cv2.warpAffine is the shape of output image (be care the row and col)
M = np.float32([[1,0,10],[0,1,10]])
dst = cv2.warpAffine(logo,M,(height,width))

plt.imshow(dst, cmap = 'Accent', interpolation = 'bicubic')
