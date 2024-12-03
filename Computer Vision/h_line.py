import cv2
import numpy as np
img =cv2.imread("h_line.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(gray,75,150)

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)

for line in lines:
    x1,y1,x2,y2 =line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,225,255),3)


output_h_line = "output_line.jpg"
success = cv2.imwrite(output_h_line, img)



cv2.imshow("gray",gray)
cv2.imshow("edges",edges)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
