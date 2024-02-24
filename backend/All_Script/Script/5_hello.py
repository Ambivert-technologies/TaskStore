import cv2
import numpy as np

img = np.zeros((500, 500, 3))
cv2.putText(img, "Hack Mobile", (180, 20), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, thickness=2, color=(0, 0, 255))
cv2.imshow("Check Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
