import cv2

img = cv2.imread("C://deets//1-1//Image and Video Processing//IVP Lab//image-and-video-processing//Images//Coloured_Circle.png")
cv2.imshow("Original Image",img)
b,g,r = cv2.split(img)
cv2.imshow("Blue Part of Image",b)
cv2.imshow("Green Part of Image",g)
cv2.imshow("Red Part of Image",r)
cv2.waitKey(0)