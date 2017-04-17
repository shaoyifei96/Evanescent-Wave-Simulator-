#The code should be developed from big picture to specific
#steps, therefore we put files in folders, this main 
#should not be edited, main is based on YOUTUBE:
#https://www.youtube.com/watch?v=vVeyP85xKD4&t=8s

#recommand using Sublime, Don't use Spyder, the tabs are 
#different, it can cause problems

#When import library or module ALWAYS import as
#When code is in a folder use foldername.filename
#e.g. import numpy as np
#e.g. import plot as plt

import numpy as np
import EH.Linear_Ops as lin_func#example of in_folder func
import EH.Curl as cr
import Initial_Material.Mat_Class as mat
import copy as cp
import matplotlib.pyplot as plt
print("Hello World")
dt=0.5
dx=0.1
dy=0.1
#setup, the following code should run once
#Set Initial Conditions
#Set Material Property
#
#
#==================TEST for material class, you can add a block of material in 2d
Mat_map=mat.Mat(10,10,dt)
Mat_map.add_mat_bond(0,2,0,2,1.2,1)#(i_i,i_f,j_i,j_f,e,mu)
print("mat=",Mat_map.e)
#==================

#======TEST PURPOSE 

Ex=np.zeros((10,10),float)
r,c=np.shape(Ex)
Ex[0:r,0:c]=0


Ez=cp.deepcopy(Ex)
Hx=cp.deepcopy(Ex)
Hy=cp.deepcopy(Ex)
Dz=cp.deepcopy(Ex)
Ez[0,0]=1

#======DO NOT USE FOR FINAL
while(True):
	CEx=cr.M_Ez_Curl_Ex(Ez,dy)
	CEy=cr.M_Ez_Curl_Ey(Ez,dx)
	Hx=lin_func.M_Ez_Hx_update(Hx,CEx,Mat_map.M_Ez_Coef_Ex)
	Hy=lin_func.M_Ez_Hy_update(Hy,CEy,Mat_map.M_Ez_Coef_Ey)
	CHz=cr.M_Ez_Curl_Hz(Hx, Hy, dx, dy)
	Dz=lin_func.M_Ez_Dz_update(Dz,CHz,Mat_map.M_Ez_Coef_Hz)
	Ez=lin_func.M_Ez_Ez_from_Dz(Dz, Mat_map.M_Ez_Coef_Dz)
	print(Ez)
	#Loop
	break
	#Update D from H
	#Update E from D
	#Handle E field boundary(boundary means edge, not material)
	#Handle E field Source

	#Update B from E
	#Update H from B
	#Handle H field Boundary
	#Handle H field Source

	#Record Some Data
	#Simulate





