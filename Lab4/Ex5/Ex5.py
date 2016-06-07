import cv2
import numpy as np



img = cv2.imread('Lane.jpg',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(3,3),3)
edges = cv2.Canny(gray,150,150*3,apertureSize = 3)
cv2.imshow('Lane Edges', edges)

minLineLength = 0
maxLineGap = 0

lines = cv2.HoughLinesP(edges,1,np.pi/90,40,minLineLength,maxLineGap)

for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    
cv2.imwrite('houghlines5.jpg',img)

if cv2.waitKey(0)==27:
    destroyAllWindows()