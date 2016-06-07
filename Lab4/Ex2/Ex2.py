import cv2
import numpy as np
from PIL import Image

#For the cameraman
im_gray = cv2.imread('cameraman.tif', 0)
(thresh, im_bw) = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print "Cameraman threshold: ",(thresh)
cv2.imwrite('Cameraman_BW.jpg', im_bw)


#For the coins
im_gray = cv2.imread('coins.png', 0)
(thresh, im_bw) = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print "Coins threshold: ",(thresh)
cv2.imwrite('Coins_BW.jpg', im_bw)

#For the answersheet
im_gray = cv2.imread('answersheet.png', 0)
(thresh, im_bw) = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print "Answersheet threshold: ",(thresh)
cv2.imwrite('answersheet_bw.jpg', im_bw)

#For the ada2 image
im_gray = cv2.imread('ada2.JPG', 0)
(thresh, im_bw) = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print "ada2 threshold: ",(thresh)
cv2.imwrite('ada2_BW.jpg', im_bw)