import numpy as np
import cv2
from matplotlib import pyplot as plt
import scipy.ndimage
from pylab import array, plot, show, axis, arange, figure, uint8 

img2 = cv2.imread('noisy2.tif', 0)

Mblur=cv2.medianBlur(img2, 25)

cv2.imwrite('Noisy 2 Median.jpg',Mblur)

img=cv2.imread('Noisy 2 Median.jpg', 0)
rows, cols = img.shape
print('Image Loaded (' + str(rows) + ' x ' + str(cols) + ')')

freq_ = np.fft.fft2(np.float32(img))
freq = np.fft.fftshift(freq_)
print(freq.shape)
cv2.imwrite('spectrum.jpg', 10*np.log(np.abs(freq)))

#Gaussian Mask
mask = np.zeros((rows,cols), np.float32)
for i in xrange(0,rows):
  for j in xrange(0,cols):
    if ((i-rows/2)**2 + (j-cols/2)**2) <= 100 ** 2:
      mask[i,j] = 1.0
mask = scipy.ndimage.filters.gaussian_filter(mask, 20)
cv2.imwrite('mask.jpg', mask * 255)

# Low Pass Filter
freq_m = np.fft.ifftshift(freq * mask)
img_back = np.fft.ifft2(freq_m)
img_back = np.absolute(img_back)
cv2.imwrite('Gaussian low pass.jpg', img_back)

# Increasing contrast
maxIntensity = 255.0 # depends on dtype of image data
x = arange(maxIntensity) 

# Parameters for manipulating image data
phi = 1
theta = 1

# Increase intensity such that
# dark pixels become much brighter, 
# bright pixels become slightly bright

newImage0 = (maxIntensity+450)*(img_back/(maxIntensity))
newImage0 = array(newImage0,dtype=uint8)

cv2.imwrite('Brighter GLPF.jpg',newImage0)
