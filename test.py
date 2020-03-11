from osgeo import gdal
import sys, os
import os.path as path
from os import listdir

if path.isfile(sys.argv[1]):
	file_list = [sys.argv[1]]
else:
	raw_file_list = [f for f in listdir(sys.argv[1]) if path.isfile(path.join(sys.argv[1], f))]
	file_list = [x for x in raw_file_list if x[-3:] == "tif"]

for file in file_list:
	data = gdal.Open(file)
	bands = data.RasterCount
	
	if sys.argv[2] == 'jpeg':
		options_list = [
		    '-ot Byte',
		    '-of JPEG',
		    '-b ' + str(bands),
		    '-scale'
		] 
		
	elif sys.argv[2] == 'png':
		options_list = [
		    '-ot Byte',
		    '-of PNG',
		    '-b ' + str(bands),
		    '-scale'
		] 
		
	else:
		exit(" YOu FUckEd Up.")
		
	options_string = " ".join(options_list)
		
	gdal.Translate(file[:-3] + sys.argv[2], file, options=options_string)
	print("Lo hice hijos de puta.")