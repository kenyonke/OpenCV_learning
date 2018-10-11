# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#create a empty image
img = np.zeros(shape=(512,512,3),dtype = np.uint8)
plt.imshow(img, cmap = 'Accent', interpolation = 'bicubic')

#draw a white line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,255,255),5)
 # para2: start point, para3: end point, para4:line color, para5:thickness 

#draw a rectangle
cv.rectangle(img,(384,0),(510,150),(0,255,0),3)

#draw a circle
cv.circle(img,(447,63), 63, (0,0,255), -1)

#draw a ellipse
cv.ellipse(img,(256,256),(200,100),0,270,180,(255,255,255),-1)
#para1: center location
#para2: size
#para3: startAngle
#para4: endAngle
#para6: color

#draw a Polygon
pts = np.array([[20,5],[20,30],[200,20],[150,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(255,255,255))

#add text in image
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'Text', (100,500), font, 4, (255,255,255), 5, cv.LINE_AA)

plt.imshow(img, cmap = 'Accent', interpolation = 'bicubic')
