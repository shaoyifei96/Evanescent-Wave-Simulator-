#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 22:07:40 2017

@author: wangleo
"""
from numpy import ones,zeros
from pylab import show,figure,xlim,ylim,axes
from matplotlib import animation

m=1
cm=1e-2*m
mm=1e-3*m
inch=2.54*cm
ft=12*inch
s=1
hz=1/s

c0=299792458*m/s
e0=8.854187817e-12*1/m
u0=1.2566370614e-6*1/m


step=1000
dz=0.006*m
Nz=200
dt=1e-11*s

#build devic on grid
ER=ones([1,Nz])
UR=ones([1,Nz])

mEy=(c0*dt)/ER
mHx=(c0*dt)/UR

Ey=zeros([1,Nz])
Hx=zeros([1,Nz])

for t in range(step):
    for nz in range(1,Nz-1):
        Hx[nz-1]=Hx[nz-1]+mHx[nz-1]*(Ey[nz]-Ey[nz-1])/dz
    Hx[nz-1]=Hx[Nz-1]+mHx[Nz-1]*(0-Ey[Nz-1])/dz
      
    Ey[0]=Ey[0]+mEy[0]*(Hx[0]-0)/dz
    for nz in range(2,Nz):
        Ey[nz-1]=Ey[nz-1]+mEy[nz-1]*(Hx[nz-1]-Hx[nz-1])/dz
