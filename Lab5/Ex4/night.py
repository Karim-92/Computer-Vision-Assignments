import numpy as np
import cv2

#Read the image and the background image, then threshold the image
imgRGB = cv2.imread("1.jpg")
OriginalImage = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2GRAY)

#Read the background image, changing the night(n) to 1-5 changes the background
background = cv2.imread("night2.jpg")
retval, imgThresh = cv2.threshold(OriginalImage, 230, 255, cv2.THRESH_BINARY)

#Prepare a kernel of 3*3 then open the image with it
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
imgOpened = cv2.morphologyEx(imgThresh, cv2.MORPH_OPEN, kernel)

#Dilate the image to fill the white parts
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (29,29))
imgDilated = cv2.dilate(imgOpened, kernel)
background = cv2.resize(background, (imgOpened.shape[1], imgOpened.shape[0]))

#Convert the image to greyscale
ones = np.where(imgDilated != 0)
indices = zip(ones[0], ones[1])
imgDilated = cv2.cvtColor(imgDilated, cv2.COLOR_GRAY2RGB)

#Set the colors of the pixels
for i in indices:
    imgDilated.itemset((i[0], i[1], 0), 1)
    imgDilated.itemset((i[0], i[1], 1), 1)
    imgDilated.itemset((i[0], i[1], 2), 1)

    imgRGB.itemset((i[0], i[1], 0), 0)
    imgRGB.itemset((i[0], i[1], 1), 0)
    imgRGB.itemset((i[0], i[1], 2), 0)

#Crop the image to add the background image to it
croppedImage = imgDilated*background
finalImage = imgRGB + croppedImage

#Show the final image and save it
cv2.imshow("Final Result", finalImage)
cv2.imwrite("Mixed background.jpg", finalImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

