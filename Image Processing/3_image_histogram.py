#
#   https://www.geeksforgeeks.org/opencv-python-program-analyze-image-using-histogram/
#
#

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Images//Parrot.jpeg")
# height, width, channels = img.shape
# new_height = height/2
# new_width = width/2
# print(new_height,new_width)
img_resized = cv2.resize(img,(0,0), fx = 0.5, fy = 0.5)
cv2.imshow("Image",img_resized)
histr = cv2.calcHist([img_resized],[0],None,[256],[0,256])
plt.plot(histr)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.title("Original")
plt.show()
cv2.waitKey(0)