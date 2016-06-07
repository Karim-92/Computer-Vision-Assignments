import cv2
import numpy as np

img=cv2.imread('salt.tif', 1)

image=cv2.imread('Salt Edge Detected.jpg',0)
lines = cv2.HoughLines(image,1,np.pi/180,110)

for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('Hough Lines.jpg',img)