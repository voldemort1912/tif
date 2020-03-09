import rasterio
import numpy as np
import PIL
import sys
import cv2

from PIL import Image


infile = rasterio.open(sys.argv[1], driver='GTiff', dtype='uint16')

if (len(sys.argv) == 3):
	index = [int(sys.argv[2])]
else:
	index = [ x for x in infile.indexes ]

print(index)

for a in index:
	infile_array = infile.read(a)

	im_col = Image.fromarray(infile_array).point(lambda i:i*(1./256)).convert('L')

	infile_array_processed = np.array(im_col)
	
	array_processing = cv2.cvtColor(infile_array_processed, cv2.COLOR_GRAY2BGR)
	#print(array_processing.dtype)
	array_processed = cv2.convertScaleAbs(array_processing)

	im = Image.fromarray(array_processed)
	im = im.convert('RGB')
	
	out_name = sys.argv[1] + str(a) + ".png"	
	
	im.save( out_name, "png")
	print("Lo hice hijos de puta.")





"""
infile_array = infile.read(a)
	print(infile_array)
	im = Image.fromarray(infile_array)
	im_col = im.point(lambda i:i*(1./256)).convert('L')

	infile_array2 = np.array(im_col)

	
	array_processing = cv2.cvtColor(infile_array2, cv2.COLOR_GRAY2BGR)
	print(array_processing.dtype)
	array_processed = cv2.convertScaleAbs(array_processing)
	#print(cvuint8.dtype)


	im = Image.fromarray(array_processed)

	#im.mode = 'I'

	
	#im2 = im.convert('RGB')
	out_name = sys.argv[1] + str(a) + ".png"	
	
	im.save( out_name, "png")
	print("Lo hice hijos de puta.")

"""
