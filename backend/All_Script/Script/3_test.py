import cv2.cv2 as cv2
import numpy as np

img = np.zeros((500, 510, 3), np.uint8)

cv2.putText(img=img, text="Script Running Well", org=(90, 50), fontFace=1, fontScale=2, color=(0, 255, 0))
cv2.putText(img=img, text="Welcome To Hacker's Paradise", org=(0, 160), fontFace=1, fontScale=2, color=(0, 255, 0))
cv2.rectangle(img, (230, 250), (285, 300), (0, 0, 255), 3)
cv2.putText(img=img, text="SK SAYED AKTAR", org=(100, 450), fontFace=1, fontScale=2, color=(0, 255, 0))
cv2.imshow("Sample Image", img)
cv2.waitKey(0)
