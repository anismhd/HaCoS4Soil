'''
AAA
'''
class ContinuousPolynomialFunction():
	"""Continuous Polynomial Function of
			1 - x, PGAref
			2 - y, Ar(f)
			3 - z, M magnitude
	"""
	def __init__(self, **para):
		self.C = para.get('C')
		self.D = para.get('D')
		self.E = para.get('E')
		# log coefficients
		self.CL = para.get('CL')
		self.DL = para.get('DL')
		self.EL = para.get('EL')
	def evaluate(x,y,z):
		N = [len()]