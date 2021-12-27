import cv2

img = cv2.imread("C://deets//1-1//Image and Video Processing//IVP Lab//image-and-video-processing//Images//Coloured_Circle.png")
cv2.imshow("Original Image",img)
b,g,r = cv2.split(img)
img_merged = cv2.merge([r,g,b])
cv2.imshow("Merged Image",img_merged)
cv2.waitKey(0)