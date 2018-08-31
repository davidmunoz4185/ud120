#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import tree
from sklearn.metrics import accuracy_score

clf_2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf_2.fit(features_train, labels_train)
pred_2 = clf_2.predict(features_test)
print accuracy_score(pred_2, labels_test)

print len(features_train[0])

clf_50 = tree.DecisionTreeClassifier(min_samples_split=50)
clf_50.fit(features_train, labels_train)
pred_50 = clf_50.predict(features_test)
print accuracy_score(pred_50, labels_test)

"""
from sklearn.neighbors.nearest_centroid import NearestCentroid
clf = NearestCentroid(shrink_threshold=shrinkage)
clf.fit(features_train, labels_train)
NearestCentroid(metric='euclidean', shrink_threshold=None)
pred = clf.predict(features_test)
print accuracy_score(pred, labels_test)
"""
#########################################################


"""
def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg
    
    ### your code goes here!
    from sklearn import linear_model
    reg = linear_model.LinearRegression()
    reg.fit(ages_train, net_worths_train)
    
    
    return reg
"""

from sklearn.linear_model import LinealRegression
reg = LinearRegression()
reg.fit(ages_train, net_worths_train)

print "katie's net worth prediction:", reg.predict([27])
print "slope:", reg.coef_
print "intercept:", reg.intercept_

print "\n ############### stats on test dataset ####################\n"
print "r-squared score:", reg.score(ages_test, net_worths_test)

print "\n ############### stats on training dataset ####################\n"
print "r-squared score:", reg.score(ages_train, net_worths_train)