#
#   https://www.geeksforgeeks.org/opencv-python-program-analyze-image-using-histogram/
#   https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html`
# 

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Images//Parrot.jpeg")
# height, width, channels = img.shape
# new_height = height/2
# new_width = width/2
# print(new_height,new_width)

# RESIZING
img_resized = cv2.resize(img,(0,0), fx = 0.5, fy = 0.5)
cv2.imshow("Image",img_resized)


# Sectioning Plot space
figure, axis = plt.subplots(2, 1)

# Method 1 of Calculating Histogram
hist_r = cv2.calcHist([img_resized],[0],None,[256],[0,256])
axis[0].plot(hist_r)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
axis[0].plot(hist)

# Method 2 of Calculating Histogram
axis[1].hist(img.ravel(),256,[0,256])

plt.show()
cv2.waitKey(0)