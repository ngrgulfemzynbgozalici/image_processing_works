from genericpath import exists
import cv2 as cv
import os

path = "showPhoto\\spring-flowers-110671_1280.jpg"

if os.path.exists(path):
    img = cv.imread(path, 0)
    cv.imshow("image", img)
else:
    print("Görsel mevcut değil.")

print("Program sonlandı.")

cv.waitKey(0)
cv.destroyAllWindows()
