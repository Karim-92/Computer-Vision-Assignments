import cv2
import numpy as np



def hitormiss(pos):
    #Opening the image and thresholding it
    utkImage=cv2.imread("b.tif",0)
    cv2.imwrite("b.jpg", utkImage)
    retval, utkThres=cv2.threshold(utkImage, 0, 255, cv2.THRESH_OTSU)

    #Use a user defined kernel to perform the hit or miss.
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (pos,pos))
    hitormissImg=cv2.morphologyEx(utkThres, cv2.MORPH_HITMISS, kernel)

    #Show the trackbar and the image
    cv2.imshow("Final Result", hitormissImg)
    cv2.imwrite("Final Image.jpg", hitormissImg)

hitormiss(1)
cv2.createTrackbar("Hit or miss: ", "Final Result", 0, 100, hitormiss)
cv2.waitKey(0)
cv2.destroyAllWindows()