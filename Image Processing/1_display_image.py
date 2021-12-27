#
# Reference: https://new.pythonforengineers.com/blog/image-and-video-processing-in-python/
# Afrah Aamer
#
import cv2

rgb_img = cv2.imread("Images//RGB_illumination.jpg")
cv2.imshow("RGB Image",rgb_img)
cv2.waitKey(0)