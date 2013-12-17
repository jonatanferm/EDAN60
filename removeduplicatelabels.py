f1 = open('concd.data', 'r')
f2 = open('concd.data.fixed', 'w')
for line in f1.xreadlines():
	t = line.split()
	f2.write(t[0])
	d = []
	for i in t[1:]:
		if i not in d:
			f2.write(' '+i)
			d.append(i)

