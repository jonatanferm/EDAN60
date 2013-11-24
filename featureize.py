import cPickle as pkl
import os

if __name__ == '__main__':
	path = './Data/Train/Tokenized/'
	ldir = os.listdir(path)
	r = {}
	for infile in ldir:
		f = open(path + infile, 'r')
		s = f.readlines()
		f.close()
		for w in s:
			if w.lower() not in r:
				r[w.lower()] = 1
			else:
				r[w.lower()] += 1
	c = 1
	f = open('./w2f.legend', 'w')
	f.write('<UnknownWord> 0\n')
	for k in r.keys():
		if r[k] < 10:
			print k
			del(r[k])
		else:
			f.write(k + ' ' + str(c) + '\n')
			r[k] = c
			c += 1
	f.close()
	f = open('./w2f.pkl', 'w')
	pkl.dump(r, f)
	f.close()
	fpath = './Data/Train/Features/'
	print "dictionary done, featureizing data."
	for infile in ldir:
		f = open(path + infile, 'r')
		s = f.readlines()
		f.close()
		f = open(fpath + infile, 'w')
		for w in s:
			if w.lower() in r:
				f.write(str(r[w.lower()])+'\n')
			else:
				f.write('0\n')
		f.close()


	

