import os
import sys
sys.path.append('./liblinear-1.94/python')
from liblinearutil import *

path = './Data/Train/libsvm/'
ldir = os.listdir(path)
c = 0
for infile in ldir:
	c += 1
	print c
	x, y = svm_read_problem(path+infile)
	m = train(x, y, '-s 7')
	save_model('./Data/Train/models/'+infile)
