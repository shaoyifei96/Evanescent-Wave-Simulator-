#curl equations subtract the two ajacent Ey and divide by distance in between
#do it in both x and y dir, after that, doing the curl of 4 H will
#generate the new E

import numpy as np

def M_Ez_Curl_Ex(Ez,dy):#curl of E pointing in z dir 
	Nx, Ny = np.shape(Ez)#get shape
	CEx=np.zeros((Nx,Ny),float)
	for nx in range(Nx):
		for ny in range(Ny-1):
			CEx[nx, ny]=(Ez[nx, ny+1]-Ez[nx,ny])/dy#general case
		CEx[nx,Ny-1]=(0-Ez[nx,Ny-1])/dy#boundary condition case
	return CEx

def M_Ez_Curl_Ey(Ez,dx):#curl of E pointing in z dir 
	Nx, Ny = np.shape(Ez)#get shape
	CEy=np.zeros((Nx,Ny),float)
	for ny in range(Ny):
		for nx in range(Nx-1):
			CEy[nx, ny]=-(Ez[nx+1, ny]-Ez[nx,ny])/dx#special case
		CEy[Nx-1,ny]=0
		#-(0-Ez[Nx-1,ny])/dx#boundary condition case
	return CEy

def M_Ez_Curl_Hz(Hx, Hy, dx, dy):
	Nx, Ny= np.shape(Hx)
	CHz=np.zeros((Nx, Ny),float)#shape
	CHz[0,0]=(Hy[0,0]-0)/dx - (Hx[0,0]-0)/dy #sepcial case 
	for nx in range (1,Nx):
		CHz[nx,0]=(Hy[nx,0]-Hy[nx-1,0])/dx - (Hx[nx,0]-0)/dy#firs colomn condition
	for ny in range (1,Ny):
		CHz[0,ny]=(Hy[0,ny]-0)/dx - (Hx[0,ny]-Hx[0,ny-1])/dy#first row special case

		for nx in range(1,Nx):
			CHz[nx,ny]=(Hy[nx,ny]-Hy[nx-1,ny])/dx -(Hx[nx,ny]-Hx[nx,ny-1])/dy
	return CHz	



