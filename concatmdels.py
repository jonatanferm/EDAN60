import os

path = './Data/Train/libsvm/'
direct = os.listdir(path)
f = open('concd.data', 'w')
for infile in direct:
	f2 = open(path+infile, 'r')
	s = f2.readlines()
	f.writelines(s)
	f2.close
f.close
