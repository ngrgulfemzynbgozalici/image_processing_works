import cv2 as cv
import numpy as np

backround = np.zeros((512, 512, 3), np.uint8) + 128 # 0 = black => 255 = white

rectangle = cv.rectangle(backround, (100, 100), (150, 155), (255, 200, 0), thickness=-1)
circle = cv.circle(backround, (250, 250), 30, (0, 0, 255), thickness=-1)

cv.namedWindow("circle and rectangle", 0)

cv.imshow("circle and rectangle", backround)

cv.waitKey(0)
cv.destroyAllWindows()
