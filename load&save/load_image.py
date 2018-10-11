import cv2 as cv
from matplotlib import pyplot as plt

#load a image
img = cv.imread('1.jpg',1)
#1: load a color image
#0: load a gray image
#-1: load image as such 

#part 1: show image in cv
'''
#create a window with auto size for showing image 
cv.namedWindow('Miyuki',cv.WINDOW_AUTOSIZE)
#show the image
cv.imshow('Miyuki',img)

#waiting for users' operation
cv.waitKey(0) & 0xFF
#release windows
cv.destroyWindow('Miyuki') #or cv.destroyAllWindows()
'''


#part 2: show image in matplotlib
#matplotlib makes use of RGB mode, but opencv utilizes BGR mode!
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #color mode change
plt.imshow(img, cmap = 'Accent', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


#copy image
img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
copy_img = img.copy()

#save image
cv.imwrite("Miyuki_copy.jpg", copy_img, [int(cv.IMWRITE_JPEG_QUALITY), 5])  #compression level: 0-9 