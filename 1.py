from matplotlib.contour import ContourSet
import numpy as np
import cv2
import skimage

loc = input("Enter image location: ")

img = cv2.imread(loc)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5 ,5), 0)
thresh = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)[1]


result = img.copy()
bounding_boxes = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

print("Number of bounding boxes: ", len(bounding_boxes))

for i in range(len(bounding_boxes)):
    centerX,centerY,width,height = cv2.boundingRect(bounding_boxes[i])
    cv2.rectangle(result, (centerX, centerY), (centerX+width, centerY+height), (255, 0, 0), 2)
    print("centerX,centerY,width,height:",centerX,centerY,width,height)
 
cv2.imshow("bounding_box", result)
cv2.waitKey(0)