import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print '\n'
print 'making feature plots'

#read in training dataset
df = pd.read_csv('train.csv')
cols = ['LowWin',
 'diff_ast',
 'diff_blk',
 'diff_dr',
 'diff_fga',
 'diff_fga3',
 'diff_fgm',
 'diff_fgm3',
 'diff_fta',
 'diff_ftm',
 'diff_or',
 'diff_pf',
 'diff_score',
 'diff_seed',
 'diff_stl',
 'diff_to']
df = df[cols]

#split training datafram into feature vector "X" and result vector "y"
X = df.ix[:,1:20].values
y = df.ix[:,0:1].values

#save overlaid histogram for each feature for winning and losing outcomes
for i in range(0,len(cols)-1):
    plt.hist(X[y[:,0]==0, i], label='lose', alpha=0.4, normed=1)
    plt.hist(X[y[:,0]==1, i], label='win', alpha=0.4, normed=1)
    plt.xlabel(cols[i+1])
    plt.ylabel('fraction')
    plt.legend(loc='upper right', fancybox=True, fontsize=12)
    plt.savefig('fig/'+cols[i+1]+'.png')
    plt.close()

print 'feature plots saved in fig dir'
