# USAGE
# python scan.py --image images/page.jpg

# import the necessary packages
from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils


for i in range(1249):
	print(i)
	inputname = "murm-jpg/murm{0}.jpg".format(i)
	image = cv2.imread(inputname)
	ratio = image.shape[0] / 500.0
	orig = image.copy()
	image = imutils.resize(image, height = 256)

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 40, 40)

	cv2.imshow("Edged", edged)
	outputname = "murm-edge/edge{0}.jpg".format(i)
	cv2.imwrite(outputname, edged)

	cv2.waitKey(1000)
	cv2.destroyAllWindows()