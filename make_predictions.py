import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

print '\n'
print 'making predictions'

#read in training and testing datasets created earlier
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

#the set of input features
predictors = ['diff_seed',
              'diff_score',
              'diff_fgm',
              'diff_fga',
              'diff_fgm3',
              'diff_fga3',
              'diff_ftm',
              'diff_fta',
              'diff_or',
              'diff_dr',
              'diff_ast',
              'diff_to',
              'diff_stl',
              'diff_blk',
              'diff_pf'
]

####################################################
## train logistic regression and make predictions ##
####################################################
alg = LogisticRegression(random_state=1, penalty='l2')
alg.fit(train_df[predictors], train_df["LowWin"])
predictions = alg.predict_proba(test_df[predictors].astype(float))[:,1]

scores = cross_validation.cross_val_score(alg, train_df[predictors], train_df["LowWin"], cv=3)
print 'Logistic Regression mean cross validation accuracy = ', scores.mean()

sub_pred = {}
counter = 0
for index, row in test_df.iterrows():
    year = row['Season']
    entry = '_'
    entry = entry.join( ( str(int(row['Season'])), str(int(row['LowTeam'])), str(int(row['HighTeam'])) ) )
    sub_pred[entry] = predictions[counter]
    counter += 1

submission = pd.DataFrame(sub_pred.items(), columns = ['id', 'pred'])
outfile = 'submission_logisticRegression.csv'
submission.to_csv(outfile, index=False)
print 'Logistic Regression predictions saved to', outfile


##############################################
## train random forest and make predictions ##
##############################################
alg = RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=8, min_samples_leaf=4)
alg.fit(train_df[predictors], train_df["LowWin"])
predictions = alg.predict_proba(test_df[predictors].astype(float))[:,1]

scores = cross_validation.cross_val_score(alg, train_df[predictors], train_df["LowWin"], cv=3)
print 'Random Forest mean cross validation accuracy = ', scores.mean()

sub_pred = {}
counter = 0
for index, row in test_df.iterrows():
    year = row['Season']
    entry = '_'
    entry = entry.join( ( str(int(row['Season'])), str(int(row['LowTeam'])), str(int(row['HighTeam'])) ) )
    sub_pred[entry] = predictions[counter]
    counter += 1

submission = pd.DataFrame(sub_pred.items(), columns = ['id', 'pred'])
outfile = 'submission_randomForest.csv'
submission.to_csv(outfile, index=False)
print 'Random Forest predictions saved to', outfile
