import numpy as np
import cv2
from pylab import array, plot, show, axis, arange, figure, uint8 

# Image data
image = cv2.imread('a.jpg',0) # load as 1-channel 8bit grayscale
cv2.imshow('image',image)
maxIntensity = 255.0 # depends on dtype of image data
x = arange(maxIntensity) 

# Parameters for manipulating image data
phi = 1
theta = 1

# Increase intensity such that
# dark pixels become much brighter, 
# bright pixels become slightly bright
#(maxIntensity/phi)*(image/(maxIntensity/theta))**0.5
#(maxIntensity+10)*(image/(maxIntensity))

newImage0 = (maxIntensity+10)*(image/(maxIntensity))
newImage0 = array(newImage0,dtype=uint8)

cv2.imshow('newImage0',newImage0)
cv2.imwrite('aBrighter.jpg',newImage0)

y = (maxIntensity/phi)*(x/(maxIntensity/theta))**0.5

#stacking images side by side and saving
stacked = np.hstack((image,newImage0)) 
cv2.imwrite('astacked.jpg',stacked)

'''
# Decrease intensity such that
# dark pixels become much darker, 
# bright pixels become slightly dark 
newImage1 = (maxIntensity/phi)*(image/(maxIntensity/theta))**2
newImage1 = array(newImage1,dtype=uint8)

cv2.imshow('newImage1',newImage1)

z = (maxIntensity/phi)*(x/(maxIntensity/theta))**2
'''

# Plot the figures
figure()
plot(x,y,'r-') # Increased brightness
plot(x,x,'k:') # Original image
#plot(x,z, 'b-') # Decreased brightness
#axis('off')
axis('tight')
show()

# Close figure window and click on other window 
# Then press any keyboard key to close all windows
closeWindow = -1
while closeWindow<0:
    closeWindow = cv2.waitKey(1) 
cv2.destroyAllWindows()

