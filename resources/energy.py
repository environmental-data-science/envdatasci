# A simple DRY method for calculating E

def Q(T, epsilon=1, unit='C'):
	""" Calculates Energy emitted by an object with temperature T

	parameters:
		T - Temperature of object
		epsilon - emissivity of object [0-1]. Default is 1
		unit = units of temperature (either 'F', 'C', or 'K') Default is 'C'

	returns:
		Q - Energy emitted by object [W/m^2]

	"""
	SIGMA = 5.67e-8 # W/m2/K^4
	if unit == 'F':
		unit = 'C'
		T = (T - 32) * (5./9.)
	if unit == 'C':
		T = T + 273.15
	return epsilon * SIGMA * T**4

