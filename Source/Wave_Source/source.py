#source file
#two kinds: 
#1. Gaussian source for just E
#2. Gaussian Source with E and H beacuase it needs to Have both to cancle 
#out the field going backward

import numpy as np
import math  as ma

def Gaus(x,y,step,dt,tau):
	Dsrc=[]
	t=np.array(range(step-1))*dt
	t0=5*tau

	for i in range(len(t)):
		Dsrc.append(ma.exp(-((t[i]-t0)/tau)**2))

	return Dsrc

def Gaus_E_H(nx_src,ny_src,tau,L,W,dx,dy,c0,dt,Mat_map):
	t0=5*tau
	tprop=1*(L*W)**(1/2)*(dx*dy)**(1/2)/c0
	t=2*t0+3*tprop
	step=int(np.ceil(t/dt))#step is defined so there are 10 propogations
	print('step',step)
	t=np.array(range(step-1))*dt

	s=dx/2+dt/2


	A=-(Mat_map.e[nx_src-1,ny_src-1]/Mat_map.mu[nx_src-1,ny_src-1])**(1/2)

	Esrc=[]
	Hsrc=[]
	for i in range(len(t)):
		Esrc.append(ma.exp(-((t[i]-t0)/tau)**2))
		Hsrc.append(A*ma.exp(-((t[i]-t0)/tau+s)**2))

	return Esrc,Hsrc,step