#linear ops just multiply the  constant with the field
#this was deprecated because the perfect matching layer require
#a tensor which is different from linear ops 

import numpy as np
#Ez mode
def M_Ez_Hx_update(CEx,CEx_coeff):
	return CEx_coeff*CEx
def M_Ez_Hy_update(CEy,CEy_coeff):
	return CEy_coeff*CEy
def M_Ez_Dz_update(CHz,CHz_coeff):
	return CHz_coeff*CHz

#Hz mode
def M_Hz_D_from_E(E,Mat_e):

	return E