import os
import nltk
import re


if __name__ == "__main__":
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	path = "./Data/Train/Proc/"
	ldir = os.listdir(path)
	for infile in ldir:
		f = open(path+infile, 'r')
		s = f.readlines()
		f.close()
		s = reduce(lambda x, y:x+y, s) #list of lines reduces to a single string
		s = sent_detector.tokenize(s) #Sentences are detected and s is split into a list of sentences
		s = map(nltk.tokenize.word_tokenize, s) #each sentence is tokenized.
		f = open('./Data/Train/Tokenized/'+infile, 'w')
		for t in s:
			for w in t:
				f.write(w)
				f.write('\n')
			f.write('\n')
		f.close()

		

