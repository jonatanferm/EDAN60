# coding: UTF-8
import numpy
import random

def r_11():
	return random.random()*2-1
class rnn:
	def __init__(self, io, h):
		self.i_hist = []
		self.h_hist = []
		self.o_hist = []
		self.io = io
		self.h = h
		self.lh = numpy.array([0. for i in xrange(h)])
		self.lhw = numpy.array([[r_11() for i in xrange(h+1)] for k in xrange(h)])
		self.hw = numpy.array([[r_11() for i in xrange(io+1)] for k in xrange(h)])
		self.ow = numpy.array([[r_11() for i in xrange(h+1)] for k in xrange(io)])
	def reset(self):
		self.lh = numpy.array([0 for i in xrange(self.h)])
	def act(self, x):
		return 1/(1+numpy.exp(-x))
	def actp(self, y):
		return y-numpy.square(y)
	def calc(self, i):
		th = self.act(sum((numpy.append(i, 1)*self.hw).transpose()))#+sum((self.lh*self.lhw).transpose()))
		self.lh = th
		to = self.act(sum((numpy.append(th, 1)*self.ow).transpose()))
		self.i_hist.append(i)
		self.h_hist.append(th)
		self.o_hist.append(to)
		return to
	def update_w(self):
		do = []
		l = len(self.i_hist)
		for i in range(l):
			do.append([])
			do[-1].append((self.o_hist[i]-self.i_hist[i])*self.actp(self.o_hist[i]))
			do[-1].append(numpy.dot(self.hw[:,:-1], do[-1][0])*self.actp(self.h_hist[i]))
		self.i_hist = []
		omean = sum(self.o_hist)/l
		self.o_hist = []
		hmean = sum(self.h_hist)/l
		self.h_hist = []
		sow = numpy.array([0. for i in xrange(self.io)])
		shw = numpy.array([0. for i in xrange(self.h)])
		for d in do:
			sow += d[0]
			shw += d[1]
		sow /= l
		shw /= l
		deltawo = sow*omean
		deltawh = shw*hmean
		self.hw[:,:-1] = self.hw[:,:-1]-0.1*((self.hw[:,:-1].transpose()*deltawh).transpose())-0.00001*self.hw[:,:-1]
		self.hw[:,-1] = self.hw[:,-1]-0.1*deltawh
		self.ow[:,:-1] = self.ow[:,:-1]-0.1*((self.ow[:,:-1].transpose()*deltawo).transpose())-0.00001*self.ow[:,:-1]
		self.ow[:,-1] = self.ow[:,-1]-0.1*deltawo


			
			


r = rnn(5, 80)
print r.calc([1, 1, 1, 0, 0])
for i in range(10000):
	for k in xrange(10):
		r.calc([1, 1, 1, 0, 0])
	r.update_w()
	#if i%10 == 0:
	#	raw_input()
	print r.calc([1, 1, 1, 0, 0])
print r.calc([1, 1, 1, 0, 0])
		

