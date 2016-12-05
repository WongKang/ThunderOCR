import cv2 as cv
import numpy as np
import mser
from color import generate_random_color
from mser import MSERcluster

# Reference :
# https://segmentfault.com/a/1190000003742442


# Load image from file
image = cv.imread('test.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
paint = image.copy()

# Retrieve MSERs from image
area_delta = 5
area_min = 180
contours = cv.MSER(area_delta,area_min).detect(gray)

# Collect MSERegins and calculate the features
regions = []
for contour in contours:
	# Fill the contour with random color
	color = generate_random_color()
	for pixel in contour:
		paint[pixel[1],pixel[0]] = color

	# Create a MSERegin structure
	region = mser.MSERegion(image,gray,contour)
	regions.append(region)

# Cluster regions
MSERcluster(regions)

# Show image
cv.imshow('MSER', paint)
cv.waitKey(0)
cv.destroyAllWindows()
