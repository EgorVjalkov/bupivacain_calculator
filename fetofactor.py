def fetofactor_smpl(x, y='', z=''):
	if x == 'y' and z == 'y': return 2
	elif (x == 'y' and y == 'y') or (x == 'n' and z == 'y'): return 1
	elif x == 's': return -1
	else:
		return 0