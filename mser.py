import cv2 as cv
import numpy as np

# ************************************************
# MSER structure (contain features)
class MSERegion:

	# ************************************************
	# Function : Build the MSER by contour
	#	     Calculate the features of MSER
	# Inputs : 
	#	- image : color image
	#	- gray : gray image
	#	- contour : list of pixels in this contour
	# Return :
	#	- Null
	def __init__(self,image,gray,contour):

		self.points = contour
		self.area = len(contour)
		self.centroid = [0,0]
		self.bounding_box = [9999999,9999999,0,0,0,0]	# left, top, right, bottom, width, height
		self.mean_colors = [0,0,0]

		# Calculate the centroid, boundingbox and mean_colors of contour
		for pixel in contour :

			# Get location
			x, y = pixel[0], pixel[1]

			# Get gray-scale of this pixel
			val = gray[y,x]

			# Get BGR color of this pixel
			bgr = image[y,x]

			# Moments++
			self.centroid[0] += x
			self.centroid[1] += y

			# Colors++
			self.mean_colors[0] += bgr[0]
			self.mean_colors[1] += bgr[1]
			self.mean_colors[2] += bgr[2]

			# Boundingbox adjust
			self.bounding_box[0] = min(self.bounding_box[0], x)	# left
			self.bounding_box[1] = min(self.bounding_box[1], y)	# top
			self.bounding_box[2] = max(self.bounding_box[2], x)	# right
			self.bounding_box[3] = max(self.bounding_box[3], y)	# bottom

		# Calculate the centroid (m10,m01)/m00
		self.centroid[0] /= self.area
		self.centroid[1] /= self.area

		# Calculate the mean color
		self.mean_colors[0] /= self.area
		self.mean_colors[1] /= self.area
		self.mean_colors[2] /= self.area

		# Calculate the size of bounding box
		self.bounding_box[4] = self.bounding_box[2] - self.bounding_box[0] + 1	# width = right - left + 1
		self.bounding_box[5] = self.bounding_box[3] - self.bounding_box[1] + 1	# height = buttom - top + 1

		# print self.area, self.centroid, self.bounding_box, self.mean_colors

	# ************************************************
	# Function : Calculate distance between itself and another MSERegin
	#	     Feature for cluster : 
	#		1. centroid distance
	#		2. color difference
	#		3. bounding box size
	#		4. text underline distance between Y-axis
	# Inputs : 
	#	- obj : another MSERegin
	# Return :
	#	- distance (normalize to 0~1)
	def dist_to(obj):
		centroid_dist = abs(self.centroid[0]-obj.centroid[0]) \
			       +abs(self.centroid[1]-obj.centroid[1])

		color_diff = abs(self.mean_colors[0]-obj.mean_colors[0]) \
			    +abs(self.mean_colors[1]-obj.mean_colors[1]) \
			    +abs(self.mean_colors[2]-obj.mean_colors[2])

		size_diff = abs(self.bounding_box[4]-obj.bounding_box[4]) \
			   +abs(self.bounding_box[5]-obj.bounding_box[5])

		return 0


# ************************************************
# Function : Cluster MSER region by hierarchical clustering
# Inputs : 
#	- regions : MSER regions
# Return :
#	- label of regions
def MSERcluster(regions):

	# Calculate distance matrix
	return 'Hello'
