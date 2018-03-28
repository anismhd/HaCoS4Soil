'''
AAA
'''
from numpy import linspace,zeros,log
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
	def generate_figure(self,**para):
		'''
			x_fix : fixed value for 'x'
			x_low : lower bound for 'x'
			x_up  : upper bound for 'x'
			y_fix : fixed value for 'y'
			y_low : lower bound for 'y'
			y_up  : upper bound for 'y'
			z_fix : fixed value for 'z'
			z_low : lower bound for 'z'
			z_up  : upper bound for 'z'
		'''
		x_fix = para.get('x_fix')
		x_low = para.get('x_low')
		x_up = para.get('x_up')
		y_fix = para.get('y_fix')
		y_low = para.get('y_low')
		y_up = para.get('y_up')
		z_fix = para.get('z_fix')
		z_low = para.get('z_low')
		z_up = para.get('z_up')
		# One dimentional case
		OneDx = ((y_fix and z_fix) or not(y_fix or z_fix)) and (x_low and x_up) # varying x
		OneDz = ((y_fix and x_fix) or not(y_fix or x_fix)) and (z_low and z_up) # varying z
		OneDy = ((z_fix and x_fix) or not(z_fix or x_fix)) and (y_low and y_up) # varying y
		# Two dimensional case (Two Dimensional Part Still Pending)
		TwoDxy = z_fix and ((x_low and x_up) and (y_low and y_up))
		TwoDxz = y_fix and ((x_low and x_up) and (z_low and z_up))
		TwoDyz = x_fix and ((y_low and y_up) and (z_low and z_up))
		AA = zeros(101)
		xx = zeros(101)
		if OneDx:
			xx = linspace(x_low,x_up, 101)
			for i,value in enumerate(xx):
				AA[i] = self.evaluate(x=value)
			plt.plot(xx,AA)
			plt.show()
			return
		if OneDy:
			xx = linspace(y_low,y_up, 101)
			for i,value in enumerate(xx):
				AA[i] = self.evaluate(y=value)
			plt.plot(xx,AA)
			plt.show()
			return
		if OneDz:
			xx = linspace(z_low,z_up, 101)
			for i,value in enumerate(xx):
				AA[i] = self.evaluate(z=value)
			plt.plot(xx,AA)
			plt.show()
			return

if __name__ == '__main__':
	print "This is a class for Continuous Polynomial Function"
	print "Test 1: Linear function A = 2x - 2"
	Linear = ContinuousPolynomialFunction(C=[-2,2])
	Linear.generate_figure(x_low=-3,x_up=10)