import cv2 
img1 = cv2.imread("Images//Jellyfish.jpg",0)
img2 = cv2.imread("Images//Pattern.jpg",0)
img1_resized = cv2.resize(img1,(400,600))
img2_resized = cv2.resize(img2,(400,600))
added_img = cv2.add(img1_resized,img2_resized)
# cv2.imwrite("Added_Image.jpg",added_img)
cv2.imshow("Added_Image",added_img)
cv2.waitKey(0)