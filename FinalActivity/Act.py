import cv2
import numpy as np
import easyocr

img_path_1 = 'Assets/placa_q.jpg'
img_path_2 = 'Assets/placa_4.jpg'

original = cv2.imread(img_path_1)
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# Filter black
mask = np.zeros(gray.shape, dtype=np.uint8)

for y in range(gray.shape[0]):
    for x in range(gray.shape[1]):
        value = gray[y, x]
        if value < 50:
            mask[y, x] = 255

# Gaussian filter
blurred = cv2.GaussianBlur(mask, (21, 21), sigmaX=9)

# Filter white
mask2 = np.zeros(blurred.shape, dtype=np.uint8)

for y in range(blurred.shape[0]):
    for x in range(blurred.shape[1]):
        value2 = blurred[y, x]
        if value2 > 120:
            mask2[y, x] = 255

# OCR

reader = easyocr.Reader(['en'])
results = reader.readtext(mask2)

for (bbox, text, confidence) in results:
    (tl, tr, br, bl) = bbox
    tl = tuple(map(int, tl))
    br = tuple(map(int, br))
    cv2.rectangle(original, tl, br, (0, 255, 0), 2)
    cv2.putText(original, text, tl, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    print(f"Detected: '{text}' with confidence {confidence:.2f}")


cv2.imshow("Original", original)
cv2.imshow("Mask", mask)
cv2.imshow("Gaussian", blurred)
cv2.imshow("Mask2", mask2)
# cv2.imshow("OCR Output", original)
cv2.waitKey(0)
cv2.destroyAllWindows()