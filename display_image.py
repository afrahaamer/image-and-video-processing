#
# Reference: https://new.pythonforengineers.com/blog/image-and-video-processing-in-python/
# Afrah Aamer
#
import cv2
import sys
rgb_img = cv2.imread(sys.argv[1])
cv2.imshow("RGB Image",rgb_img)
cv2.waitKey(0)