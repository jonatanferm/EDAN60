import random
import numpy as np

class nn:
	def __init__(self, h, io):
		def r_11():
			return random.random()*2-1
		self.h = h
		self.io = io
		self.hw = np.array([[4, 1], [1, 0]])
		self.ow = np.array([[1, 0], [0, 1]])
		self.h_hist = []
		self.o_hist = []
		#self.hw = np.array([[r_11() for i in xrange(io)] for k in xrange(h)])
		#self.ow = np.array([[r_11() for i in xrange(h)] for k in xrange(io)])
	def act(self, x):
		#return sum(x)
		return 1/(1+np.exp(-sum(x)))
	def actprime(self, y):
		return abs(y-y*y)
	def calc(self, inp):
		self.h_hist.append(self.act(self.hw*inp))
		self.o_hist.append(self.act(self.ow.transpose()*self.h_hist[-1]))
		return self.o_hist[-1]


n = nn(3, 2)
print n.calc(np.array([1, 1]))

