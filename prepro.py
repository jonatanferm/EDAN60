import os
import nltk
import re


def bdrop(f, l, d=0):
	if d > 500:
		return ["ehum"]
	elif l == []:
		return []
	elif f(l[0]):
		return l[1:]
	else:
		return bdrop(f, l[1:], d+1)

if __name__ == "__main__":
	path = "./Data/Train/Raw/"
	ldir = os.listdir(path)
	p = re.compile('\*END\*')
	for infile in ldir:
		f = open(path+infile, 'r')
		s = f.readlines()
		f.close()
		s = bdrop(p.match, s)
		f = open('./Data/Train/Proc/'+infile, 'w')
		f.writelines(s)
		f.close()

		

