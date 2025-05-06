import cv2
import numpy as np
import math

av_filter = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) / 9

gaussian_filter = np.array([[
    np.power(math.e, -4), 
    np.power(math.e, -2), 
    np.power(math.e, -4)
],[
    np.power(math.e, -2), 
    1, 
    np.power(math.e, -2)
],[
    np.power(math.e, -4), 
    np.power(math.e, -2), 
    np.power(math.e, -4)
]]) * (2/math.pi)

img = cv2.imread('Assets/van-gogh.jpg')

img_gaussian = cv2.filter2D(
            img, 
            ddepth=-1, 
            kernel=gaussian_filter)

factor2 = 2
factor4 = 4
factor8 = 8

subsampled2_after = img[::factor2, ::factor2]
subsampled4_after = img[::factor4, ::factor4]
subsampled8_after = img[::factor8, ::factor8]

subsampled2_before = img_gaussian[::factor2, ::factor2]
subsampled4_before = img_gaussian[::factor4, ::factor4]
subsampled8_before = img_gaussian[::factor8, ::factor8]

subsampled2_gaussian = cv2.filter2D(
            subsampled2_after, 
            ddepth=-1, 
            kernel=gaussian_filter)

subsampled4_gaussian = cv2.filter2D(
            subsampled4_after, 
            ddepth=-1, 
            kernel=gaussian_filter)

subsampled8_gaussian = cv2.filter2D(
            subsampled8_after, 
            ddepth=-1, 
            kernel=gaussian_filter)

cv2.imshow("Subsampled by factor 2", subsampled2_after)
cv2.imshow("Gaussian before subsampled by factor 2", subsampled2_before)
cv2.imshow("Gaussian after subsampled by factor 2", subsampled2_gaussian)

cv2.imshow("Subsampled by factor 4", subsampled4_after)
cv2.imshow("Gaussian before subsampled by factor 4", subsampled4_before)
cv2.imshow("Gaussian after subsampled by factor 4", subsampled4_gaussian)

cv2.imshow("Subsampled by factor 8", subsampled8_after)
cv2.imshow("Gaussian before subsampled by factor 8", subsampled8_before)
cv2.imshow("Gaussian after subsampled by factor 8", subsampled8_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()