import cPickle as pkl
import re

f2 = open("3gram1w.pkl", 'r')
r = pkl.load(f2)
f2.close()

f1 = open("./Data/Test/Holmes.machine_format.questions.txt", 'r')
q = f1.readlines()
f1.close()

answers = []

rc = re.compile("\[")
def best_alt(l):
	lt = map(lambda x: x.split(), l)
	def c3g(f):
		def rf(tl, c=0):
			if f(tl[c]):
				return map(lambda x: x+'\n', tl[c-2:c]+[tl[c][1:-1]]+tl[c+1:c+3])
			else:
				return rf(tl, c+1)
		return rf
	lt = map(c3g(rc.match), lt)
	def l2p(tl):
		def prob(i):
			if i[0] in r and i[1] in r[i[0]][1] and i[2] in r[i[0]][1][i[1]][1]:
				d1 = r[i[0]][1][i[1]][1][i[2]]
			elif i[1] in r and i[2] in r[i[1]][1]:
				d1 = r[i[1]][1][i[2]][0]
			else:
				return 0
			if i[2] in r and i[3] in r[i[2]][1] and i[4] in r[i[2]][1][i[3]][1]:
				d2 = r[i[2]][1][i[3]][1][i[4]]
			elif i[3] in r and i[4] in r[i[3]][1]:
				d2 = r[i[3]][1][i[4]][0]
			else:
				return 0
			return d1*d2
		return map(prob, tl)
	lt = l2p(lt)
	mp = 0
	mi = 0
	for i in range(len(lt)):
		if lt[i] > mp:
			mp = lt[i]
			mi = i
	return l[mi]

for i in range(len(q)/5):
	temp = []
	for k in range(5):
		temp.append(q[i*5+k])
	answers.append(best_alt(temp))

f3 = open("./Data/Test/ngramanswers.txt", 'w')
for a in answers:
	f3.write(a)
f3.close()

