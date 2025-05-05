import cv2
import numpy as np

img = cv2.imread('Assets/pool-balls.jpg')

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lower_yellow = np.array([200, 200, 0])
upper_yellow = np.array([255, 255, 100])

mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

for y in range(rgb.shape[0]):
    for x in range(rgb.shape[1]):
        r, g, b = rgb[y, x]
        if (lower_yellow[0] <= r <= upper_yellow[0] and
            lower_yellow[1] <= g <= upper_yellow[1] and
            lower_yellow[2] <= b <= upper_yellow[2]):
            mask[y, x] = 255

result_rgb = np.zeros_like(rgb)
for y in range(rgb.shape[0]):
    for x in range(rgb.shape[1]):
        if mask[y, x] == 255:
            result_rgb[y, x] = rgb[y, x]

result_bgr = cv2.cvtColor(result_rgb, cv2.COLOR_RGB2BGR)

cv2.imshow("Original", img)
cv2.imshow("Mask RGB", mask)
cv2.imshow("Filtered Yellow RGB", result_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()