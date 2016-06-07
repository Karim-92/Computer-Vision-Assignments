import cv2
import numpy as np
from PIL import Image


#First Image ada2.JPG
image=cv2.imread('ada2.jpg',0)
gaussianThreshOne=cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
medianThreshOne=cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imwrite("ada2 gaussian threshold.jpg", gaussianThreshOne)
cv2.imwrite("ada2 median threshold.jpg", medianThreshOne)


#Second Image Intensity.tif
img=cv2.imread('Intensity.jpg', 0)
gaussianThreshTwo=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)
medianThreshTwo=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 2)

cv2.imwrite("Intensity gaussian threshold.jpg", gaussianThreshTwo)
cv2.imwrite("Intensity median threshold.jpg", medianThreshTwo)

#It's best to use adaptive threshold when an Image has multiple varying illuminations as it gives better results.
#Global is best for Image with the same illuminations.
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()