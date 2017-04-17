#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 22:07:40 2017

@author: wangleo
"""
from math import floor,ceil,exp
from numpy import ones,zeros,array,sqrt
from pylab import show,figure,xlim,ylim,axes,plot,show,draw
from matplotlib import animation
<<<<<<< Updated upstream
=======
from time import sleep
    
    
m=1
cm=1e-2*m
mm=1e-3*m
inch=2.54*cm
ft=12*inch
s=1
hz=1/s
>>>>>>> Stashed changes


m=1.0

ion()

cm=1e-2*m
mm=1e-3*m
inch=2.54*cm
ft=12.0*inch
s=1.0
hz=1.0/s


c0=299792458.0*m/s
e0=8.854187817e-12*1/m
u0=1.2566370614e-6*1/m

fmax=5e3*hz
nmax=1
NLAM=10
NBUFZ=[100,100]

lam0=c0/fmax
dz=lam0/nmax/NLAM

Nz=sum(NBUFZ)+3
za=array(range(0,Nz-1))*dz


#build devic on grid
ER=ones(Nz)
UR=ones(Nz)

nbc=sqrt(UR[0]*ER[0])
dt=nbc*dz/(2*c0)

tau=0.5/fmax
t0=5*tau

tprop=nmax*Nz*dz/c0
t=2*t0+3*tprop
step=ceil(t/dt)

t=array(range(step-1))*dt
nz_src=floor(Nz/2)
Esrc=[]
for i in range(len(t)):  
    Esrc.append(exp(-((t[i]-t0)/tau)**2))

#plot(t,Esrc)

mEy=(c0*dt)/ER
mHx=(c0*dt)/UR

Ey=zeros(Nz)
Ey[40]=40
Hx=zeros(Nz)
Hx[40]=14


fig=figure(1)
for t in range(step):

    for nz in range(Nz-1):
        Hx[nz]=Hx[nz]+mHx[nz]*(Ey[nz+1]-Ey[nz])/dz#general case
    Hx[Nz-1]=Hx[Nz-1]+mHx[Nz-1]*(0-Ey[Nz-1])/dz
      
    Ey[0]=Ey[0]+mEy[0]*(Hx[0]-0)/dz
    for nz in range(1,Nz):
        Ey[nz]=Ey[nz]+mEy[nz]*(Hx[nz]-Hx[nz-1])/dz#general case
     
    Ey[nz_src-1]=Ey[nz_src-1]+Esrc[t-1]
    
    
    plot(range(Nz),Hx,range(Nz),Ey)
    show()



