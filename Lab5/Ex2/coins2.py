import cv2
import numpy as np

#Perform necessary processing on the image
def processImage():
    imgOriginal=cv2.imread("Coins2.jpg", 0)
    retval, img = cv2.threshold(imgOriginal, 0, 255, cv2.THRESH_OTSU)
    
    #Create a copy for processing
    imgCopy=img.copy()
    
    init = 7
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (init, init))
    imgCopy = cv2.morphologyEx(imgCopy, cv2.MORPH_CLOSE, kernel)
    kernels = list()
    previous = 9999

    for i in range(1, 50, 5):
        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (i,  i))
        openedImage = cv2.morphologyEx(imgCopy, cv2.MORPH_OPEN, kernel)
        contours = cv2.findContours(openedImage, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
        
        if (previous == 9999):
            previous = len(contours[0])
            
        elif (previous - len(contours[0]) > 1):
            kernels.append((i, i))

    kernels[:0] = ((init, init), )
    
    imgGrey = imgOriginal.copy()
    imgGrey = cv2.cvtColor(imgGrey, cv2.COLOR_GRAY2RGB)
              
    previousKernel = (0,0)
    j = 0
              
    for i in reversed(kernels):
        if (j == 0):
            previousKernel = i
            j += 1
            continue
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, i)
        previousKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, previousKernel)
        previousShape = cv2.morphologyEx(img, cv2.MORPH_OPEN, previousKernel)
        currentShape = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        temp = currentShape - previousShape
        cleaner = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        temp = cv2.morphologyEx(temp, cv2.MORPH_OPEN, cleaner)
        previousKernel = i
        j += 1
        imgProcessed = colorBorders(imgGrey, temp, j)
              
    cv2.imshow("Result", imgProcessed)
    cv2.imwrite("Coins Result.jpg", imgProcessed)
    
# Color the borders of the coins, uses a function to randomize the color for a generic approach
def colorBorders(originalImage, img, color):
    
    #Dilate the image
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    imgDilated = cv2.dilate(img, kernel)
    img = imgDilated - img

    #Get all the white borders
    imgBorders = np.where(img != 0)
    imgBorders = zip(imgBorders[0], imgBorders[1])

    #Generate a random number for the color
    rand = int(np.random.rand(1, 1) * 10)
    randomColor = int(np.random.rand(1, 1) * 255)

    #Colors red if rand<3, green if <6 and not <3, blue if >=6
    for i in imgBorders:
        if rand < 3:
            originalImage.itemset((i[0], i[1], 0), 0)
            originalImage.itemset((i[0], i[1], 1), 0)
            originalImage.itemset((i[0], i[1], 2), randomColor)
            
        elif rand < 6:
            originalImage.itemset((i[0], i[1], 0), 0)
            originalImage.itemset((i[0], i[1], 1), randomColor)
            originalImage.itemset((i[0], i[1], 2), 0)
            
        else:
            originalImage.itemset((i[0], i[1], 0), randomColor)
            originalImage.itemset((i[0], i[1], 1), 0)
            originalImage.itemset((i[0], i[1], 2), 0)
    return originalImage


processImage()
cv2.waitKey(0)
cv2.destroyAllWindows()