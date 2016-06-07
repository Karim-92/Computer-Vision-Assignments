import cv2
import numpy as np

def processImage(pos):
    if(pos<1):
        return
    
    imgOriginal=cv2.imread('coins.png',0)
    retval, img=cv2.threshold(imgOriginal, 0, 255, cv2.THRESH_OTSU)
    
    #Close the entire image using a kernel defined by the user.
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (pos,pos))
    closedImage=cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    #Use a second kernel to remove the small coins from the image by subtracting
    #closed image minus the large coins only image
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (pos+40,pos+40))
    largeCoinsImg = cv2.morphologyEx(closedImage, cv2.MORPH_OPEN, kernel)
    smallCoinsImg = closedImage - largeCoinsImg
    
    #Performing the erosion processing
    smallCoinsImg = cv2.morphologyEx(smallCoinsImg, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (19, 19)))
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (35,35))
    smallCoinsImg = cv2.erode(smallCoinsImg, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35,35))
    smallCoinsImg = cv2.dilate(smallCoinsImg, kernel)
    finalRes = colorImage(imgOriginal, smallCoinsImg, largeCoinsImg)
    
    #Show the trackbar and the image
    cv2.imshow("Final Result", finalRes)
    cv2.imwrite("Final Image.jpg", finalRes)
    
def colorImage(originalImage, imageOne, imageTwo):
    
    #Dilate the first image
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    imageOneDilated= cv2.dilate(imageOne, kernel)
    imageOne = imageOneDilated - imageOne

    #Dilate the second Image
    imageTwoDilated = cv2.dilate(imageTwo, kernel)
    imageTwo = imageTwoDilated - imageTwo

    #Get all the borders in both images by getting the white points
    imageOneBorders = np.where(imageOne != 0)
    imageOneBorders = zip(imageOneBorders[0], imageOneBorders[1])
    
    imageTwoBorders = np.where(imageTwo != 0)
    imageTwoBorders = zip(imageTwoBorders[0], imageTwoBorders[1])

    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_GRAY2RGB)
    
    #Color the borders of small coins red
    for i in imageOneBorders:
        originalImage.itemset((i[0], i[1], 0), 0)
        originalImage.itemset((i[0], i[1], 1), 0)
        originalImage.itemset((i[0], i[1], 2), 255)

    #Color the borders of the large coins blue
    for i in imageTwoBorders:
        originalImage.itemset((i[0], i[1], 0), 255)
        originalImage.itemset((i[0], i[1], 1), 0)
        originalImage.itemset((i[0], i[1], 2), 0)
        
    return originalImage
    
processImage(1)
cv2.createTrackbar("Structuring element: ", "Final Result", 0, 100, processImage)
cv2.waitKey(0)
cv2.destroyAllWindows()