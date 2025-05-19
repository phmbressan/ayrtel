import cv2
import pytesseract
import numpy as np


def extract_text_from_region(image, box):
    (x1, y1), (x2, y2) = box
    roi = image[y1:y2, x1:x2]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = sharpen_image(gray)
    return pytesseract.image_to_string(
        gray,
        config=r"--psm 8 --oem 1 -c tessedit_char_whitelist='1234567890.'",
        lang="eng",
    ).strip(" .\n")


def sharpen_image(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened
