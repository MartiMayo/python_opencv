import numpy as np
import cv2
from imutils import imutils

# translations
image = cv2.imread("/home/mmc/code/python_opencv/Books/Practical Python and OpenCV, 3rd Edition/code/images/trex.png")
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape
[0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape
[0]))
cv2.imshow("Shifted Up and Left", shifted)

shifted = imutils.translate(image, 0, 100)
cv2.imshow('Shifted Down', shifted)


cv2.imshow('Original', image)
im_resized = imutils.resize(image, width=100)
cv2.imshow('Resized', im_resized)