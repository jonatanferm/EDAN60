import numpy
import random

def r_11():
	return random.random()*2-1

class rnn:
	def __init__(self, io, h):
		self.i_hist = []
		self.h_hist = []
		self.o_hist = []
		self.lh = numpy.array([0 for i in xrange(h)])
		self.lhw = numpy.array([[r_11() for i in xrange(h)] for k in xrange(h)])
		self.hw = numpy.array([[r_11() for i in xrange(io)] for k in xrange(h)])
		self.ow = numpy.array([[r_11() for i in xrange(h)] for k in xrange(io)])

	def act(self, x):
		ex = numpy.exp(-2*x)
		return (1-ex)/(1+ex)
	def actp(self, y):
		return 1-numpy.square(y)
	def calc(self, i):
		th = self.act(sum((i*self.hw).transpose())#+sum((self.lh*self.lhw).transpose()))
		self.lh = th
		to = self.act(sum((th*self.ow).transpose()))
		self.i_hist.append(i)
		self.h_hist.append(th)
		self.o_hist.append(to)
		return to
	def update_w(self):
		do = []
		for i in range(len(i_hist)):
			do.append([])
			do[-1].append((o_hist[i]-i_hist[i])*self.actp(o_hist[i]))
			do[-1].append(numpy.dot(do[-1][0], self.hw)*self.actp(h_hist[i]))
			### DET HÄR ÄR INTE KLART OCH JAG ÄR TRÖTT

			
			


r = rnn(3, 2)
print r.calc(numpy.array([1, 0, 0]))
print r.calc(numpy.array([0, 1, 0]))
print r.calc(numpy.array([0, 0, 1]))
		

