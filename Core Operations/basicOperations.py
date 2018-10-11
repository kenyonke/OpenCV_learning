import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('1.jpg')

# We can access a pixel value by its row and column coordinates.
pixel = img[10,10]
print('RGB value in (10,10): ',pixel)

#Also, we can access RGB channel
B_pixel = img[10,10,0] # Remember! The mode of OpenCV is BGR
print('B value in (10,10):',B_pixel)

#modify the pixel value
img[10:100,10:100] = [0,0,0]

#Another way to access the pixel
print('Original R value: ',img.item(10,10,2)) #R channel
img.itemset((10,10,2),100) #change the R value in (10,10) to 100
print('Changed R value: ',img.item(10,10,2))

img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #color mode change
plt.imshow(img, cmap = 'Accent', interpolation = 'bicubic')

#Properties of the image
print('shape: ',img.shape)
print('size:', img.size)
print('dtype:', img.dtype)

#Image ROI
logo = img[870:1040,1670:1850]
img[0:170,0:180] = logo

#splitting and merging image channels
b,g,r = cv.split(img)
print(b)
print(g)
print(r)
img = cv.merge((g,r,b))
plt.imshow(img, cmap = 'Accent', interpolation = 'bicubic')

#Making Borders
replicate = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=[255,0,0])

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
