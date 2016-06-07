import numpy as np
import cv2
from matplotlib import pyplot as plt


#import the image to be processed
img = cv2.imread('sap.jpg',0)

#using a bilateral filter
Biblur = cv2.bilateralFilter(img,9,75,75)

#using blur (averaging filter)
blur = cv2.blur(img,(5,5))
#cv2.imwrite('sap Average filter.jpg',blur)

#using gaussian blur
Gblur = cv2.GaussianBlur(img,(5,5),0)
#cv2.imwrite('sap Gaussian Blur.jpg', Gblur)

#using median filter
Mblur=cv2.medianBlur(img,5)
#cv2.imwrite('sap Median.jpg',Mblur)

#stacking all results side by side and saving output
res = np.hstack((img,Biblur,blur,Gblur,Mblur))
cv2.imwrite('res.jpg',res)
