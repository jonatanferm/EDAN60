import os
import nltk
import re
import cPickle as pkl

if __name__ == "__main__":
	path = "./Data/Train/Tokenized/"
	ldir = os.listdir(path)
	r = {}
	z = 0
	for infile in ldir:
		f = open(path+infile, 'r')
		s = f.readlines()
		z += len(s)
		f.close()
		for i in range(len(s)-2):
			if s[i] not in r:
				r[s[i]] = [1., {}]
			else:
				r[s[i]][0] += 1
			if s[i+1] not in r[s[i]][1]:
				r[s[i]][1][s[i+1]] = [1., {}]
			else:
				r[s[i]][1][s[i+1]][0] += 1
			if s[i+2] not in r[s[i]][1][s[i+1]][1]:
				r[s[i]][1][s[i+1]][1][s[i+2]] = 1.
			else:
				r[s[i]][1][s[i+1]][1][s[i+2]] += 1.
	for k1 in r.keys():
		for k2 in r[k1][1].keys():
			for k3 in r[k1][1][k2][1].keys():
				r[k1][1][k2][1][k3] /= r[k1][1][k2][0]
			r[k1][1][k2][0] /= r[k1][0]
		r[k1][0] /= z


	f = open('3gram1w.pkl', 'w')
	pkl.dump(r, f)
	f.close()
else:
	r = {}
	s = ["hej", "pa", "dig", "din", "fuling", "test", "dig", "din", "foo", "", ""]
	for i in range(2, len(s)-2):
		if s[i] not in r:
			r[s[i]] = [{}, 1., {}]
		else:
			r[s[i]][1] += 1
		if s[i+1] not in r[s[i]][2]:
			r[s[i]][2][s[i+1]] = [1., {}]
		else:
			r[s[i]][2][s[i+1]][0] += 1
		if s[i-1] not in r[s[i]][0]:
			r[s[i]][0][s[i-1]] = [1., {}]
		else:
			r[s[i]][0][s[i-1]][0] += 1
		if s[i+2] not in r[s[i]][2][s[i+1]][1]:
			r[s[i]][2][s[i+1]][1][s[i+2]] = 1.
		else:
			r[s[i]][2][s[i+1]][1][s[i+2]] += 1
		if s[i-2] not in r[s[i]][0][s[i-1]][1]:
			r[s[i]][0][s[i-1]][1][s[i-2]] = 1.
		else:
			r[s[i]][0][s[i-1]][1][s[i-2]] += 1
	z = len(s)
	for k in r.keys():
		for k1 in r[k][0].keys():
			for k1a in r[k][0][k1][1].keys():
				r[k][0][k1][1][k1a] /= r[k][0][k1][0]
			r[k][0][k1][0] /= r[k][1]
		for k1 in r[k][2].keys():
			for k1a in r[k][2][k1][1].keys():
				r[k][2][k1][1][k1a] /= r[k][2][k1][0]
			r[k][2][k1][0] /= r[k][1]
		r[k][1] /= z

	for k in r.keys():
		print k
		print r[k]
