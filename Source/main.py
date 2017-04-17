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
dt=0.001
dx=0.1
dy=0.1
#setup, the following code should run once
#Set Initial Conditions
#Set Material Property
#
#
#==================TEST for material class, you can add a block of material in 2d
Mat_map=mat.Mat(100,100,dt)
Mat_map.add_mat_bond(0,2,0,2,1.2,1)#(i_i,i_f,j_i,j_f,e,mu)
print(Mat_map.e)
#==================

#======TEST PURPOSE 

Ex=np.zeros((10,10),float)
r,c=np.shape(Ex)
Ex[0:r,0:c]=0

Ex=np.zeros((2,2),float)
Ex[0,0]=0
Ex[0,1]=0
Ex[1,0]=0
Ex[1,1]=0

Ez=cp.deepcopy(Ex)



#======DO NOT USE FOR FINAL
while(True):
	cr.M_Ez_Curl_Ex(Ez,dy)

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





