'''
This is a class for Amplification Function of Soil
'''
from numpy import size, argmax, linspace
import matplotlib.pyplot as plt
class AmplificationFunction():
	"""docstring for AmplificationFunction"""
	def __init__(self, type1, **parameters):
		'''
			type		 - 'continuous' function or 'piecewise' function or a 'separate external file'
				in case of continuous
					Equation Type 1
						log (Amp) = C0 + C1 PGAref  + D1 Ar 
									   + C1L log(PGAref + C0L) + D1L log(Ar+D0L)
									   + ...............
									   + Cn (PGAref)^n + Dn (Ar)^n
									   + CnL (log(PGAref + C0L))^n  + DnL (log(PGAref + D0L))^n
 						sigma     = SC0 + SC1 PGAref + SD1 Ar 
									    + SC1L log(PGAref + SC0L) + SD1L log(Ar+SD0L)
									    + ...............
									    + SCn (PGAref)^n + SDn (Ar)^n
									    + SCnL (log(PGAref + SC0L))^n  + SDnL (log(PGAref + SD0L))^n
				in case of piecewise continuous
					Equation Type 2
						Equation Type 1 in Piecewise form
						C D, Cn, Dn, SC, SD, SCn, SDn will be defined as 2D, each row for each section

		'''
		self.type = type1
		self.C = parameters.get('C')
		self.CL = parameters.get('CL')
		self.D = parameters.get('D')
		self.DL = parameters.get('DL')
		self.SC = parameters.get('SC')
		self.SCL = parameters.get('SCL')
		self.SC = parameters.get('SC')
		self.SDL = parameters.get('SDL')
		self.lim = parameters.get('limits')
	def evaluate(PGAref,Ar):
		if self.type == 'piecewise':
			N = [size(self.C,1),size(self.CL,1),size(self.D,1),size(self.DL,1),size(self.SC,1),size(self.SCL,1),size(self.SDL,1)]
			num_pieces = size(self.C,0)
			for index,limit in enumerate(self.lim):
				if Ar <= limit:
					break
			C = self.C[index]
			CL = self.CL[index]
			D = self.D[index]
			DL = self.DL[index]
			SC = self.SC[index]
			SCL = self.SCL[index]
			SD = self.SD[index]
			SDL = self.SDL[index]
		if self.type == 'continuous':
			C = self.C
			CL = self.CL
			D = self.D
			DL = self.DL
			SC = self.SC
			SCL = self.SCL
			SD = self.SD
			SDL = self.SDL
		lnMedian = C[0]
		sigma = SC[0]
		for i in range(1,max(N)):
			# Median
			if i <= N[0]-1:
				lnMedian = lnMedian + C[i]*PGAref**i
			if i <= N[1]-1:
				lnMedian = lnMedian + CL[i]*( log(PGAref+ CL[0]) )**i 
			if i <= N[2]-1:
				lnMedian = lnMedian + D[i]*Ar**i 
			if i <= N[3]-1:
				lnMedian = lnMedian + DL[i]*log(Ar+DL[0])**i
			# Sigma
			if i <= N[4]-1:
				sigma = sigma + SC[i]*PGAref**i
			if i <= N[5]-1:
				sigma = sigma + SCL[i]*( log(PGAref+ SCL[0]) )**i 
			if i <= N[6]-1:
				sigma = sigma + SD[i]*Ar**i 
			if i <= N[7]-1:
				sigma = sigma + SDL[i]*log(Ar+SDL[0])**i
		return lnMedian, sigma
	def generate_figure():
		Ar = 0
		pass
#		elif self.type == 'continuous':
#			N = [size(self.C,0),size(self.CL,0),size(self.DL,0),size(self.SC,0),size(self.SCL,0),size(self.SDL,0)]
#			num_pieces = 1

		'''

if __name__ == '__main__':
	A = AmplificationFunction('continuous', A=0)