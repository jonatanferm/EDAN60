f = open('concd.data.fixed', 'r')
w = open('fixedset.data', 'w')
for line in f.xreadlines():
	t = line.split()
	mf = int(t[0])
	w.write(t[0])
	for i in t[1:]:
		if mf != int(i.split(':')[0]):
			w.write(' '+i)
	w.write('\n')
f.close()
w.close()

