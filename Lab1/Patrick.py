import numpy as np
import cv2

"""# Load an color image in grayscale
img = cv2.imread('Patrick.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

img=np.zeros((512,512,3), np.uint8)
img=cv2.rectangle(img, (384,0),(510,128),(0,255,0),3)
cv2.imshow('Patrick', img)
cv2.waitKey(0)
cv2.destroyAllWindows()