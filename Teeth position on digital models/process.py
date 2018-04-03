import math
import pandas as pd

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in radians.
    """
    ox, oy, oz = origin
    px, py, pz = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy, pz


def loadData(fileName, fields):
	return pd.read_csv(fileName, delimiter=',', skipinitialspace=True, usecols=fields)

fields = ['info','l_x','l_y','l_z','m_x','m_y','m_z','d_x','d_y','d_z','a_x','a_y','a_z','b_x','b_y','b_z']
n_digits = 4
suffix = '_2'

dataset = loadData('uploads/data.csv', fields)

col_l_x_new = []
col_l_y_new = []
col_l_z_new = []
col_d_x_new = []
col_d_y_new = []
col_d_z_new = []
col_a_x_new = []
col_a_y_new = []
col_a_z_new = []
col_b_x_new = []
col_b_y_new = []
col_b_z_new = []
col_rotacao = []
col_angulacao = []
col_torque = []

for i in range(dataset.shape[0]):
	l = (dataset['l_x'][i],dataset['l_y'][i],dataset['l_z'][i])
	m = (dataset['m_x'][i],dataset['m_y'][i],dataset['m_z'][i])
	d = (dataset['d_x'][i],dataset['d_y'][i],dataset['d_z'][i])
	a = (dataset['a_x'][i],dataset['a_y'][i],dataset['a_z'][i])
	b = (dataset['b_x'][i],dataset['b_y'][i],dataset['b_z'][i])

	angle = math.atan((d[0] - m[0])/(d[1] - m[1]))

	l_new = rotate(m, l, angle)
	d_new = rotate(m, d, angle)
	a_new = rotate(m, a, angle)
	b_new = rotate(m, b, angle)
	
	angulacao = math.atan((a_new[1] - b_new[1])/(a_new[2] - b_new[2]))
	torque = math.atan((a_new[0] - b_new[0])/(a_new[2] - b_new[2]))

	col_l_x_new.append(round(l_new[0], n_digits))
	col_l_y_new.append(round(l_new[1], n_digits))
	col_l_z_new.append(round(l_new[2], n_digits))
	col_d_x_new.append(round(d_new[0], n_digits))
	col_d_y_new.append(round(d_new[1], n_digits))
	col_d_z_new.append(round(d_new[2], n_digits))
	col_a_x_new.append(round(a_new[0], n_digits))
	col_a_y_new.append(round(a_new[1], n_digits))
	col_a_z_new.append(round(a_new[2], n_digits))
	col_b_x_new.append(round(b_new[0], n_digits))
	col_b_y_new.append(round(b_new[1], n_digits))
	col_b_z_new.append(round(b_new[2], n_digits))

	col_rotacao.append(round(angle, n_digits))
	col_angulacao.append(round(angulacao, n_digits))
	col_torque.append(round(torque, n_digits))

dataset[str('l_x') + str(suffix)] = col_l_x_new
dataset[str('l_y') + str(suffix)] = col_l_y_new
dataset[str('l_z') + str(suffix)] = col_l_z_new
dataset[str('d_x') + str(suffix)] = col_d_x_new
dataset[str('d_y') + str(suffix)] = col_d_y_new
dataset[str('d_z') + str(suffix)] = col_d_z_new
dataset[str('a_x') + str(suffix)] = col_a_x_new
dataset[str('a_y') + str(suffix)] = col_a_y_new
dataset[str('a_z') + str(suffix)] = col_a_z_new
dataset[str('b_x') + str(suffix)] = col_b_x_new
dataset[str('b_y') + str(suffix)] = col_b_y_new
dataset[str('b_z') + str(suffix)] = col_b_z_new
dataset[str('rotacao')] = col_rotacao
dataset[str('angulacao')] = col_angulacao
dataset[str('torque')] = col_torque

dataset.to_csv('uploads/out.csv', sep=',', encoding='utf-8')