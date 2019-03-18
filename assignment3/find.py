import os
import sys

if len(sys.argv) > 2:
	print('Arguments: %s', str(sys.argv))
	file_type = str(sys.argv[1])
	print(file_type)
	directory = str(sys.argv[2])
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith(file_type):
				print(os.path.join(root, file))
