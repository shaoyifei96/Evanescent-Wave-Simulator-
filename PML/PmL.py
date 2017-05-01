#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 22:51:14 2017

@author: wangleo
"""
def NPML(XL,XH,YL,YH,W,L):
#set the PML parameters
    PML=[XL,XH,YL,YH]
    
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
    mHy0 = (1/dt) + sigHx/(2*e0)
    mHy1 = ((1/dt) - sigHx/(2*e0))/mHy0
    mHy2 = - c0/mu0/mHy0
    mHy3 = - (c0*dt/e0) * sigHy/mu0/mHy0
    mDz0 = (1/dt) + (sigDx + sigDy)/(2*e0)+sigDx*sigDy*(dt/4/e0**2)
    mDz1 = (1/dt) - (sigDx + sigDy)/(2*e0)- sigDx*sigDy*(dt/4/e0**2)
    mDz1 = mDz1/ mDz0
    mDz2 = c0/mDz0
    mDz4 = - (dt/e0**2)*sigDx*sigDy/mDz0
    