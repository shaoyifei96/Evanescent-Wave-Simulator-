import numpy as np

def E_to_D(E,Mat_e):
	D=E#this has pointer problem, be careful #edit
	r,c=np.shape(E)
	for i in range (0,r):
		for j in range (0,c):
			D[i,j]=E[i,j]*Mat_e[i,j]

	return D