import os



tokpath = './Data/Train/Features/'
svmpath = './Data/Train/libsvm/'

dir1 = os.listdir(tokpath)
for infile in dir1:
	f = open(tokpath+infile, 'r')
	s = f.readlines()
	f.close()
	f = open(svmpath+infile, 'w')
	cursent = []
	for line in s:
		if line != "22445\n": #the code for a new sentence
			cursent.append(line)
		else:
			for i in range(len(cursent)):
				if cursent[i] != '0\n': #the code for an unknown word
					f.write(cursent[i][:-1]+' ')
					for j in cursent[:i]:
						f.write(j[:-1]+':1 ')
					for j in cursent[i+1:]:
						f.write(str(int(j)+54659)+':1 ')
					f.write('\n')
			cursent = []
	f.close()
