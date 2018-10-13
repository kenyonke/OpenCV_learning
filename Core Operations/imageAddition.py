# -*- coding: utf-8 -*-
import cv2 as cv
from matplotlib import pyplot as plt

#load
logo = cv.imread('opencv_logo.jpg')
miyuki = cv.imread('1.jpg')

'''
#resize for matching
row,col = logo.shape[:2]
print(row,col)
res_miyuki = cv.resize(miyuki,(col,row),interpolation=cv.INTER_CUBIC)
#blending
img = cv.addWeighted(logo,0.3,res_miyuki,1,0)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #color mode change
plt.imshow(img, cmap = 'Accent', interpolation = 'bicubic')
'''


#Bitwise
#put logo on the top-left of the photo
#if we add two photo together directly, it will change the color
row,col = logo.shape[:2]
roi = miyuki[:row,:col]

img2gray = cv.cvtColor(logo,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask) # the same effect of cv.THRESH_BINARY_INV, also, it can be seem as a boolean Not function(1-->0 and 0-->1)

miyuki_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
logo_fg = cv.bitwise_and(logo,logo,mask = mask)
# cv.bitwise_and(src1,src2,mask)
# dst = src1(I) and src2(I) if mask(I)!=0 

dst = cv.add(miyuki_bg,logo_fg)
miyuki[0:row,0:col] = dst

miyuki = cv.cvtColor(miyuki, cv.COLOR_BGR2RGB) #color mode change
plt.imshow(miyuki, cmap = 'Greys_r', interpolation = 'bicubic')
