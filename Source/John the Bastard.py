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
import math as ma
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
L=100
W=100
#set the size of a single grid
# l=1

e0=1
mu0=1
c0=299792458.0#wrong number for not explode

e1=2#different material

dt = 0.3e-8
#dt=(e1*mu0)**(1/2)*L/c0/2#originally 2 in the denominator changed to 5
  
Mat_map=mat.Mat(L,W,dt)
print(Mat_map.M_Ez_Coef_Ex)
print(Mat_map.M_Ez_Coef_Ey)
print(Mat_map.M_Ez_Coef_Hz)
print(Mat_map.M_Ez_Coef_Dz)
    
Mat_map.add_mat_bond(0,int(L),int(W/2)-10,int(W/2),e1,mu0)#(i_i,i_f,j_i,j_f,e,mu)
Mat_map.add_mat_bond(0,int(L/2),0,int(W),e1,mu0)#(i_i,i_f,j_i,j_f,e,mu)

# dx=1e-6
# dy=1e-6

# nmax=1
# fmax=5e9
# tau=0.5/fmax


def myfunction(x):
	return 50-x

matbond_low=0
matbond_high=50
Mat_map.add_mat_bond_advanced(myfunction,matbond_low,matbond_high,e1,mu0)
dx=.1
dy=.1

# tprop=nmax*(L*W)**(1/2)*(dx*dy)**(1/2)/c0
# t=t=2*t0+3*tprop
# step=int(np.ceil(t/dt))
# print(step)


tau   = 3.3e-8
step = 500;
t0=5*tau
t=np.array(range(step-1))*dt
# print(t)



nx_src=int(3/4*L)
ny_src=int(3/4*W)
Dsrc=[]

for i in range(len(t)):  
    Dsrc.append(ma.exp(-((t[i]-t0)/tau)**2))


#setup, the following code should run once
#Set Initial Conditions
#Set Material Property
#set the PML parameters
PML=[10,10,10,10]

W2=2*W
L2=2*L

sigx=np.zeros([L2,W2])
print(sigx)
for nx in range(2*PML[0]):
    nx1=2*PML[0]-nx;
    for i in range(W2):
        sigx[nx1-1,i]=(0.5*e0/dt)*(nx/2/PML[0])**3
for nx in range(2*PML[1]):
    nx1=L2-2*PML[1]+nx+1;
    for i in range(W2):
        sigx[nx1-1,i]=(0.5*e0/dt)*(nx/2/PML[1])**3

sigy=np.zeros([L2,W2])
for ny in range(2*PML[2]):
    ny1=2*PML[2]-ny;
    for i in range(L2):
        sigy[i,ny1-1]=(0.5*e0/dt)*(ny/2/PML[2])**3
for ny in range(2*PML[3]):
    ny1=W2-2*PML[3]+ny+1;
    for i in range(L2):
        sigy[i,ny1-1]=(0.5*e0/dt)*(ny/2/PML[3])**3


sigHx=np.zeros([L,W])
sigHy=np.zeros([L,W])
sigHx1=np.zeros([L,W])
sigHy1=np.zeros([L,W])
sigDx=np.zeros([L,W])
sigDy=np.zeros([L,W])


for i in range(L):
    for j in range(W):
        sigHx[i,j]=sigx[i*2,j*2]
        sigHy[i,j]=sigy[i*2,j*2]
        sigHx1[i,j]=sigx[i*2+1,j*2+1]
        sigHy1[i,j]=sigx[i*2+1,j*2+1]
        sigDx[i,j]=sigx[i*2,j*2]
        sigDy[i,j]=sigy[i*2,j*2]
        
mHx0 = (1/dt) + sigHy/(2*e0)
mHx1 = ((1/dt) - sigHy/(2*e0))/mHx0
mHx2 = -c0/mu0/mHx0
mHx3 = -(c0*dt/e0)*sigHx/mu0/mHx0
mHy0 = (1/dt) + sigHx1/(2*e0)
mHy1 = ((1/dt) - sigHx1/(2*e0))/mHy0
mHy2 = -c0/mu0/mHy0
mHy3 = -(c0*dt/e0)*sigHy1/mu0/mHy0
mDz0 = (1/dt)+(sigDx + sigDy)/(2*e0)+sigDx*sigDy*(dt/4/e0**2)
mDz1 = (1/dt)-(sigDx + sigDy)/(2*e0)-sigDx*sigDy*(dt/4/e0**2)
mDz1 = mDz1/ mDz0
mDz2 = c0/mDz0
mDz4 = -(dt/e0**2)*sigDx*sigDy/mDz0

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
ICEx=cp.deepcopy(Ex)
ICEy=cp.deepcopy(Ex)
IDz=cp.deepcopy(Ex)
#inital condition

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
      # Create a figure
plt.gca().axes.get_xaxis().set_ticks([])  # Turn off x axis ticks
plt.gca().axes.get_yaxis().set_ticks([])  # Turn off y axis ticks
plt.imshow(Ez)

     # Typical scale of wave (higher values are clipped)




#
  
#======DO NOT USE FOR FINAL

# <<<<<<< Updated upstream
ims=[]
# <<<<<<< HEAD
# =======
# >>>>>>> Stashed changes
# while(n<100):
# =======
cont=0.05
for t in range(step) :
# 	#print(CEx)
 	CEx=cr.M_Ez_Curl_Ex(Ez,dy)
	#print("CEx=\n",CEx)
 	CEy=cr.M_Ez_Curl_Ey(Ez,dx)
	#print("CEy=\n",CEy)
# 	ICEx=ICEx+CEx
# 	ICEy=ICEy+CEy
#    
#    
# 	Hx=mHx1*Hx+(mHx2*CEx+mHx3*ICEx)
# 	#print(Hx)
# 	Hy=mHy1*Hy+(mHy2*CEy+mHy3*ICEy)
# 	#print(Hy)
# 	CHz=cr.M_Ez_Curl_Hz(Hx, Hy, dx, dy)
#    
# 	IDz=Dz+IDz
#    
#
# 	Dz=mDz1*Dz+mDz2*CHz+mDz4*IDz
# 	#add in source here
# 	Dz[nx_src-1,ny_src-1]=Dz[nx_src-1,ny_src-1]+Dsrc[t-1]
# 	#Dz[nx_src-1,ny_src-1]=Dsrc[t-1]
# 	Ez=Dz/Mat_map.e
# 	#print("Ez=",Ez)







	#CEx=cr.M_Ez_Curl_Ex(Ez,dy)
	#print("CEx=\n",CEx)
#	CEy=cr.M_Ez_Curl_Ey(Ez,dx)
	#print("CEy=\n",CEy)
 	Hx=Hx-CEx*cont
	#print("Hx=\n",Hx)
#	Hy=Hy-lin_func.M_Ez_Hy_update(CEy,Mat_map.M_Ez_Coef_Ey)
 	Hy=Hy-CEy*cont
	
	#print("Hy=\n",Hy)
 	CHz=cr.M_Ez_Curl_Hz(Hx, Hy, dx, dy)
	#print("CHz=\n",CHz)
	#Dz=Dz+lin_func.M_Ez_Dz_update(CHz,Mat_map.M_Ez_Coef_Hz)
 	Dz=Dz+CHz*cont
	#print("Dz(nosource)=\n",Dz)
	#print("SC=",Dsrc[t-1])
 	Dz[nx_src-1,ny_src-1]=Dsrc[t-1]+Dz[nx_src-1,ny_src-1]
	#print("Dz(has source)=\n",Dz)
 	Ez=Dz/Mat_map.e
	#print("EzNew=\n",Ez)
#	CEx=cr.M_Ez_Curl_Ex(Ez,dy)
#	#print("CEx=\n",CEx)
#	CEy=cr.M_Ez_Curl_Ey(Ez,dx)
#	#print("CEy=\n",CEy)
#	#Hx=Hx+lin_func.M_Ez_Hx_update(CEx,Mat_map.M_Ez_Coef_Ex)
#	Hx=Hx-CEx*cont
#	#print("Hx=\n",Hx)
#	#Hy=Hy+lin_func.M_Ez_Hy_update(CEy,Mat_map.M_Ez_Coef_Ey)
#	Hy=Hy-CEy*cont
#	
#	#print("Hy=\n",Hy)
#	CHz=cr.M_Ez_Curl_Hz(Hx, Hy, dx, dy)
#	#print("CHz=\n",CHz)
#	#Dz=Dz+lin_func.M_Ez_Dz_update(CHz,Mat_map.M_Ez_Coef_Hz)
#	Dz=Dz+CHz*cont
#	#print("Dz(nosource)=\n",Dz)
#	#print("SC=",Dsrc[t-1])
# 	Dz[nx_src-1,ny_src-1]=Dsrc[t-1]+Dz[nx_src-1,ny_src-1]
#	#print("Dz(has source)=\n",Dz)
#	Ez=Dz
#	print("EzNew=\n",Ez)
 	im=plt.imshow(Ez, animated=True,origin='lower',interpolation="none")


 	plt.hot()

	#im=Axes3D.plot_surface(X=X, Y=Y, Z=Ez,rstride=1, cstride=1)
	#plt.colorbar()
 	ims.append([im])
	#np.savetxt("Ez10.csv", Ez, delimiter=",")
 	print(t)


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

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=0)

plt.show()







