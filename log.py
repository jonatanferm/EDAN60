import sys
sys.path.append('./liblinear-1.94/python')
from liblinearutil import *

y, x = svm_read_problem('concd.data')
m = train(y, x, '-s 0 -v 4')
save_model('concd.model', m)



