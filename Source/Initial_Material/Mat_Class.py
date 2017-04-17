import numpy as np
class Mat:

	def __init__(self, row, col):
		self.row= row
		self.col= col
		self.e=np.zeros((row, col),float)
		self.mu=np.zeros((row, col),float)

	def add_mat_bond(self,i_lower,i_upper,j_lower,j_upper,e,mu):#add a block of 2D material
		#This is rather complicated, will consider more
		for i in range(i_lower, i_upper):
			for j in range (j_lower,j_upper):
				self.e[i,j]=e
				self.mu[i,j]=mu
				
			
			

		



