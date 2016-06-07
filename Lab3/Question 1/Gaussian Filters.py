import cv2
import numpy as np
import scipy.ndimage

print('Using OpenCV ' + cv2.__version__)

img = cv2.imread('pout.jpg', 0)
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
mask = scipy.ndimage.filters.gaussian_filter(mask, 32)
cv2.imwrite('mask.jpg', mask * 255)

# Low Pass Filter
freq_m = np.fft.ifftshift(freq * mask)
img_back = np.fft.ifft2(freq_m)
img_back = np.absolute(img_back)
cv2.imwrite('Gaussian low pass.jpg', img_back)

# Invert Mask
mask = np.ones((rows,cols), np.float32) - mask


# High Pass Filter
freq_m = np.fft.ifftshift(freq * mask)
img_back = np.fft.ifft2(freq_m)
img_back = np.absolute(img_back)
cv2.imwrite('Gaussian high pass.jpg', img_back)
