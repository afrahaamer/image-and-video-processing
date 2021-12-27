import cv2

img = cv2.imread("Images//Coloured_Circle.png")
cv2.imshow("Original Image",img)

# Method 1
# b,g,r = cv2.split(img)

# cv2.imshow("Blue Part of Image",b)
# cv2.imshow("Green Part of Image",g)
# cv2.imshow("Red Part of Image",r)


# Method 2 
r = img.copy()              	# Creates a copy of the image array 
r[:,:,0] = r[:,:,1] = 0         # Setting b & g channels to 0/black
cv2.imshow("red",r)

g = img.copy()
g[:,:,0] = g[:,:,2] = 0         # Setting b & r channels to 0/black
cv2.imshow("green",g)

b = img.copy()
b[:,:,1] = b[:,:,2] = 0         # Setting g & r channels to 0/black
cv2.imshow("blue",b)

cv2.waitKey(0)