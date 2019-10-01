import numpy as np

# FUnction to convert image to grayscale
def rgb2gray(rgb):
	return np.dot (rgb[...,:3],[0.299,0.587,0.119])


path = raw_input()	

img = rgb2gray(path)