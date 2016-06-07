import cv2
import numpy as np
from PIL import Image

#Global Variables
lowThreshold = 0
highThreshold = 200
ratio = 3
apertureSize = 10

def CannyThreshold(lowThreshold):
    #Apply gaussian blur with kernel of 11X11
    blurred_image = cv2.GaussianBlur(img,(11,11),3)
    #Detect edges with Canny
    detected_edges = cv2.Canny(blurred_image,lowThreshold,lowThreshold*ratio,apertureSize)
    
    #For the rectangle only image
    blurred_rectangle = cv2.GaussianBlur(img,(11,11),1)
    #Save an image with the rectangle only to color it red, 135 is the lowest threshold at which
    #the circle disappears completely and the rectangle is about to disappear
    rectangleOnly = cv2.Canny(blurred_rectangle,183,183*3,apertureSize)
    
    #Show Image
    cv2.imshow('Salt Edge Detected', detected_edges)
    cv2.imwrite('Salt Edge Detected.jpg', detected_edges)
    cv2.imwrite('Salt with rectangle only.jpg', rectangleOnly)

#Open the image
img = cv2.imread('salt.tif', 0)

#Create trackbar and window
cv2.namedWindow('Salt Edge Detected')
cv2.createTrackbar('Threshold','Salt Edge Detected',lowThreshold, highThreshold, CannyThreshold)

#Initialization
CannyThreshold(0)


#Open the rectangle only image to paint red
image = Image.open("Salt with rectangle only.jpg").convert('RGB')

#Load pixels in the image
pix = image.load()
redTuple=(255,0,0)

x=image.size[0]
y=image.size[1]

#Color pixels if they're not black
for i in range(x):
  for j in range(y):
    if(pix[i,j]!=(0,0,0)):
        pix[i,j]=redTuple

result=image.save("Salt Red.jpg")


#Close the window on keyboard press                  
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
    
#Combine the two images, the red rectangle image with the edge detected image
imageOne=Image.open('Salt Edge Detected.jpg')
imageTwo=Image.open('Salt Red.jpg')

imageTwo.paste(imageOne,(0,0),imageOne)
imageTwo.save("Final Result.jpg")
                  



