import cv2
import numpy as np
import math

def add_salt_and_pepper(img, amount=0.1):
    noisy = img.copy()
    total_pixels = img.shape[0] * img.shape[1]

    # Salt
    num_salt = int(amount * total_pixels / 2)
    coords = [np.random.randint(0, i - 1, num_salt) for i in img.shape[:2]]
    noisy[coords[0], coords[1]] = 255

    # Pepper
    num_pepper = int(amount * total_pixels / 2)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in img.shape[:2]]
    noisy[coords[0], coords[1]] = 0

    return noisy

img = cv2.imread('Assets/camera.jpg')
noisy_img = add_salt_and_pepper(img)


av_filter = np.array([
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
            ]) / 9

gaussian_filter = np.array([
            [np.power(math.e, -4), np.power(math.e, -2), np.power(math.e, -4)],
            [np.power(math.e, -2), 1, np.power(math.e, -2)],
            [np.power(math.e, -4), np.power(math.e, -2), np.power(math.e, -4)]
            ]) * (2/math.pi)

avfiltered_img = cv2.filter2D(img, ddepth=-1, kernel=av_filter)
gaussianfiltered_img = cv2.filter2D(img, ddepth=-1, kernel=gaussian_filter)


cv2.imshow("Original Image", img)
cv2.imshow("Noisy Image (Salt and Pepper)", noisy_img)
cv2.imshow("Filtered Image (AV)", avfiltered_img)
cv2.imshow("Filtered Image (Gaussian)", gaussianfiltered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()