import numpy as np
import cv2

#read image to be processed
img = cv2.imread('pout.jpg',0)

#use equilize histogram method
equ = cv2.equalizeHist(img)

#stacking images side-by-side
res = np.hstack((img,equ)) 
cv2.imwrite('pout2.jpg',res)