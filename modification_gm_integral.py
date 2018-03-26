'''
This Program in Written by
	Anis Mohammed Vengasseri
	anis.mhd@gmail.com
	reachamv.com

	For more theoretical background ref
		1 - Cramer, Chris H. "Site-specific seismic-hazard analysis that is completely probabilistic." Bulletin of the Seismological Society of America 93.4 (2003): 1841-1846.

Description of Input Arguments
	IM_array			:: Intensity of ground motion array used in hazard calculation
	Rock_GM_Median		:: Median of ground motion for a given magnitude and distance
	lnRock_GM_SD		:: Standard deviation of log normal ground motion for a given magnitude and distance
	ground_amp_fun_type	:: Probability density model used in ground motion amplification function.
							0 - for lognormal
							1 - for normal
	para1				:: array of numbers equivalent to IM_array for defining ground_amp_fun_type
							median - in the case of lognormal
							mean   - in the case of gaussian
	para2				:: array of numbers equivalent to IM_array for defining ground_amp_fun_type
'''
from numpy import zeros, log
from scipy.stats import norm

def proabability_less_than_a_IM_for_a_rock_motion():
	'''
	This function will evaluate the probability of surface motion(As) being less than a given value (IM) for a input base rock motion Ar 

	Simply :: It will do the job of mequation (7) of ref 1
	'''
	pass

def generate_rock_gm_probability(IM_array,Rock_GM_Median,lnRock_GM_SD):
	'''
	This is function to evaluate probability of occurence each base rock intesity of motion
	from a given median and standard deviation from attenuation equation

	Simply :: It will do the job of equation (5) of ref 1
	'''
	P_A0_Ar = zeros(len(IM_array))
	Z = (log(IM_array) - log(Rock_GM_Median))/lnRock_GM_SD
	for i in range(len(IM_array)):
		if i==0:
			P_A0_Ar[0] = norm.cdf(0.5*(Z[0]+Z[1]))
			continue
		if i==(len(IM_array)-1):
			P_A0_Ar[-1] = 1.0-norm.cdf(0.5*(Z[-2]+Z[-1]))
			continue
		else:
			P_A0_Ar[i] = norm.cdf( 0.5*(Z[i+1]+Z[i]) ) - \
			 norm.cdf( 0.5*(Z[i]+Z[i-1]) )
			continue
	return P_A0_Ar

def soil_ground_motion_excedance_probability(IM_array,Rock_GM_Median, lnRock_GM_SD, ground_amp_fun_type, para1, para2):
	P_A0_Ar = generate_rock_gm_probability(IM_array,Rock_GM_Median,lnRock_GM_SD)# The P[A0 = Ar | M,R] as given in eqn(5) of ref 1
	pass

if __name__ == '__main__':
	import numpy as np
	import matplotlib.pyplot as plt
	from scipy.stats import norm
	print "Testing of generate_rock_gm_probability function"
	print "\t 1 - Cramer, Chris H. Site-specific seismic-hazard analysis that is completely probabilistic. \n\t Bulletin of the Seismological Society of America 93.4 (2003): 1841-1846."
	print "Basis : Ref(1) Table 1"
	table1 = np.loadtxt('paper_table1.txt', delimiter=',')
	P_A0_Ar = generate_rock_gm_probability(table1[0],0.85,0.75)
	print "\t{0:3s} {1:15s} {2:15s} {3:15s} {4:15s}\n\t{5:066d}".format('NO','GM Bin', 'P(A=Ar),Paper', 'P(A=Ar),Comput.','ERROR (%)',0)
	for i in range(len(table1[0])):
		print "\t{0:3d} {1:15.7f} {2:15.5E} {3:15.5E} {4:15.3f}".format(i+1, table1[0,i], table1[1,i], P_A0_Ar[i], (P_A0_Ar[i]-table1[1,i])*100/table1[1,i])
	print "\n\t{0:3s} {1:15s} {2:15.3f} {3:15.3f} {4:15s}".format(' ', 'Total', sum(table1[1]), sum(P_A0_Ar), '')
	print "\n\t TESTING COMPLETED SUCCESFULLY"