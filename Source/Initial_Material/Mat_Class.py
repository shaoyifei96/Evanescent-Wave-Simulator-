import numpy as np
class Mat:
	def __init__(self, row, col):
		e0=8.854187817e-12
		mu0=1.2566370614e-6
		self.row= row
		self.col= col
		self.e=np.full((row, col),e0)
		self.mu=np.full((row, col),mu0)

	def add_mat_bond(self,i_lower,i_upper,j_lower,j_upper,e,mu):#add a block of 2D material
		#This is rather complicated, will consider more
		for i in range(i_lower, i_upper):
			for j in range (j_lower,j_upper):
				self.e[i,j]=e
				self.mu[i,j]=mu

			
			

		



