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
import EH.E as E_func#example of in_folder func
import Initial_Material.Mat_Class as mat
import matplotlib.pyplot as plt
print("Hello World")

#setup, the following code should run once
#Set Initial Conditions
#Set Material Property
#
#
#==================TEST for material class, you can add a block of material in 2d
Mat_map=mat.Mat(100,100)
Mat_map.add_mat_bond(0,2,0,2,1.2,1)#(i_i,i_f,j_i,j_f,e,mu)
print(Mat_map.e)
#==================

#======TEST PURPOSE 
Mat_e=np.zeros((2,2),float)
Mat_e[0,0]=0.1
Mat_e[0,1]=0.1
Mat_e[1,0]=1
Mat_e[1,1]=1
E=np.zeros((2,2),float)
E[0,0]=1
E[0,1]=1
E[1,0]=.1
E[1,1]=.1

D=E_func.E_to_D(E,Mat_e)
print(D)
#======DO NOT USE FOR FINAL
while(True):
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





