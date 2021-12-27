import cv2
import numpy as np

img = cv2.imread("C://deets//1-1//Image and Video Processing//IVP Lab//image-and-video-processing//Images//Coloured_Circle.png")
cv2.imshow("Original Image",img)

# Splitting the image
b,g,r = cv2.split(img)

# Merging with Black
k = np.zeros_like(b)   # zeroes_like() creates an empty null data structure similar to the one passed to it
bm = cv2.merge([b,k,k]) # Merging each channel with black to give the effect of colour
gm = cv2.merge([k,g,k])
rm = cv2.merge([k,k,r])

# Displaying splitted coloured image
cv2.imshow("Blue Part of Image",bm)
cv2.imshow("Green Part of Image",gm)
cv2.imshow("Red Part of Image",rm)

# Merging the splitted image
img_merged = cv2.merge([b,g,r])
cv2.imshow("Merged Image",img_merged)
cv2.waitKey(0)