import numpy as np
class Mat:

	def __init__(self, row, col):
		self.row= row
		self.col= col
		self.e=np.zeros((row, col),float)
		self.mu=np.zeros((row, col),float)

	def add_mat_bond(i,j,e,mu):
		#This is rather complicated, will consider more
		self.e[i,j]=e
		self.mu[i,j]=mu
		



