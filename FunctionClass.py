'''
AAA
'''
from numpy import linspace,zeros,log, array
import matplotlib.pyplot as plt
from bisect import bisect
from sys import stdout

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
			self.pieces[piece] = ContinuousPolynomialFunction(C=para.get('C{0:d}'.format(piece+1)),\
												  D=para.get('D{0:d}'.format(piece+1)),\
												  E=para.get('E{0:d}'.format(piece+1)),\
												  CL=para.get('CL{0:d}'.format(piece+1)),\
												  DL=para.get('DL{0:d}'.format(piece+1)),\
												  EL=para.get('EL{0:d}'.format(piece+1)))
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
		return self.pieces[self.find_interval(x)].evaluate(x=x, y=y, z=z)

	def find_interval(self,x):
		return bisect(self.limits,x)

	def generate_figure(self, x_low, x_up, n = 101,color='r', **para):
		y = para.get('y')
		if not y:
			y = 0
		z = para.get('z')
		if not z:
			z = 0
		fig = plt.figure()
		i1 = self.find_interval(x_low)
		i2 = self.find_interval(x_up)
		if (i1 == 0) and (i2 == len(self.limits)):
			new_limits = [x_low] + self.limits + [x_up]
		elif i1 == 0:
			new_limits = [x_low] + self.limits[:i2] + [x_up]
		elif i2 == len(self.limits):
			new_limits = [x_low] + self.limits[i1:] + [x_up]
		else:
			new_limits = [x_low] + self.limits[i1:i2] + [x_up]
		for i in range(len(new_limits)-1):
			if abs(new_limits[i]-new_limits[i+1]) == 0:
				continue
			else:
				xx = linspace(new_limits[i],new_limits[i+1],n)
				yy = array([self.evaluate(x=x,y=y,z=z) for x in xx])
			plt.plot(xx,yy,c=color)
		return fig

def tests(**para):
	if para.get('test_floder'):
		loc = para.get('test_floder')
	else:
		loc = './tests/'
	if para.get('filename'):
		f = open(loc+para.get('filename'), 'w')
	else:
		f = stdout
	f.write('# Test of Function Class\n\n')
	# Testing of Continuous polynomial function
	f.write('## Testing of ContinuousPolynomialFunction Class\n\n')
	f.write('## Linear Function y=mx+c\n\n')
	f.write('\t\tConsider m = 2, c = 5')
	TES1 = ContinuousPolynomialFunction(C=[5,2])
	f.write('\t\tFunction usage, __TES1 = ContinuousPolynomialFunction(C=[5,2])__')

if __name__ == '__main__':
	tests(filename='FunctionClassTest.md')
#	BiLinear = PiecewiseContinousPolynomialFunction(2,[1],C1=[0,1],C2=[1])
#	BiLinear.generate_figure(x_low=0,x_up=10)
