'''
AAA
'''
from numpy import linspace,zeros,log, array
import matplotlib.pyplot as plt

class ContinuousPolynomialFunction():
	"""Continuous Polynomial Function of
			1 - x, PGAref
			2 - y, Ar(f)
			3 - z, M magnitude
	"""
	def __init__(self, **para):
		self.N = []
		self.C = para.get('C')
		self.N.append(len(self.C) if self.C else 0)
		self.D = para.get('D')
		self.N.append(len(self.D) if self.D else 0)
		self.E = para.get('E')
		self.N.append(len(self.E) if self.E else 0)
		# log coefficients
		self.CL = para.get('CL')
		self.N.append(len(self.CL) if self.CL else 0)
		self.DL = para.get('DL')
		self.N.append(len(self.DL) if self.DL else 0)
		self.EL = para.get('EL')
		self.N.append(len(self.EL) if self.EL else 0)
		# length of each array
#		self.N = [len(self.C),len(self.D),len(self.E),len(self.CL),len(self.DL),len(self.EL)]
	def evaluate(self,**para):
		if self.C:
			A = self.C[0]
		else:
			A = 0
		x = para.get('x')
		if not x:
			x = 0
		y = para.get('y')
		if not y:
			y = 0
		z = para.get('z')
		if not z:
			z = 0
		for i in range(1,max(self.N)):
			# Median
			if i <= self.N[0]-1:
				A = A + self.C[i]*x**i
			if i <= self.N[3]-1:
				A = A + self.CL[i]*( log(x+ self.CL[0]) )**i 
			if i <= self.N[1]-1:
				A = A + self.D[i]*y**i 
			if i <= self.N[4]-1:
				A = A + self.DL[i]*(log(y+self.DL[0]))**i
			if i <= self.N[2]-1:
				A = A + self.E[i]*z**i
			if i <= self.N[5]-1:
				A = A + self.EL[i]*(log(z+self.EL[0]))**i
		return A
	def generate_figure(self, x_low, x_up, n=101, **para):
		xx = linspace(x_low, x_up, n)
		y = para.get('y')
		if not y:
			y = 0
		z = para.get('z')
		if not z:
			z = 0
		yy = array([self.evaluate(x=x,y=y,z=z) for x in xx])
		plt.plot(xx,yy)
		plt.show()
class PiecewiseContinousPolynomialFunction(ContinuousPolynomialFunction):
	"""docstring for Piece wise ContinousPolynomialFunction"""
	def __init__(self, num_pieces, limits, **para):
		self.num_pieces = num_pieces
		self.pieces = {}
		self.limits = limits
		for piece in range(num_pieces):
			self.pieces[piece] = super().__init__(C=para.get('C{0:d}'.format(piece+1)),\
												  D=para.get('C{0:d}'.format(piece+1)),\
												  E=para.get('C{0:d}'.format(piece+1)),\
												  CL=para.get('C{0:d}'.format(piece+1)),\
												  DL=para.get('C{0:d}'.format(piece+1)),\
												  EL=para.get('C{0:d}'.format(piece+1)))
	def evaluate(self,**para):
		x = para.get('x')
		if not x:
			x = 0
		y = para.get('y')
		if not y:
			y = 0
		z = para.get('z')
		if not z:
			z = 0
		for i,limit in enumerate(self.limits):
			if x <= limit:
				return self.pieces[i].evaluate(x=x, y=y, z=z)
				break
	def generate_figure(self, x_low, x_up,y,z, n = 101):
		pass

def tests():
	pass

if __name__ == '__main__':
	print "This is a class for Continuous Polynomial Function"
	print "Test 1: Linear function A = 2x - 2"
	Linear = ContinuousPolynomialFunction(C=[-2,2])
	Linear.generate_figure(x_low=-3,x_up=10)