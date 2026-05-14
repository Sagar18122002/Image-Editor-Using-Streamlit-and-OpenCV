import cv2
import numpy as np


def apply_blur(image, ksize):
    if ksize > 1:
        if ksize % 2 == 0:
            ksize += 1
        image = cv2.GaussianBlur(image, (ksize, ksize), 0)
    return image


def apply_sharpness(image, alpha):
    blurred = cv2.GaussianBlur(image, (0, 0), 3)
    image = cv2.addWeighted(image, 1 + alpha, blurred, -alpha, 0)
    return image


def apply_brightness(image, beta):
    image = cv2.convertScaleAbs(image, alpha=1, beta=beta)
    return image


def apply_contrast(image, alpha):
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
    return image


def apply_edge_detection(image, thresh1, thresh2):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, thresh1, thresh2)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


def apply_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)