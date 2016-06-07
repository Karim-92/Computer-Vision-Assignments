import numpy as np 
import cv2

#Open the image & threshold it
imgOriginal=cv2.imread("Coins&pen.jpg", 0)
retval, img=cv2.threshold(imgOriginal, 0, 255, cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)

#Create a proper kernel to get the image without the coins and the image without the pen for processing
#Then apply opening to it
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
coinsImg=cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
penImg=img-coinsImg

#Open the pen image to get pen only
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
penImg = cv2.morphologyEx(penImg, cv2.MORPH_OPEN, kernel)

#Get the borders of the pen and the coins
penContours=cv2.findContours(penImg, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
coinContours=cv2.findContours(coinsImg, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

temp = int(len(penContours[0][0])/4)

#Put the text over the recognized parts in the original image
cv2.putText(imgOriginal, "Pen", tuple(penContours[0][0][temp][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 100)
cv2.putText(imgOriginal, "Coin", tuple(coinContours[0][0][15][0]), cv2.FONT_HERSHEY_PLAIN, 1, 0)
cv2.putText(imgOriginal, "Coin", tuple(coinContours[0][1][15][0]), cv2.FONT_HERSHEY_PLAIN, 1, 0)

cv2.imshow("Final Result", imgOriginal)
cv2.imwrite("Coins & Pen Identified.jpg", imgOriginal)
cv2.waitKey(0)
cv2.destroyAllWindows()
