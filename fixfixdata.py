f = open('concd.data.fixed', 'r')
w = open('fixedset.data', 'w')
for line in f.xreadlines():
	t = line.split()
	w.write(t[0])
	t = map(lambda x: x.split(':'), t[1:])
	t = sorted(t, key=lambda x: int(x[0]))
	for i in t:
		w.write(' '+i[0]+':'+i[1])
	w.write('\n')
f.close()
w.close()
