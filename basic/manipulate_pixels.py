import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/home/mmc/code/python_opencv/Books/Practical Python and OpenCV, 3rd Edition/code/images/trex.png")
cv2.imshow('platjeta', img)

img[0:100,0:100] = (0,0,255)
cv2.imshow('modified', img)