import re
import math
import pandas as pd
import numpy as np

def convertIgsToFloat(c):
	return float(c[0]) * math.pow(10, float(c[2]))

with open('uploads/input.igs', 'r') as myfile:
    data = myfile.read().replace('\n', '')

columns = ['x', 'y', 'z']

coords = re.findall(r'(-?[0-9]\d*(\.\d+)?)D(-?[0-9]\d*(\.\d+)?)', data)

coord_arr = np.zeros(shape=(len(coords)//3,3))

i = 0
for c in range(0, len(coords) - 2, 3):
	x = convertIgsToFloat(coords[c])
	y = convertIgsToFloat(coords[c+1])
	z = convertIgsToFloat(coords[c+2])
	coord_arr[i] = [x, y, z]
	i = i + 1

df_ = pd.DataFrame(coord_arr, columns=columns)
df_.index = df_.index + 1
df_.to_csv('uploads/out.csv', sep=';', encoding='utf-8')