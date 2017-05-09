#PML boundary by matching each next layer to be a perfect aborbant
#of the previous layer


import numpy as np

def pmlx(PML,W,L,dt):
    #set the PML parameters
    e0=1
    mu0=1
    c0=299792458.0
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
            sigHx[i,j]=sigx[i*2,j*2+1]
            sigHy[i,j]=sigy[i*2,j*2+1]
            sigHx1[i,j]=sigx[i*2+1,j*2]
            sigHy1[i,j]=sigx[i*2+1,j*2]
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

    return mHx0,mHx1,mHx2,mHx3,mHy0,mHy1,mHy2,mHy3,mDz0,mDz1,mDz2,mDz4