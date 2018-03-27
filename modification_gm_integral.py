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
from numpy import zeros, log, interp, dot
from scipy.stats import norm

def proabability_less_than_a_IM_for_a_rock_motion(A0, IM_array,ground_amp_fun_type, para1, para2):
	'''
	This function will evaluate the probability of surface motion(As) being less than a given value (IM) for a input base rock motion Ar 

	Simply :: It will do the job of quation (7) of ref 1
	'''
	P_As_l_A0 = zeros(len(IM_array))
	if ground_amp_fun_type=='lognormal':
		for i in range(len(IM_array)):
			mean = log(para1[i]*IM_array[i])
			sigma = para2[i]
			P_As_l_A0[i] = norm.cdf( (log(A0)-mean)/sigma )
#		mean = log(interp(Ar,IM_array,para1))
#		sigma = interp(Ar,IM_array,para2)
#		return norm.cdf( (log(Ar)-mean)/sigma )
	elif ground_amp_fun_type=='normal':
		for i in range(len(IM_array)):
			mean = para1[i]*IM_array[i]
			sigma = para2[i]
			P_As_l_A0[i] = norm.cdf( (A0-mean)/sigma )
#		mean = interp(Ar,IM_array,para1)
#		sigma = interp(Ar,IM_array,para2)
#		return norm.cdf( (Ar-mean)/sigma )
	else:
		return None
	pass
	return P_As_l_A0

def generate_rock_gm_probability(IM_array,Rock_GM_Median,lnRock_GM_SD):
	'''
	This is function to evaluate probability of occurence each base rock intesity of motion
	from a given median and standard deviation from attenuation equation

	Simply :: It will do the job of equation (5) of ref 1
	'''
	P_A0_e_Ar = zeros(len(IM_array))
	Z = (log(IM_array) - log(Rock_GM_Median))/lnRock_GM_SD
	for i in range(len(IM_array)):
		if i==0:
			P_A0_e_Ar[0] = norm.cdf(0.5*(Z[0]+Z[1]))
			continue
		if i==(len(IM_array)-1):
			P_A0_e_Ar[-1] = 1.0-norm.cdf(0.5*(Z[-2]+Z[-1]))
			continue
		else:
			P_A0_e_Ar[i] = norm.cdf( 0.5*(Z[i+1]+Z[i]) ) - \
			 norm.cdf( 0.5*(Z[i]+Z[i-1]) )
			continue
	return P_A0_e_Ar

def soil_ground_motion_excedance_probability(IM_array,Rock_GM_Median, lnRock_GM_SD, ground_amp_fun_type, para1, para2):
	P_A0_e_Ar = generate_rock_gm_probability(IM_array,Rock_GM_Median,lnRock_GM_SD)# The P[A0 = Ar | M,R] as given in eqn(5) of ref 1
	P_As_g_A0 = zeros(len(IM_array))
	for i in range(len(IM_array)):
		A0 = IM_array[i]
		P_As_l_A0 = proabability_less_than_a_IM_for_a_rock_motion(A0,IM_array,ground_amp_fun_type, para1, para2) # The P[As<=A0|Ar] as given in eqn(7) of ref 1
		P_As_g_A0[i] = 1 - sum(P_As_l_A0*P_A0_e_Ar)
	return P_As_g_A0

if __name__ == '__main__':
	import numpy as np
	import matplotlib.pyplot as plt
	from scipy.stats import norm
	print "\n\n\tRef: 1 - Cramer, Chris H. Site-specific seismic-hazard analysis that is completely probabilistic. \n\tBulletin of the Seismological Society of America 93.4 (2003): 1841-1846.\n"
	print "\t1 - Testing of generate_rock_gm_probability function"
	print "\tBasis : Ref(1) Table 1"
	table1 = np.loadtxt('paper_table1.txt', delimiter=',')
	P_A0_e_Ar = generate_rock_gm_probability(table1[0],0.85,0.75)
	print "\t{0:3s} {1:15s} {2:15s} {3:15s} {4:15s}\n\t{5:066d}".format('NO','GM Bin', 'P(A=Ar),Paper', 'P(A=Ar),Comput.','ERROR (%)',0)
	for i in range(len(table1[0])):
		print "\t{0:3d} {1:15.7f} {2:15.5E} {3:15.5E} {4:15.3f}".format(i+1, table1[0,i], table1[1,i], P_A0_e_Ar[i], (P_A0_e_Ar[i]-table1[1,i])*100/table1[1,i])
	print "\n\t{0:3s} {1:15s} {2:15.3f} {3:15.3f} {4:15s}".format(' ', 'Total', sum(table1[1]), sum(P_A0_e_Ar), '')
	print "\t2 - Testing of proabability_less_than_a_IM_for_a_rock_motion function \n"
	fmt = '\t{0:2s}\{1:3s}'
	hline = '\t------'
	for i in range(len(table1[0])):
		fmt = fmt + '|{0:6.4f}'.format(table1[0,i])
		hline = hline + '-------'
	print fmt.format('A0','Ar')
	print hline
	for i in range(len(table1[0])):
		fmt = '\t{0:6.4f}'.format(table1[0,i])
		P_As_l_A0 = proabability_less_than_a_IM_for_a_rock_motion(table1[0,i], table1[0],'lognormal', table1[2], table1[3])
		for j in range(len(table1[0])):
			fmt = fmt + '|{0:6.4f}'.format(P_As_l_A0[j])
		print fmt
		print hline
	P_As_g_A0 = soil_ground_motion_excedance_probability(table1[0],0.85, 0.75, 'lognormal', table1[2], table1[3])
	print "\n\n\t{0:3s}|{1:15s}|{2:25s}|{3:25s}|{4:15s}".format('NO','As', 'P(As > A0| M,R), Paper', 'P(As > A0| M,R), Comput','ERROR (%)')
	print hline
	for i in range(len(table1[0])):
		print "\t{0:3d} {1:15.7f} {2:25.5E} {3:25.5E} {4:15.3f}".format(i+1, table1[0,i], table1[4,i], P_As_g_A0[i], (P_As_g_A0[i]-table1[4,i])*100/table1[4,i])
	print "\n\t TESTING COMPLETED SUCCESFULLY"