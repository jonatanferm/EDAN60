import cPickle as pkl
rpath = './Data/Test/Holmes.machine_format.answers.txt'
spath = './models/liblinquestions.txt'
f = open(rpath, 'r')
sf = open(spath, 'w')

pick = open('w2f.pkl', 'r')
r = pkl.load(pick)
pick.close()

lines = f.readlines()
f.close()
for i in range(0, len(lines)):
	temp = lines[i][1:]
	a = 0
	tw = []
	c = None
	for k in temp:
		if k[0] == '[':
			a = 54659
			if k[1:-1]+'\n' in r:
				c = r[k[1:-1]+'\n']
		elif k+'\n' in r:
			tw.append(r[k+'\n']+a)
	
	if c:
		sf.write(str(c))
		for k in sorted(list(set(tw))):
			sf.write(' ')
			sf.write(str(k))
			sf.write(':1')
	sf.write('\n')
sf.close()

	
