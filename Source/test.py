#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:32:16 2017

@author: wangleo
"""

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
import matplotlib.animation as animation
import time as tm
import matplotlib.colors as clr
from mpl_toolkits.mplot3d import Axes3D


#set up the size of the map
L=10
W=10
#set the size of a single grid
l=1

e0=8.854187817e-12
mu0=1.2566370614e-6
c0=299792458.0#wrong number for not explode

dt=(e0*mu0)**(1/2)/c0/5#originally 2 in the denominator changed to 5
  
Mat_map=mat.Mat(L,W,dt)

def myfunction(x):
	return x

matbond_low=0
matbond_high=10
Mat_map.add_mat_bond_advanced(myfunction,matbond_low,matbond_high,10,10)
dx=1
dy=1



#setup, the following code should run once
#Set Initial Conditions
#Set Material Property
#
#
#==================TEST for material class, you can add a block of material in 2d


print("mat=",Mat_map.e)
#==================

#======TEST PURPOSE 


Ex=np.zeros((L,W),float)

r,c=np.shape(Ex)
Ex[0:r,0:c]=0


Ez=cp.deepcopy(Ex)
Hx=cp.deepcopy(Ex)
Hy=cp.deepcopy(Ex)
Dz=cp.deepcopy(Ex)
#inital condition
Hy[int(L/2),int(W/2)+2]=.1


fig =plt.figure(1)      # Create a figure
ax1=plt.subplot(1,2,1)
ax1.set_aspect('equal')
ax1.set_xlim([0, W])
ax1.set_ylim([0, L])
x=range(matbond_low,matbond_high)
y=[]
for x_now in x:
    y.append(myfunction(x_now))
im_mat=ax1.plot(x,y)



plt.subplot(1,2,2)
scale = 10          # Typical scale of wave (higher values are clipped)
plt.gca().axes.get_xaxis().set_ticks([])  # Turn off x axis ticks
plt.gca().axes.get_yaxis().set_ticks([])  # Turn off y axis ticks
plt.imshow(Hy)



#plt.colorbar()
  
#======DO NOT USE FOR FINAL
n=0

# <<<<<<< Updated upstream
ims=[]
# <<<<<<< HEAD
# =======
# >>>>>>> Stashed changes
# while(n<100):
# =======
X = range(L)
Y = range(W)
X, Y = np.meshgrid(X, Y)


while(n<100):


	print(n)
	CEx=cr.M_Ez_Curl_Ex(Ez,dy)
	#print(CEx)
	CEy=cr.M_Ez_Curl_Ey(Ez,dx)
	#print(CEy)
	Hx=lin_func.M_Ez_Hx_update(Hx,CEx,Mat_map.M_Ez_Coef_Ex)
	#print(Hx)
	Hy=lin_func.M_Ez_Hy_update(Hy,CEy,Mat_map.M_Ez_Coef_Ey)
	#print(Hy)
	CHz=cr.M_Ez_Curl_Hz(Hx, Hy, dx, dy)
	Dz=lin_func.M_Ez_Dz_update(Dz,CHz,Mat_map.M_Ez_Coef_Hz)
	#add in source here

	Ez=lin_func.M_Ez_Ez_from_Dz(Dz, Mat_map.M_Ez_Coef_Dz)
	#print("Ez=",Ez)
	im=plt.imshow(Ez, animated=True,origin='lower',interpolation="bicubic",norm=clr.Normalize())
	plt.hsv()

	#im=Axes3D.plot_surface(X=X, Y=Y, Z=Ez,rstride=1, cstride=1)
	#plt.colorbar()
	ims.append([im])
	#np.savetxt("Ez10.csv", Ez, delimiter=",")
	n=n+1



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

ani = animation.ArtistAnimation(fig, ims, interval=30, blit=True,
                                repeat_delay=0)

plt.show()







