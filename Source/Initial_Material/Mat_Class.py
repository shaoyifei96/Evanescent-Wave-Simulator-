import numpy as np
class Mat:
	def __init__(self, row, col, dt):
		self.e0=1
		self.mu0=1
		self.c0=1#wrong number for not explode
		self.dt=dt
		self.row= row
		self.col= col
		self.e=np.full((row, col),self.e0)
		self.mu=np.full((row, col),self.mu0)
		self.M_Ez_Coef_Ex=-self.c0*dt/self.mu
		self.M_Ez_Coef_Ey=self.c0*dt/self.mu
		self.M_Ez_Coef_Hz=self.c0*dt#thi is a const indenpendent of material property
		self.M_Ez_Coef_Dz=1/self.e


	def add_mat_bond(self,i_lower,i_upper,j_lower,j_upper,e,mu):#add a block of 2D material
		#This is rather complicated, will consider more
		self.e[i_lower:i_upper,j_lower:j_upper] =e
		self.mu[i_lower:i_upper,j_lower:j_upper]=mu
		self.M_Ez_Coef_Ex[i_lower:i_upper,j_lower:j_upper]=-self.c0*self.dt/self.mu[i_lower:i_upper,j_lower:j_upper]
		self.M_Ez_Coef_Ey[i_lower:i_upper,j_lower:j_upper]=self.c0*self.dt/self.mu[i_lower:i_upper,j_lower:j_upper]
		self.M_Ez_Coef_Dz[i_lower:i_upper,j_lower:j_upper]=1/self.e[i_lower:i_upper,j_lower:j_upper]
		
		
	
	def add_mat_bond_advanced(self,f,i_lower,i_upper,e,mu):
		for i in range (i_lower,i_upper):
			j_upper =int(f(i))
			self.add_mat_bond(i,i+1,0,j_upper,e,mu)

			
			

		



