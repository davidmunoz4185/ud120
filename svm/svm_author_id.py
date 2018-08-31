#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

t0 = time()

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# Only 1% of data
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC
clf = SVC(kernel="linear")
clf = SVC(C=1.0, kernel="rbf") # --> 0.61 accuraty
clf = SVC(C=10.0, kernel="rbf") # --> 0.61 accuraty
clf = SVC(C=100.0, kernel="rbf") # --> 0.61 accuraty
clf = SVC(C=1000.0, kernel="rbf") # --> 0.82 accuraty
clf = SVC(C=10000.0, kernel="rbf") # --> 0.89 accuraty
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)


print len(filter(lambda x:x==1,pred))

print("pred[10]: ",pred[10])
print("pred[26]: ",pred[26])
print("pred[50]: ",pred[50])
print("pred[1]: ",pred[1])

from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)
print "accuracy time:", round(time()-t0, 3), "s"

"""
from sklearn import tree
from sklearn.metrics import accuracy_score

clf_2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf_2.fit(features_train, labels_train)
pred_2 = clf_2.predict(features_test)
acc_min_samples_split_2 = accuracy_score(pred_2, labels_test)

clf_50 = tree.DecisionTreeClassifier(min_samples_split=50)
clf_50.fit(features_train, labels_train)
pred_50 = clf_50.predict(features_test)
acc_min_samples_split_50 = accuracy_score(pred_50, labels_test)
"""



#########################################################
### your code goes here ###

#########################################################


"""
import math
-0.5*log(0.5, 2) - 0.5*log(0.5, 2) 
"""