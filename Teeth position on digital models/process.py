import math
import pandas as pd

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle aformat a given origin.
    The angle should be given in radians.
    """
    ox, oy, oz = origin
    px, py, pz = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy, pz


def loadData(fileName, fields):
	return pd.read_csv(fileName, delimiter=';', skipinitialspace=True, usecols=fields)

fields_in  = ['info','x','y','z']
fields_out = ['l_x','l_y','l_z','d_x','d_y','d_z','a_x','a_y','a_z','b_x','b_y','b_z']
n_format = '.8f'
suffix = '_2'

dataset = loadData('uploads/data.csv', fields_in)

col_l_x = []
col_l_y = []
col_l_z = []
col_m_x = []
col_m_y = []
col_m_z = []
col_d_x = []
col_d_y = []
col_d_z = []
col_a_x = []
col_a_y = []
col_a_z = []
col_b_x = []
col_b_y = []
col_b_z = []
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

for i in range(0, dataset.shape[0], 5):
	l = (float(dataset['x'][i]),float(dataset['y'][i]),float(dataset['z'][i]))
	m = (float(dataset['x'][i+1]),float(dataset['y'][i+1]),float(dataset['z'][i+1]))
	d = (float(dataset['x'][i+2]),float(dataset['y'][i+2]),float(dataset['z'][i+2]))
	a = (float(dataset['x'][i+3]),float(dataset['y'][i+3]),float(dataset['z'][i+3]))
	b = (float(dataset['x'][i+4]),float(dataset['y'][i+4]),float(dataset['z'][i+4]))

	col_l_x.append(format(l[0], n_format))
	col_l_y.append(format(l[1], n_format))
	col_l_z.append(format(l[2], n_format))
	col_m_x.append(format(m[0], n_format))
	col_m_y.append(format(m[1], n_format))
	col_m_z.append(format(m[2], n_format))
	col_d_x.append(format(d[0], n_format))
	col_d_y.append(format(d[1], n_format))
	col_d_z.append(format(d[2], n_format))
	col_a_x.append(format(a[0], n_format))
	col_a_y.append(format(a[1], n_format))
	col_a_z.append(format(a[2], n_format))
	col_b_x.append(format(b[0], n_format))
	col_b_y.append(format(b[1], n_format))
	col_b_z.append(format(b[2], n_format))

	angle = math.atan((d[0] - m[0])/(d[1] - m[1]))

	l_new = rotate(m, l, angle)
	d_new = rotate(m, d, angle)
	a_new = rotate(m, a, angle)
	b_new = rotate(m, b, angle)
	
	angulacao = math.atan((a_new[1] - b_new[1])/(a_new[2] - b_new[2]))
	torque = math.atan((a_new[0] - b_new[0])/(a_new[2] - b_new[2]))

	col_l_x_new.append(format(l_new[0], n_format))
	col_l_y_new.append(format(l_new[1], n_format))
	col_l_z_new.append(format(l_new[2], n_format))
	col_d_x_new.append(format(d_new[0], n_format))
	col_d_y_new.append(format(d_new[1], n_format))
	col_d_z_new.append(format(d_new[2], n_format))
	col_a_x_new.append(format(a_new[0], n_format))
	col_a_y_new.append(format(a_new[1], n_format))
	col_a_z_new.append(format(a_new[2], n_format))
	col_b_x_new.append(format(b_new[0], n_format))
	col_b_y_new.append(format(b_new[1], n_format))
	col_b_z_new.append(format(b_new[2], n_format))

	col_rotacao.append(format(math.degrees(angle), n_format))
	col_angulacao.append(format(math.degrees(angulacao), n_format))
	col_torque.append(format(math.degrees(torque), n_format))

df = pd.DataFrame(columns=fields_out)

df[str('l_x')] = col_l_x
df[str('l_y')] = col_l_y
df[str('l_z')] = col_l_z
df[str('d_x')] = col_d_x
df[str('d_y')] = col_d_y
df[str('d_z')] = col_d_z
df[str('a_x')] = col_a_x
df[str('a_y')] = col_a_y
df[str('a_z')] = col_a_z
df[str('b_x')] = col_b_x
df[str('b_y')] = col_b_y
df[str('b_z')] = col_b_z
df[str('l_x') + str(suffix)] = col_l_x_new
df[str('l_y') + str(suffix)] = col_l_y_new
df[str('l_z') + str(suffix)] = col_l_z_new
df[str('d_x') + str(suffix)] = col_d_x_new
df[str('d_y') + str(suffix)] = col_d_y_new
df[str('d_z') + str(suffix)] = col_d_z_new
df[str('a_x') + str(suffix)] = col_a_x_new
df[str('a_y') + str(suffix)] = col_a_y_new
df[str('a_z') + str(suffix)] = col_a_z_new
df[str('b_x') + str(suffix)] = col_b_x_new
df[str('b_y') + str(suffix)] = col_b_y_new
df[str('b_z') + str(suffix)] = col_b_z_new
df[str('rotacao')] = col_rotacao
df[str('angulacao')] = col_angulacao
df[str('torque')] = col_torque

df.to_csv('uploads/out.csv', sep=';', encoding='utf-8')