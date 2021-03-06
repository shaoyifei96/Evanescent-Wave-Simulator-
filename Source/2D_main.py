#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:32:16 2017
@author: wangleo, shaoy
"""
#The code should be developed from big picture to specific
#steps, therefore we put files in folders, this main 
#only handle constant, update, animation 

#When import library or module ALWAYS import as
#When code is in a folder use foldername.filename
import numpy as np
import EH.Curl as cr
import Initial_Material.Mat_Class as mat
import Wave_Source.source as src
import copy as cp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PML.PMLX as pml
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D#do not delete, important for 3D
#from mpl_toolkits.mplot3d import Axes3D

#set up the size of the map
L=100
W=100

#frames=320 #frames hsould always show 10 wave propogation,this is not necessary anymore.
#======parameters=======
e0=100#initial mateiral epsilon
e1=1#thinner material to show Evanescant
mu0=1
c0=299792458.0
fmax=5e3#highest frequesency of wave
nmax=e1*mu0
dx=dy=c0/fmax/nmax#grid size based on f and n
tau = 0.5/fmax
dt=tau/10
Mat_map=mat.Mat(L,W,dt)#set up mateiral with values
print(Mat_map.M_Ez_Coef_Ex)
print(Mat_map.M_Ez_Coef_Ey)
print(Mat_map.M_Ez_Coef_Hz)
print(Mat_map.M_Ez_Coef_Dz)

#======different material=======
Mat_map.add_mat_bond(0,int(L),0,int(W),e0,mu0)#(i_i,i_f,j_i,j_f,e,mu)#initialize to be some material
#Mat_map.add_mat_bond(0,int(L/2),0,int(W),e1,mu0)#(i_i,i_f,j_i,j_f,e,mu)
#Mat_map.add_mat_bond(0,int(L/2)-15,0,int(W),e0,mu0)
#Use a function to add material
def function1(x):
	return x+40
def function2(x):
	return x+30

matbond_low=0
matbond_high=100
#material adds on the left of the specified function
Mat_map.add_mat_bond_advanced(function1,matbond_low,matbond_high,e1,mu0)
#Mat_map.add_mat_bond_advanced(function2,matbond_low,matbond_high,e0,mu0)

#======sources of wave=======
nx_src=int(np.floor(30))
ny_src=int(np.floor(30))

Esrc,Hsrc,step=src.Gaus_E_H(nx_src,ny_src,tau,L,W,dx,dy,c0,dt,Mat_map)
#step is defined for 10 wave propogation 
#========Source end==========

#setup, the following code should run once
#Set Initial Conditions
#Set Material Property
#set the PML parameters
PMLx=[10,10,10,10]
mHx0,mHx1,mHx2,mHx3,mHy0,mHy1,mHy2,mHy3,mDz0,mDz1,mDz2,mDz4=pml.pmlx(PMLx,L,W,dt)
#
#==================PML END


print("mat=",Mat_map.e)
#==================

Ex=np.zeros((L,W),float)

r,c=np.shape(Ex)
Ex[0:r,0:c]=0


Ez=cp.deepcopy(Ex)
Hx=cp.deepcopy(Ex)
Hy=cp.deepcopy(Ex)
Dz=cp.deepcopy(Ex)
ICEx=cp.deepcopy(Ex)
ICEy=cp.deepcopy(Ex)
IDz=cp.deepcopy(Ex)
#inital condition

fig =plt.figure()      # Create a figure
ax1=plt.subplot(1,2,1) # this plot is to show the the material boundary
ax1.set_aspect('equal')
ax1.set_xlim([0, W])
ax1.set_ylim([0, L])
x=range(matbond_low,matbond_high)
y1=[]
y2=[]
for x_now in x:
    y1.append(function1(x_now))
    y2.append(function2(x_now))
im_mat=ax1.plot(y1,x)

#ani=plt.subplot(1,2,2)
      # Create a figure
plt.gca().axes.get_xaxis().set_ticks([])  # Turn off x axis ticks
plt.gca().axes.get_yaxis().set_ticks([])  # Turn off y axis ticks

     # Typical scale of wave (higher values are clipped)


ims=[]
Ezs=[]
#list to contain images for animation
for t in range(step) :#iterating function

 	CEx=cr.M_Ez_Curl_Ex(Ez,dy)
 	CEy=cr.M_Ez_Curl_Ey(Ez,dx)
 	
     
##====TFSF=====================================================================     
 	for i in range(L):
         
         CEx[i,ny_src-1]=(Ez[i,ny_src-1]-Ez[i,ny_src-2]-Esrc[t-1])/dy

 	ICEx=ICEx+CEx
 	ICEy=ICEy+CEy 
    
 	Hx=mHx1*Hx+(mHx2*CEx+mHx3*ICEx)

 	Hy=mHy1*Hy+(mHy2*CEy+mHy3*ICEy)

 	CHz=cr.M_Ez_Curl_Hz(Hx, Hy, dx, dy)
 	for i in range(L):
         CHz[i,ny_src-1]=(Hy[i,ny_src-1]-Hy[i-1,ny_src-1])/dx-(Hy[i,ny_src-1]-Hy[i,ny_src-2])/dy+Hsrc[t-1]/dy
 
 	IDz=Dz+IDz
 	Dz=mDz1*Dz+mDz2*CHz+mDz4*IDz
#==============================================================================
 	
##====single source============================================================
# 	ICEx=ICEx+CEx
# 	ICEy=ICEy+CEy
# 	Hx=mHx1*Hx+(mHx2*CEx+mHx3*ICEx)
## 	#print(Hx)
# 	Hy=mHy1*Hy+(mHy2*CEy+mHy3*ICEy)
## 	#print(Hy)
# 	CHz=cr.M_Ez_Curl_Hz(Hx, Hy, dx, dy)
# 	IDz=Dz+IDz
# 	Dz=mDz1*Dz+mDz2*CHz+mDz4*IDz
# 	Dz[nx_src-1,ny_src-1]=Esrc[t-1]+Dz[nx_src-1,ny_src-1]
##====single source============================================================

##====visualization============================================================
 	Ez=Dz/Mat_map.e


 	#im=plt.imshow(Ez, origin='lower',animated=True,interpolation="bicubic")
 	im=plt.imshow(Ez, origin='lower',animated=True,interpolation="bicubic")

 	plt.hsv()
 	#ims.append([im])
 	Ezs.append([Ez])
	
 	print(t)
##====Animation============================================================

#ani = animation.ArtistAnimation(fig, ims, interval=20, blit=True,
#                                repeat_delay=0)


#======3D Animation=========================

def data(i):
	#print(i)
	ax.clear()

	line=ax.plot_surface(xx,yy,Ezs[i][0],cmap=cm.coolwarm)
	ax.set_zlim(-1.0, 1.0)

	return line,

print("Ezs=",np.shape(Ezs))


ax=fig.add_subplot(122,projection="3d")


x=range(W)
y=range(L)
xx,yy=np.meshgrid(x,y)



line=ax.plot_surface(xx,yy,Ezs[1][0])
ax.set_zlim(-1.0,1.0)
ani=animation.FuncAnimation(fig, data,frames=range(step),interval=30,repeat_delay=0,blit=False)
#================================

plt.show()





