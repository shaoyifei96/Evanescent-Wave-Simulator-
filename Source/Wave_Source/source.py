#source file
#two kinds: 
#1. point source
import numpy as np
import math  as ma

def Gaus(x,y,step,dt,tau):
	Dsrc=[]
	t=np.array(range(step-1))*dt
	t0=5*tau

	for i in range(len(t)):
		Dsrc.append(ma.exp(-((t[i]-t0)/tau)**2))

	return Dsrc
