import cv2
import numpy as np

img = cv2.imread('Assets/pool-balls.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([35, 255, 255])

mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

for y in range(hsv.shape[0]):
    for x in range(hsv.shape[1]):
        h, s, v = hsv[y, x]
        if (lower_yellow[0] <= h <= upper_yellow[0] and
            lower_yellow[1] <= s <= upper_yellow[1] and
            lower_yellow[2] <= v <= upper_yellow[2]):
            mask[y, x] = 255

result_hsv = np.zeros_like(hsv)
for y in range(hsv.shape[0]):
    for x in range(hsv.shape[1]):
        if mask[y, x] == 255:
            result_hsv[y, x] = hsv[y, x]

result_hsv = cv2.cvtColor(result_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", img)
cv2.imshow("Mask HSV", mask)
cv2.imshow("Filtered Yellow HSV", result_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()