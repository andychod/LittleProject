import numpy as np
import cv2

img = cv2.imread("image.jpg")

#以灰階方式讀取圖片
img_gray = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)

cv2.imshow('My Image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#寫入圖檔
cv2.imwrite('output.jpg',img_gray)
