import numpy as np
#Ez mode
def M_Ez_Hx_update(Hx,CEx,CEx_coeff):
	return Hx+CEx_coeff*CEx
def M_Ez_Hy_update(Hy,CEy,CEy_coeff):
	return Hy+CEy_coeff*CEy
def M_Ez_Dz_update(Dz,CHz,CHz_coeff):
	return Dz+CHz_coeff*CHz
def M_Ez_Ez_from_Dz(Dz,Dz_coef):
	return Dz_coef*Dz

#Hz mode
def M_Hz_D_from_E(E,Mat_e):
	D=E#this has pointer problem, be careful #edit
	r,c=np.shape(E)
	for i in range (0,r):
		for j in range (0,c):
			D[i,j]=E[i,j]*Mat_e[i,j]

	return D