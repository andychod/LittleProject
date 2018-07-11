## 安裝套件(使用pyCharm)
* numpy <br>
* opencv-python <br>
<br>

讀取檔案
```python
img = cv2.imread('image.jpg')
```
檔案格式:<br>
OpenCV 的 cv2.imread 在讀取圖片時，可以在第二個參數指定圖片的格式，可用的選項有三種：<br>
* cv2.IMREAD_COLOR :<br>
此為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel。<br>
* cv2.IMREAD_GRAYSCALE:<br>
以灰階的格式來讀取圖片。<br>
* cv2.IMREAD_UNCHANGED: <br>
讀取圖片中所有的 channels，包含透明度的 channel。<br>
<br>

範例:
```python
# 以灰階的方式讀取圖檔
img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 顯示圖片
cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
# 關閉 'My Image' 視窗
cv2.destroyWindow('My Image')
# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 寫入圖檔
cv2.imwrite('output.jpg', img)
```